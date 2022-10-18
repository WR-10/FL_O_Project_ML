from django.db import models
from user.models import Users

class Article(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = 'files/covers', null = True)
    create_at = models.DateField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   
