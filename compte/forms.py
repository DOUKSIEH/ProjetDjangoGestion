from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUSer(UserCreationForm):
    """Form definition for   
     MODELNAME."""

    # email = forms.EmailField()

    class Meta:
        """Meta definition for MODELNAMEform."""

        model =  User
        
        fields = ['username','email','password1','password2']
