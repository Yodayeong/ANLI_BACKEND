from django.shortcuts import render, HttpResponse
import random

# Create your views here.

def home(request):
    return HttpResponse('RANDOM' + str(random.random()))

def create(request):
    return HttpResponse('CREATE')

def read(request, id):
    return HttpResponse('READ' + str(id))