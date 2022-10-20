from django.shortcuts import render, redirect
from .models import Users
from django.contrib import auth


    
def searchuser(request):
    if request.method == "POST":
        search = request.POST.get('searchuser') # 검색어를 serach에 넣은것 # html의 name 동근아!!! 너 미쳤니?? 뒤질 준비해라...
        searchusers = Users.objects.filter(username=search)
        print(search)
        print(searchusers)
        return render(request, 'searchuser.html', {'searchusers':searchusers}) # .은 확실할 때만 쓰고 남용하지 마라 동근아 제발 . 생활화 하지말자 동근아 한 번 더 기억하자 동근아
    
    