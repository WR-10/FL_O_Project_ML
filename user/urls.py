from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('searchuser/', views.searchuser, name="searchuser"),
    path('profile/modify/',views.profile_modify),
    path('background/modify/',views.background_modify),
    path('profile/<int:id>' ,views.user_profile),
    path('follow/<int:id>', views.user_follow, name = 'user-follow'),
]
