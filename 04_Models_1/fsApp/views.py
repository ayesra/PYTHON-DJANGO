from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def fswelcome(request):
    return HttpResponse('FS sayfasına hoşgeldiniz')
