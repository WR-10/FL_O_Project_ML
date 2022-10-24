from django.shortcuts import render, redirect
from .models import Users
from tweet.models import Article
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def searchuser(request):
    if request.method == "POST":
        search = request.POST.get('searchuser')
        searchusers = Users.objects.filter(first_name=search)
        return render(request, 'searchuser.html', {'searchusers':searchusers})

@login_required
def user_view(request): # 유저 리스트 검색
    if request.method == 'GET':
       user_list = Users.objects.all().exclude(username = request.user.username)   
       return render(request, 'searchuser.html', {'user_list' : user_list})

@login_required
def user_follow(request, id): #유저 팔로우 기능
    me = request.user
    click_user = Users.objects.get(id = id)
    if me in click_user.followed.all():
        click_user.followed.remove(request.user)
    else:
        click_user.followed.add(request.user)
    return redirect('/user/profile/'+str(id))


def profile_modify(request):
    if request.method == "POST":
        user = request.user
        if request.POST.get('profile') =='':
            pass
        else:
            user.profile = request.POST.get('profile')
        if request.POST.get('first-name') == '':
            pass
        else:
            user.first_name = request.POST.get('first-name')
        try:
            user.image = request.FILES['image']
        except:
            pass
        user.save()

        return redirect('/')

def background_modify(request):
    if request.method == "POST":
        user = request.user
        user.background = request.FILES['background']
        try:
            user.image = request.FILES['image']
        except:
            pass
        user.save()

        return redirect('/')
    
def user_profile(request,id):
    if request.method == "GET":
        target_user = Users.objects.get(id=id)
        articles = Article.objects.filter(user=target_user)
        
        context = {
            'target_user':target_user,
            'articles' : articles
        }

        return render(request,'serve.html',context)

    