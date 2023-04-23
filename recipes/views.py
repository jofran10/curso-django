from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'recipes/pages/home.html', context={'name': 'jofran'})

""" def sobre(request):
    return render(request, 'recipes/sobre.html')

def contato(request):
    return HttpResponse('CONTATO - RECIPES 2') """
