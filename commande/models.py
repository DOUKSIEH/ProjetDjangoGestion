from django.db import models
from client.models import Client
from produit.models import Produit
from datetime import datetime

# Create your models here.
class Commande(models.Model):
    STATUS=(('ATTENTE','EN ATTENTE'),('NONLIVREE','EN COURS DE LIVRAISON'),('LIVRE','LIVRÉ'))
    client = models.ForeignKey(Client,null=True,on_delete=models.SET_NULL,default=1)
    produits = models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL,default=1)
    status = models.CharField(max_length=200,null=True,choices=STATUS,default=1)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        if self.status == 'ATTENTE':
            print('------EN ATTENTE------: ' + self.status)
            return 'La commande est en attente de validation'

        elif self.status == 'NONLIVREE':
            print('------nonlivré------: ' + self.status)
            return 'La commande est en cours de livraison'

        else :
            print('------livré------: '+ self.status)
            return 'La commande a été livrée (le {}) '.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        
    
