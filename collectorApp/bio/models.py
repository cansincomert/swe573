from django.db import models
from groups.models import Group,GroupMember,User

# Create your models here.
class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(
        default='', null=True, blank=True)

    def __str__(self):
        return self.owner.username

