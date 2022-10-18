from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Article
from machine_learning import machine_learning

def write(request):
    # user = authenticate(request, username = username, password = password)
    # if user:
        
        if request.method == "GET":
            return render(request, 'write.html', {'article' : '안녕하세요'})
        elif request.method == "POST":
            article = Article()
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.image = request.FILES['image']
            
            article.save()
            
            #* 이 포스팅의 이미지로 Yolov5 돌려서 결과(tag) 출력

            # tag = machine_learning.ml_yolov5(article.image)

            # tag model(db) 저장

            # article.tag 저장
            

            # Article.objects.create(title = title, content = content, image = article.image)


def community(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-create_at')
        context = {
            'articles' : articles
        }
        # print(articles[0].image)
        
        return render(request, 'community.html', context)

def add(request, id):
    pass
            


             



        
        
     