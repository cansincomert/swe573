from django.shortcuts import render
from groups.models import Group,GroupMember,User

# Create your views here.
def profile(request, pk):
    user = User.objects.get(id=int(pk))

    try:
        profile = User.objects.get(owner__id=int(pk))
    except:
        profile = User.objects.create(owner=user)
        profile.save()

    pk_var = str(profile.owner.pk)
