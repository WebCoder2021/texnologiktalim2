from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Module(models.Model):
    image = models.ImageField(upload_to='modules',verbose_name='Rasm',null=True,blank=True)
    name = models.CharField(max_length=500)
    order = models.PositiveSmallIntegerField(default=1)
    slug = models.SlugField(unique=True,null=True)
    def themes(self):
        themes = Theme.objects.filter(module__name=self.name).all()
        return themes
    class Meta:
        verbose_name = "Modul"
        verbose_name_plural = "Modullar"
    def __str__(self) -> str:
        return self.name

class Theme(models.Model):
    module = models.ForeignKey(Module,on_delete=models.CASCADE,verbose_name="Modul")
    image = models.ImageField(upload_to='themes',verbose_name='Mavzu')
    title = models.CharField(max_length=500,verbose_name='Nomi')
    order = models.PositiveSmallIntegerField(default=0,verbose_name='Mavzu tartib raqami')
    content = RichTextField(verbose_name="Mazmuni")
    slug = models.SlugField(unique=True,null=True) 

    def questions(self):
        q = Question.objects.filter(theme_title=self.title).all()
        return q
    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = "Mavzular"
    def __str__(self) -> str:
        return self.title

class Answer(models.Model):
    content = models.CharField(max_length=500,verbose_name="Variant")
    is_true = models.BooleanField(default=False,verbose_name='To\'g\'ri yoki xatoligi')

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variantlar"
    
    def __str__(self) -> str:
        return self.content

class Question(models.Model):
    theme = models.ForeignKey(Theme, on_delete = models.CASCADE,verbose_name="Mavzuni tanlang")
    content = models.CharField(max_length=500,verbose_name='Savol matni')
    answers = models.ManyToManyField(Answer,verbose_name='Variantlar')
    order = models.PositiveSmallIntegerField(default=1,verbose_name='Savol tartib raqami')

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
        ordering = ['order']
    
    def __str__(self) -> str:
        return self.content




