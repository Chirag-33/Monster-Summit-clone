from django import forms
from .models import Profile,Comment,Speaker

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'profile_picture']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        exclude = ['slug']