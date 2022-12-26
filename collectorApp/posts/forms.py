''' from django.forms import ModelForm
from django.forms import CharField
from .models import Content, Profile

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(ModelForm):
    
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']

class ContentForm(ModelForm):
    tag = CharField(required=False,
                    help_text='<br/>You can enter multiple tags by separating them with commas(,).')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in ['header', 'link', 'description', 'visibility']:
            self.fields[field_name].help_text = None

        self.fields['link'].required = False

    class Meta:
        model = Content
        fields = ['header', 'tag', 'link', 'description', 'visibility']
        
 '''