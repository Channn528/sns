from django.db import models

# Create your models here.
from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="img/", blank = True)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes')    
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    objects = models.Manager()
    content = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name='comments')
    # Post의 Comment, Comment의 Post를 서로 추적 가능
    
    created_at = models.DateTimeField(auto_now_add=True)
        
        