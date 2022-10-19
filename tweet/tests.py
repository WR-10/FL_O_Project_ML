from django.shortcuts import render 
from .models import Article


# Create your tests here.
def write(request):
    # user = authenticate(request, username = username, password = password)
    # if user:
        
        if request.method == "GET":
            return render(request, 'write.html')
        elif request.method == "POST":
            article = Article()
            article.title = request.POST.get('title')
            article.content = request.POST.get('content')
            article.image = request.FILES['image']
            article.save()
            
            
            print(article.image)
