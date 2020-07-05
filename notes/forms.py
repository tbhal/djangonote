from django import forms
from django.contrib.auth.models import User
from notes.models import Note, Tag

## forms are the way we give our website the information it needs to write things to our database, so we want to make sure the info we're feeding it is sanitized and formatted properly.

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('label', 'body', 'tags')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('label',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']