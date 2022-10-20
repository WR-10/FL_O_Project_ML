from django.http import HttpResponse
from django.shortcuts import render, redirect
from tweet.models import Article
from django.contrib.auth import authenticate
from user.models import Users
from django.contrib.auth.decorators import login_required



def main(request):
    user = request.user.is_authenticated
    if user:
        if request.method == "GET":
            a = request.user.id
            articles = Article.objects.filter(user_id = a).order_by('-updated_at')
            context = {
                    'articles' : articles
                }
            print(context)
            
            return render(request,'main.html', context)
    else: 
        return redirect('/accounts/login/')


@login_required
def user_view(request):
    if request.method == 'GET':
       user_list = Users.objects.all().exclude(username = request.user.username)  
       print(user_list)  
       return render(request, 'searchuser.html', {'user_list' : user_list})

@login_required
def user_follow(request, id):
    me = request.user
    click_user = Users.objects.get(id = id)
    if me in click_user.followed.all():
        click_user.followed.remove(request.user)
    else:
        click_user.followed.add(request.user)
    return redirect('/user/profile/'+str(id))     #127.0.0.1/8000/user/profile/2


