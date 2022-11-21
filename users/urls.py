from django.urls import path
from .views import *
urlpatterns = [
    path('', log_in,name='login'),
    path('logout/', logout_view,name='logout'),
    path('check_user/', check_user,name='check_user'),
    path('settings/', settings, name="settings"),
    path('profile/', profile, name="profile"),
    path('test/', test_result, name="test_result"),
    path('test/<int:id>/', user_test_info, name="user_test_info"),
    
]