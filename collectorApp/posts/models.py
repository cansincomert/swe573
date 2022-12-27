#models.py
from django.db import models
from django.urls import reverse
from django.conf import settings


import misaka

from groups.models import Group,GroupMember

from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, related_name= "posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True)
    link = models.URLField(default="http://example.com",null=True)
    #tags = models.ManyToManyField(Tag, related_name='posts')
    description = models.TextField(default="Enter a description here", null=False)
    
    
    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"username": self.user.username,"pk":self.pk})

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user","message"]
    
        

