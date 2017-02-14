from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.
from ckeditor.fields import RichTextField
class Navigation(models.Model):
    nav_name = models.CharField(max_length=100)
    create_time = models.DateTimeField()

    def __str__(self):
        return self.nav_name

class Context(models.Model):
    classify = models.ForeignKey(Navigation)
    title = models.CharField(max_length=200)
    shortcontext = models.TextField(max_length=500)
    context = UEditorField(width=800,height=200)
    #context = RichTextField(config_name='awesome_ckeditor')
    create_time = models.DateTimeField()
    hits = models.IntegerField(default=0)
    times = models.IntegerField(default=0)
    goods = models.IntegerField(default=0)
    bads = models.IntegerField(default=0)
    sessionid = models.TextField(max_length=32)


    def __str__(self):
        return self.title

class Author(models.CharField):
    pass

class Comment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    createtime = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Context)

    def __str__(self):
        return self.article