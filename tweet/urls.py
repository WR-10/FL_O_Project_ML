from django.urls import path
from tweet import views



urlpatterns = [
    path('write/', views.write, name = 'write'),
    path('community/', views.community, name = 'community'),
    path('add/<int:id>', views.add, name = 'add')
]

