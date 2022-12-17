from django.db import models

from users.models import CustomUser

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.name

class FinalControlTest(models.Model):
    question = models.CharField(max_length=500)
    image = models.ImageField(upload_to='tests/images/',null=True,blank=True)
    ans = models.CharField(max_length=500)
    ans1 = models.CharField(max_length=500)
    ans2 = models.CharField(max_length=500)
    ans3 = models.CharField(max_length=500)
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)

    def __str__(self):
        return self.question + ' - ' + str(self.lesson.name)

    def answers(self):
        context = [
            { 'name':self.ans, 'is_true':True },
            { 'name':self.ans1, 'is_true':False },
            { 'name':self.ans2, 'is_true':False },
            { 'name':self.ans3, 'is_true':False },
            ]
        return list(context)


class ControlTest(models.Model):
    question = models.ForeignKey(FinalControlTest,on_delete=models.CASCADE)
    answer = models.CharField(max_length=500,null=True)
    is_true  = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.question.question


class UserControlTestResult(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tests = models.ManyToManyField(ControlTest)
    
    def result(self):
        if (self.tests.filter(is_true=True).count()) > 0:
            r = (self.tests.filter(is_true=True).count()*100) / self.tests.count()
            return '{:.2f}'.format(r)
        else: return 0
    
    def is_trues(self):
        return self.tests.filter(is_true=True).count()


    def __str__(self) -> str:
        return self.user.get_full_name()

    class Meta:
        ordering = ['-date']

class UserTestsResult(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    tests = models.ManyToManyField(ControlTest)

    def result(self):
        if (self.tests.filter(is_true=True).count()) > 0:
            r = (self.tests.filter(is_true=True).count()*100) / self.tests.count()
            return '{:.2f}'.format(r)
        else: return 0

    def is_trues(self):
        return self.tests.filter(is_true=True).count()


    def __str__(self) -> str:
        return self.user.get_full_name()

    class Meta:
        ordering = ['-date']