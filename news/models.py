from django.db import models
from ckeditor.fields import RichTextField
from users.models import CustomUser
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Yangilik kategoriyalari'
        verbose_name = 'Yangilik kategoriyasi'

    def __str__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Yangilik teglari'
        verbose_name = 'Yangilik tegi'

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=250,verbose_name='Sarlavha')
    sub_title = models.CharField(max_length=500,verbose_name='Tag lavha')
    image = models.ImageField(upload_to='events',verbose_name='Ram')
    content = RichTextField(verbose_name='Yangilik matni')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='Kim tomonidan qo\'shildi')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Kategoriya')
    tags = models.ManyToManyField(Tag,verbose_name='Teglar')
    created = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,verbose_name='Url manzil')
    class Meta:
        verbose_name_plural = 'Yangilik'
        verbose_name = 'Yangiliklar'
    def __str__(self):
        return self.title

class PostCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def posts_count(self):
        num = Post.objects.filter(category=self.id).count()
        return num
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Maqola kategoriyalari'
        verbose_name = 'Maqola kategoriyasi'
class PostTag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        verbose_name_plural = 'Maqola teglari'
        verbose_name = 'Maqola tegi'
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250,verbose_name='Sarlavha')
    sub_title = models.CharField(max_length=500,verbose_name='Tag sarlavha')
    image = models.ImageField(upload_to='events',verbose_name='Rasm')
    content = RichTextField(verbose_name='Maqola xabari',null=True,blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,verbose_name='Kim qo\'shganligi')
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE,verbose_name='Kategoriya')
    tags = models.ManyToManyField(PostTag,verbose_name='Teglar')
    created = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True,verbose_name='Url manzil')
    url = models.URLField(verbose_name='Kitob url manzili',blank=True,null=True)
    class Meta:
        verbose_name_plural = 'Maqolalar'
        verbose_name = 'Maqola'
    def comments(self):
        comment = PostComment.objects.filter(post__slug=self.slug)
        return comment

    def __str__(self):
        return self.title

class PostComment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    content = models.TextField()
    def __str__(self):
        return self.content
    class Meta:
        verbose_name_plural = 'Maqola izohlari'
        verbose_name = 'Maqola izohi'