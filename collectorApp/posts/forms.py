#forms.py
from django import forms

from groups.models import Group, User
from posts.models import Post

from django.views.generic import CreateView

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'message', 'group', 'user', 'link', 'tags', 'description']
    template_name = 'posts/post_form.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tags'].widget = forms.CharField(widget=forms.TextInput)
