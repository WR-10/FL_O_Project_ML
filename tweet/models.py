from tkinter import CASCADE
from django.db import models
from user.models import Users
import os
from uuid import uuid4
from django.utils import timezone

class Article(models.Model):
    def date_upload_to(instance, filename):
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        uuid_name = uuid4().hex
        extension = os.path.splitext(filename)[-1].lower() 
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    title = models.CharField(max_length = 100, null = True)
    content = models.TextField(null = True)
    image = models.ImageField(upload_to = date_upload_to, null = True)
    create_at = models.DateField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(Users, on_delete = models.CASCADE, null = True) 
    taghash = models.ManyToManyField('Tag', related_name = "tagged")
    
class TweetComment(models.Model):
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

class Tag(models.Model):
    tagname = models.CharField(max_length=20)