

from chat.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'attachment']