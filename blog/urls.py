from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
] # view 'post_list' assigined at url ''(write nothing)
