from django.shortcuts import render
from .models import *
# Create your views here.
def finalcontrol(request):
    context = {}
    if request.method == 'GET':
            start = request.GET.get('start',False)
            if start:
                context['start'] = True
    if request.user.is_authenticated:
        context['tests'] = FinalControlTest.objects.filter(lesson_id=1).all().order_by('?')[:5]
        context['lesson'] = Lesson.objects.all().first()


        

    return render(request,'finalcontrol/finalcontrol.html',context)