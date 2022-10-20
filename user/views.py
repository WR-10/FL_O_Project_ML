from django.shortcuts import render, redirect
from .models import Users
from django.contrib import auth


    
def searchname(request, profile):
    if request.method == "GET":
        search_name = Users.objects.filter(profile=profile)
    return render(request, 'search.html', {'search_name':search_name})

def profile_modify(request):
    if request.method == "POST":
        print("profile_modify")
        user = request.user
        user.profile = request.POST.get('profile')
        try:
            user.image = request.FILES['image']
        except:
            pass
        user.save()

        return redirect('/')
