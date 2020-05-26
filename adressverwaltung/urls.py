from django.urls import path
from . import views

urlpatterns = [
    path('',  views.post_list,  name='post_list'), 
    path('person/<int:pk>/',  views.post_detail,  name='post_detail'), 
    path('person/new/',  views.post_new,  name='post_new'), 
    path('person/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
