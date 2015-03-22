from django import forms
from django.contrib.auth.models import User
from note.models import Note, Rating, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('title','file')