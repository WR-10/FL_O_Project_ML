from django.urls import path
from tweet import views


urlpatterns = [
    path('write/', views.write, name = 'write'),
    path('community/', views.community, name = 'community'),
    path('comment/<int:id>', views.write_comment, name='write-comment'),
    path('comment/delete/<int:id>', views.delete_comment, name='delete_comment'),
    path('detail/<int:id>/', views.post_detail),
    path('like/<int:id>', views.post_like, name='post_like'),
]