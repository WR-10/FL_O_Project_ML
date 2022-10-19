from django.urls import path
from tweet import views



urlpatterns = [
    path('write/', views.write, name = 'write'),
    path('community/', views.community, name = 'community'),
    path('community/<int:id>', views.add, name = 'add'),
    path('community/<int:id>/mod', views.mod)
]

