
from django import forms
from .models import Name

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['name']

    name = forms.CharField(widget=forms.TextInput(attrs={"id":"newStudentName"}))