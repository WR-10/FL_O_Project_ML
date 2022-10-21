from django.urls import path
from tweet import views

app_name = "tweet"

urlpatterns = [
    path('write/', views.write, name = 'write'),
    path('add/<int:id>', views.add, name = 'add'),
    path('post-detail/comment/<int:id>', views.write_comment, name='write_comment'),
    path('post-detail/comment/delete/<int:id>', views.delete_comment, name='delete_comment'),
    path('like/<int:id>', views.post_like, name='post_like'),
    path('community/<int:id>', views.add, name = 'add'),
    path('community/<int:id>/mod', views.mod),
    path('search_result/', views.search_result, name="search_result"),
    path('search_result/<int:id>', views.search_target_result),
    path('post-detail/<int:id>', views.post_detail),
]


