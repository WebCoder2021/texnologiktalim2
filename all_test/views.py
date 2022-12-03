from django.shortcuts import render

from home.bot_send import bot_send, get_test_result
from .models import *
# Create your views here.
def test(request):
    context = {}
    if request.user.is_authenticated:
        context['tests'] = TestQuestion.objects.all().order_by('?')[:5]
        context['old_results'] = UserTestResult.objects.filter(user=request.user)
        if request.method == 'GET':
            start = request.GET.get('start',False)
            if start:
                context['start'] = True
        if request.method == "POST":
            result = UserTestResult.objects.create(user=request.user)
            for p,value in request.POST.items():
                if p != "csrfmiddlewaretoken":
                    ts = UserTest.objects.create(question_id=int(p),answer_id=int(value))
                    ts.save()
                    result.tests.add(ts)
                    result.save()
                    context['result'] = result

            bot_send(get_test_result(result.id))




            # result = UserTestResult.objects.create(user=request.user)
            # for test in tests:
            #     ts = UserTest.objects.create(question_id=int(test.id),answer_id=int(request.POST.get(str(test.id),False)))
            #     ts.save()

                # result.tests.add(ts)
                # result.save()
                # context['result'] = result


    return render(request,'test/test.html',context)