from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("user.urls")),
    path('tweet/', include('tweet.urls')),
    path('',views.main),
    path('accounts/', include('allauth.urls')),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

