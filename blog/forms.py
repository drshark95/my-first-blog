from django import forms

from .models import Post

class PostForm(forms.ModelForm): # make form 'ModelForm'

    class Meta: # which model
        model = Post
        fields = ('title', 'text',)
