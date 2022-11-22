import random
from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser
# Create your models here.
class TestAnswer(models.Model):
    content = models.CharField(max_length=500,verbose_name="Variant")
    is_true = models.BooleanField(default=False,verbose_name='To\'g\'ri yoki xatoligi')

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variantlar"
    
    def __str__(self) -> str:
        return self.content

class TestQuestion(models.Model):
    content = RichTextField(verbose_name="Savol matni")
    answers = models.ManyToManyField(TestAnswer,verbose_name='Variantlar')
    def is_true(self):
        return self.answers.filter(is_true=True).all().first()

    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
    def __str__(self) -> str:
        return self.content

class UserTest(models.Model):
    question = models.ForeignKey(TestQuestion,on_delete=models.CASCADE)
    answer = models.ForeignKey(TestAnswer,on_delete=models.CASCADE)
    is_true  = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if TestAnswer.objects.filter(id=self.answer_id).first().is_true:
            self.is_true = True
        super(UserTest, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.question.content

class UserTestResult(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tests = models.ManyToManyField(UserTest)

    def is_trues(self):
        return self.tests.filter(is_true=True).count()
    
    def result(self):
        if (self.tests.filter(is_true=True).count()) > 0:
            r = (self.tests.filter(is_true=True).count()*100) / self.tests.count()
            return '{:.2f}'.format(r)
        else: return 0git 


    def __str__(self) -> str:
        return self.user.get_full_name()

    class Meta:
        ordering = ['-date']

