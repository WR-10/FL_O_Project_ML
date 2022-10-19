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
    
class TweetComment(models.Model):
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE)# 포스트 게시글 참조
    author = models.ForeignKey(Users, on_delete=models.CASCADE) # 작성자
    comment = models.TextField() #댓글 내용
    created_at = models.DateTimeField(auto_now_add=True) #작성 날짜
    updated_at = models.DateTimeField(auto_now=True)
    #업뎃 날짜


    # 게시글 작성시 DB에 title로 표시
    def __str__(self):
        return self.comment
