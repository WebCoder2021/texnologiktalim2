from django.urls import path
from .views import *
urlpatterns = [
    path('', events, name='events'),
    path('event/<slug:slug>/detail', event_detail, name='event_detail'),
    path('blog', blog, name='blog'),
    path('blog/<slug:slug>/detail', blog_detail, name='blog_detail'),

]