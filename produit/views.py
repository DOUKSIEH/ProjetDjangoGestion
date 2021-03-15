from django.shortcuts import render
from commande.models import Commande
from client.models import Client

from django.template.defaulttags import register


# def get_item(dictionary, key):
#     return dictionary.get(key)

# register.filter('get_item', get_item)   
# # Create your views here.
# @register.filter(name='get_item')
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'cmds':commandes,'clients':clients}
    return render(request,'produit/accueil.html',context=context)