from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    course = forms.CharField(max_length=100, required=False)
    class Meta:
        model=User
        fields=['username','email','course','password1','password2']



class CertificateForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    course_name = forms.CharField(max_length=255)
