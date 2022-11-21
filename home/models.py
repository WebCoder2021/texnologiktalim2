from django.db import models
from ckeditor.fields import RichTextField
from .validators import validate_file_extension
# Create your models here.
class Books(models.Model):
    image = models.ImageField(upload_to='themes',verbose_name="Rasm")
    title = models.CharField(max_length=500,verbose_name="Kitob nomi")
    author = models.CharField(max_length=200,verbose_name='Kitob muallifi')
    file = models.FileField(upload_to='books',verbose_name='Kitob fayli',validators=[validate_file_extension])
    url = models.URLField(verbose_name='Kitob url manzili',blank=True,null=True)

    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar"
    def __str__(self) -> str:
        return self.title

class InternetResources(models.Model):
    image = models.ImageField(upload_to='themes',verbose_name="Resurs rasmi")
    title = models.CharField(max_length=500,verbose_name='Sarlavha')
    content = models.CharField(max_length=500,verbose_name='Qisqacha',null=True)
    url = models.URLField(verbose_name='Resurs url manzili')

    class Meta:
        verbose_name = "Internet resurs"
        verbose_name_plural = "Internet resurslar"
    def __str__(self) -> str:
        return self.title

class VideoCategory(models.Model):
    name = models.CharField(max_length=200,unique=True)
    def videos(self):
        return VideoLessons.objects.filter(category__name=self.name)
    def __str__(self):
        return self.name
class VideoLessons(models.Model):
    category = models.ForeignKey(VideoCategory,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=500,verbose_name='Sarlavha')
    iframe = models.TextField(null=True,blank=True,verbose_name="YouTube ifareme")

    class Meta:
        verbose_name = "Video dars"
        verbose_name_plural = "Video darslar"
    def __str__(self) -> str:
        return self.title




class Questionnaire(models.Model):
    publish = models.BooleanField(default=False,verbose_name="So'rovnoma holati")
    title = models.CharField(max_length=500,verbose_name="So'rovnoma savoli")
    ans1 = models.CharField(max_length=200,verbose_name="Variant")
    ans2 = models.CharField(max_length=200,verbose_name="Variant")
    ans3 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    ans4 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    ans5 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    ans6 = models.CharField(max_length=200,null=True,blank=True,verbose_name="Variant")
    res1 = models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    res2 = models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    res3 = models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    res4 = models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    res5 = models.PositiveSmallIntegerField(null=True,blank=True,default=0)
    res6 = models.PositiveSmallIntegerField(null=True,blank=True,default=0)

    class Meta:
        verbose_name = "So'rovnoma"
        verbose_name_plural = "So'rovnomalar"
    def __str__(self) -> str:
        return self.title
    def nums(self):
        return self.res1+self.res2+self.res3+self.res4+self.res5+self.res6

class IncomingMessages(models.Model):
    fullname = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    direction = models.CharField(max_length=250)
    phone = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname + " "  + self.content