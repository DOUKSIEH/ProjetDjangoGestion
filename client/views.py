from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Client
from commande.models import Commande
from commande.filters import CommandeFiltre


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ClientListView(ListView):

    model = Client
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        # context['now'] = timezone.now()
        return context


class ClientDetailView(DetailView):

    model = Client
    # paginate_by = 100  # if pagination is desired
    # queryset = Client.objects.all()
    # def get_object(self):
    #     id_ = self.kwargs.get("id")
    #     print(self.queryset)
    #     context['cmds'] = Commande.objects.all()
    #     # return context
    #     return get_object_or_404(Client,id=id_)
    def get_context_data(self, **kwargs):
        id_ = self.kwargs.get("pk")
        print(id_)
        client = Client.objects.get(id=id_)
        
        context = super().get_context_data(**kwargs)
        # print(context)
        obj = self.get_object()
        print(obj)

        # product_set = obj.product_set.all()

        context['cmds'] = obj.commande_set.all()
        
        print(context)
        return context 
        # get_object_or_404(Client,context=context)
# Create your views here.
# def list_client(request,id):
#     client = Client.objects.get(id=id)
#     commande = client.commande_set.all()
#     myfilters = CommandeFiltre(request.GET,queryset=commande)
#     commande = myfilters.qs 
#     print(myfilters.qs)
#     context = {'client': client, 'cmds':commande,"myfilters":myfilters}
#     return render(request,'client/liste.html',context=context)