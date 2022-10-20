from django.urls import path, include
from user import views

app_name = "user"

urlpatterns = [
    path('searchname/<str:profile>/', views.searchname, name="searchname"),
]
