from django.shortcuts import render

from users.models import CustomUser
from .models import *
# Create your views here.
def finalcontrol(request):
    context = {}
    context['lessons'] = Lesson.objects.all()
    if request.method == 'GET':
        print(request.GET)
        lesson_check = request.GET.get('lesson',False)
        user_check = request.GET.get('username',False)
        print(lesson_check,user_check)
        if CustomUser.objects.filter(username=user_check).exists():
            user = CustomUser.objects.get(username=user_check)
            context['user'] = user
            print(user)
        if lesson_check:
            lesson = Lesson.objects.filter(name=lesson_check).first()
            context['lesson'] = lesson
            print(lesson)
            if user and lesson:
                start = request.GET.get('start',False)
                if start:
                    context['start'] = True
                context['old_results'] = UserControlTestResult.objects.filter(user=request.user)
                context['tests'] = FinalControlTest.objects.filter(lesson_id=1).all().order_by('?')[:5]

    else:
        context['user_err'] = "Bunday foydalanuvchi mavjud emas"
    
    if request.method == 'POST':
        user_id = request.GET.get('username',False)
        lesson_check = request.GET.get('lesson',False)
        user = CustomUser.objects.get(username=user_id)
        lesson = Lesson.objects.filter(name=lesson_check).first()
        result = UserControlTestResult.objects.create(user=user,lesson=lesson)
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

