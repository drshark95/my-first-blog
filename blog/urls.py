from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #  view 'post_list' assigined at url ''(write nothing)
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # view 'post_detail' assigned at url include post, integer for post_number, '/'
]
