from django.shortcuts import render, redirect
from .models import Users
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def signup(request):
    if request.method == "GET":
        return render(request, '/signup.html')
    elif request.method == "POST":
        username =  request.POST.get('username')
        profile = request.POST.get('profile')
        password =  request.POST.get('password')
        passwordcheck =  request.POST.get('passwordcheck')

        if password == passwordcheck:
            Users.objects.create_user(username=username, password=password, profile=profile)
            return redirect('/user/signin')

    else:
        return redirect('/user/signup')


def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username, password)
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)

            print("to home")
            return redirect('/user/home')
        else:
            return redirect('/user/signin')


@login_required
def home(request): 
    if request.method == "GET":
        return render(request,'home.html')

@login_required
def logout(request):
        auth.logout(request)
        return redirect("/user/signin")
    
def searchname(request, profile):
    if request.method == "GET":
        print("searchnameget들옴")
        search_name = Users.objects.filter(profile=profile)

    return render(request, 'search.html', {'search_name':search_name})

