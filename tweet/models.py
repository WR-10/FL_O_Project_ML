from django.db import models
from user.models import Users
import os
from uuid import uuid4
from django.utils import timezone

class Article(models.Model):
    def date_upload_to(instance, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower() 
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    title = models.CharField(max_length = 100)
    content = models.TextField()
    image = models.ImageField(upload_to = date_upload_to, null = True)
    create_at = models.DateField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
   
