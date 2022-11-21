from django.urls import path
from .views import *
urlpatterns = [
    path('', modules,name='modules'),
    path('<slug:slug>/', module,name='module'),
    
]