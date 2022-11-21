from django.shortcuts import render
from .models import *

# Create your views here.
def modules(request):
    context = {}
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'modules/modules.html',context)
def module(request,slug):
    context = {}
    context['md'] = Module.objects.filter(slug=slug).first()
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'modules/module.html',context)