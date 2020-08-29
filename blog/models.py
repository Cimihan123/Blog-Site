from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Skill(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media')

    def __str__(self):

        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):

        return self.name





class Post(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    description = RichTextField(max_length=200000)
    date = models.DateTimeField(auto_now=True , blank=True)
    img = models.ImageField(upload_to='media')

    def __str__(self):

        return self.title



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=20)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True , blank=True)

    def __str__(self):

        return self.name

