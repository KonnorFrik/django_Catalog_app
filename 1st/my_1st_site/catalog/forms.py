from django import forms
from .models import AnyFile


class RegistrationLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150)
    password = forms.CharField(label="Password", max_length=150, widget=forms.PasswordInput)


class AnyFileForm(forms.ModelForm):
    class Meta:
        model = AnyFile
        fields = ['title', 'file']


class UserNoteForm(forms.Form):
    note_title = forms.CharField(label='Title For Note', max_length=100)
    note_description = forms.CharField(label="Description for note", max_length=300, widget=forms.Textarea)

    file_form = AnyFileForm()
