from django.shortcuts import render
from django.core.paginator import Paginator

from modul.models import Module
from .models import *
# Create your views here.
def events (request):
    events = Event.objects.all()
    category = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'events': events,
        'category': category,
        'tags': tags,
    }
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'news/events.html',context)
def event_detail(request,slug):
    context ={}
    event = Event.objects.filter(slug=slug).first()
    context['event'] = event
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'news/event-details.html',context)
def blog (request):
    posts = Post.objects.all()
    category = PostCategory.objects.all()
    tags = PostTag.objects.all()
    if request.method == "GET":
        ct = request.GET.get('ct',False)
        tg = request.GET.get('tg',False)
        if ct:
            posts = Post.objects.filter(category__id=ct).all()
        if tg:
            posts = Post.objects.filter(tags__id__in=[tg])
    popular_posts = Post.objects.all().order_by('-update_date')[:5]
    paginator = Paginator(posts.order_by('-id'), 5)
    page_number = request.GET.get('page')
    context = {
        'posts': paginator.get_page(page_number),
        'category': category,
        'popular_posts': popular_posts,
        'tags': tags,
    }
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'news/blog-home.html',context)
def blog_detail(request,slug):
    context = {}
    post = Post.objects.filter(slug=slug).first()
    popular_posts = Post.objects.exclude(slug=slug).order_by('-update_date')[:5]
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment = request.POST.get('comment', False)
        if comment:
            cm = PostComment.objects.create(user=request.user, post=post,content=comment)
            cm.save()
    category = PostCategory.objects.all()
    tags = PostTag.objects.all()
    context = {
        'post': post,
        'popular_posts': popular_posts,
        'category': category,
        'tags': tags,
    }
    context['modules'] = Module.objects.all().order_by('order')
    return render(request,'news/blog-single.html',context)