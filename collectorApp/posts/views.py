#views.py
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic
from django.http import Http404
from django.contrib import messages

from braces.views import SelectRelatedMixin


from . import models
from . import forms



from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post
    select_related = ("user","group")

class UserPosts(generic.ListView):
    model = models.Post
    template_name = "posts/user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context


class PostDetail(SelectRelatedMixin,generic.DetailView):
        model = models.Post
        select_related = ("user", "group")
        
        def get_queryset(self):
            queryset = super().get_queryset()
            return queryset.filter(user__username__iexact = self.kwargs.get("username"))
    
class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ("message", "group", "title", "description", "link", "tags")
    model = models.Post
    template_name = 'posts/post_form.html'

    print("test");
    return;
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.title = form.cleaned_data.get("title")
        self.object.description = form.cleaned_data.get("description")
        self.object.link = form.cleaned_data.get("link")
        
    # Split the tags string on commas and create a list of tag names
        tag_names = form.cleaned_data.get("tags").split(',')
        tags = []
        # Loop through the tag names and create or retrieve the Tag objects
        for tag_name in tag_names:
            tag = models.Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        # Set the tags for the post
        self.object.tags.set(tags)
    
        self.object.save()
        return super().form_valid(form)


    
class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
        model = models.Post
        select_related = ("user","group")
        success_url = reverse_lazy("posts:all")

        def get_queryset(self):
            queryset = super().get_queryset()
            return queryset.filter(user_id = self.request.user.id)

        def delete(self, *args, **kwargs):
            messages.success(self.request,"Post Deleted")
            return super().delete(*args, **kwargs)
            