from django.shortcuts import redirect, render

from users.models import CustomUser
from .models import *
# Create your views here.
def finalcontrol(request):
    context = {}
    if request.user.is_authenticated and request.user.is_superuser:
        context['lessons'] = Lesson.objects.all()
        if request.method == 'GET':
            lesson_check = request.GET.get('lesson',False)
            user_check = request.GET.get('username',False)
            if CustomUser.objects.filter(username=user_check).exists() and Lesson.objects.filter(name=lesson_check).exists():
                user = CustomUser.objects.get(username=user_check)
                context['user'] = user
                if lesson_check:
                    lesson = Lesson.objects.filter(name=lesson_check).first()
                    context['lesson'] = lesson
                    if user and lesson:
                        start = request.GET.get('start',False)
                        if start:
                            context['start'] = True
                        context['old_results'] = UserControlTestResult.objects.filter(user=user,lesson=lesson)
                        context['tests'] = FinalControlTest.objects.filter(lesson=lesson).all().order_by('?')[:5]
                else:
                    context['user_err'] = "Ma'lumotlar xato kiritildi"
                    print(context['user_err'])
        if request.method == 'POST':
            user_id = request.GET.get('username',False)
            lesson_check = request.GET.get('lesson',False)
            user = CustomUser.objects.get(username=user_id)
            lesson = Lesson.objects.filter(name=lesson_check).first()
            result = UserControlTestResult.objects.create(user=user,lesson=lesson)
            context['old_results'] = UserControlTestResult.objects.filter(user=user,lesson=lesson)
            context['user'] = user
            context['lesson'] = lesson
            for p,value in request.POST.items():
                    if p != "csrfmiddlewaretoken":
                        question = FinalControlTest.objects.filter(id=int(p)).first()
                        ts = ControlTest.objects.create(question_id=int(p))
                        ts.answer = value
                        if question.ans == value:
                            ts.is_true = True
                        ts.save()
                        result.tests.add(ts)
                        result.save()
                        context['result'] = result
        return render(request,'finalcontrol/finalcontrol.html',context)
    else:
        return redirect('home')

