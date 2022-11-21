from django.db import models

# Create your models here.
class Lesson(models.Model):
    name = models.CharField(max_length=200)
    course = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.name + ' - ' + str(self.course)

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
