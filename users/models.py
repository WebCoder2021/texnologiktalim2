from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username fields is required")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)
# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('Username'), max_length=200, unique=True
    )
    first_name = models.CharField(max_length=100,null=True,blank=True,verbose_name='Ism')
    last_name = models.CharField(max_length=100,null=True,blank=True,verbose_name='Familiya')
    middle_name = models.CharField(max_length=100,null=True,blank=True,verbose_name='Sharif')
    picture = models.ImageField(upload_to='user/',null=True,verbose_name='Rasm',blank=True,default='user.jpg')
    email = models.EmailField(max_length=200,null=True,blank=True,verbose_name='Email')
    location = models.CharField(max_length=250,null=True,blank=True,verbose_name='Manzil')
    faculty = models.CharField(max_length=250,null=True,blank=True,verbose_name='Fakultet')
    direction = models.CharField(max_length=250,null=True,blank=True,verbose_name='Yo\'nalish')
    group = models.CharField(max_length=250,null=True,blank=True,verbose_name='Guruh')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_seen = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.username + ' ' + str(self.get_full_name())

    def get_full_name(self):
        ful_name = ' '
        if self.first_name:
            ful_name += self.first_name
        if self.last_name:
            ful_name += ' ' + self.last_name
        if self.middle_name:
            ful_name += ' ' + self.middle_name
        return  ful_name
    def get_absolute_url(self):
        return f'/users/{self.id}'

    def get_update_url(self):
        return f'/users/{self.id}/update'

    def get_delete_url(self):
        return f'/users/{self.id}/delete'

