from django.shortcuts import render, get_object_or_404
from .models import Post #.; current dir
from django.utils import timezone

def post_list(request): # get request
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # instances of all published post with time-order
    return render(request, 'blog/post_list.html', {'posts': posts}) # show post_list html template when parameter='post'

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
