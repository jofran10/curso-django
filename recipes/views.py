from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('HOME - RECIPES 2')

def sobre(request):
    return HttpResponse('SOBRE- RECIPES 2')

def contato(request):
    return HttpResponse('CONTATO - RECIPES 2')
