from django.shortcuts import render
from .models import Post #.; current dir
from django.utils import timezone

def post_list(request): # get request
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # instances of all published post with time-order
    return render(request, 'blog/post_list.html', {'posts': posts}) # show post_list html template when parameter='post'
