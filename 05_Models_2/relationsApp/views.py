# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse('model 2 dersine hoşgeldiniz')