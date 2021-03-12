from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_client(req):
    return HttpResponse("<h1>Liste des cients</h1>")