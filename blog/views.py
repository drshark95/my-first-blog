from django.shortcuts import render

def post_list(request): # get request
    return render(request, 'blog/post_list.html', {}) # show post_list html template
