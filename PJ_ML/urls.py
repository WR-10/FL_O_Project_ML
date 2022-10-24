from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('tweet/', include('tweet.urls')),
    path('accounts/', include('allauth.urls')),
    path('',views.main),
    path('searchuser/', views.user_view, name = 'user-list'),
    path('user/follow/<int:id>', views.user_follow, name = 'user-follow'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

