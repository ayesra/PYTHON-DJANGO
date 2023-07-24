from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dswelcome(request):
    return HttpResponse('ds sayfasına hoş geldiniz')