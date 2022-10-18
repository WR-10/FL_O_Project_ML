from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

def write(request):
    # user = authenticate(request, username = username, password = password)
    # if user:
        
        if request.method == "GET":

            return render(request, 'write.html', {'article' : '안녕하세요'})
        elif request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            Article.objects.create(title = title, content = content)
            
            return redirect('/tweet/community/')

def community(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        context = {
            'articles' : articles
        }
        return render(request, 'community.html', context)


             



        
        
     