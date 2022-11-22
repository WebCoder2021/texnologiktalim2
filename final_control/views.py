from django.shortcuts import render

from users.models import CustomUser
from .models import *
# Create your views here.
def finalcontrol(request):
    context = {}
    if request.method == 'GET':
            start = request.GET.get('start',False)
            if start:
                context['start'] = True
    if request.user.is_authenticated:
        context['old_results'] = UserControlTestResult.objects.filter(user=request.user)
        context['tests'] = FinalControlTest.objects.filter(lesson_id=1).all().order_by('?')[:5]
        lesson = Lesson.objects.all().first()
        context['lesson'] = lesson
        result = UserControlTestResult.objects.create(user=request.user,lesson=lesson)
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

