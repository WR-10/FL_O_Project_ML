from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article

def write(request):
    # user = authenticate(request, username = username, password = password)
    # if user:
        
        if request.method == "GET":
            return render(request, 'write.html')
        elif request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            article = Article()
            article.image = request.FILES['image']
            
            Article.objects.create(title = title, content = content, image = article.image)
            
            
            return redirect('/tweet/community/')

def community(request):
    if request.method == 'GET':
        articles = Article.objects.all().order_by('-create_at')
        context = {
            'articles' : articles
        }
        
        return render(request, 'community.html', context)

        

def add(request, id):
    id_com = Article.objects.get(id = id) # get의 의미 db에 A필드에 B인걸 가지고 오겠따(where같은개념)  
    com = {
        'id_com' : id_com,
    }
    print(id_com.id) 
    return render(request, 'add.html', com) #render는 type는 반드시 딕셔너리만 가능하게끔 되어있다. 

def mod(request, id):
    if request.method == 'GET':
        id_sa = Article.objects.get(id = id)
        b = {
            'id_sa' : id_sa,
        }
        return render(request, 'mod.html', b)

    elif request.method == 'POST':
        id_sa = Article.objects.get(id = id)
        id_sa.title = request.POST.get('title')
        id_sa.content = request.POST.get('content')
        id_sa.save()
            
        return redirect('/tweet/community/')        
        
            


             



        
        
     