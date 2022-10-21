from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from uuid import uuid4
class Users(AbstractUser):
    def date_upload_to(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        img_path = 'profile/'
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower() 
        # 결합 후 return
        return '/'.join([
            img_path,
            uuid_name + extension,
        ])
    
    def date_upload_to_bg(instance, filename):
    # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        img_path = 'background/'
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower() 
        # 결합 후 return
        return '/'.join([
            img_path,
            uuid_name + extension,
        ])

    image = models.ImageField(upload_to = date_upload_to, null = True, default = 'profile/default_profile.png')
    background = models.ImageField(upload_to = date_upload_to_bg, null = True, default = 'background/big-sur-4k-wp.jpg')
    profile = models.TextField(max_length=500, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'followed')
