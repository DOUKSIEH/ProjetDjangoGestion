from django.forms import  ModelForm 
from .models import Commande





class CommandeForm(ModelForm):
    """Form definition for   
     MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model =   Commande
        
        fields = '__all__'
