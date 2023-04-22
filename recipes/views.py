from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/home.html')   ## usando namespaces

def sobre(request):
    return HttpResponse('SOBRE- RECIPES 2')

def contato(request):
    return HttpResponse('CONTATO - RECIPES 2')
