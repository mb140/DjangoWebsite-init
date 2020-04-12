from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def homev0(request):
    return HttpResponse('<h1>this is homepage v0</h1>')

def homev1(request):
    return render(request, 'generator/home_v1.html')

def homev2(request):
    return render(request, 'generator/home_v2.html',{'keyValue':'myAnyVaue_v2'})

def homev4(request):
    return render(request, 'generator/home_v4_genPas.html')

def respas(request):
    len = int(request.GET.get('length',default= 6))
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+/'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    paswd = ''
    for x in range(len):
        paswd += random.choice(characters)
        # paswd.append(random.choice(characters))
    return render(request, 'generator/resultPage.html',{'keyValue':paswd})

def aboutpage(request):
    return render(request, 'generator/aboutpage.html')