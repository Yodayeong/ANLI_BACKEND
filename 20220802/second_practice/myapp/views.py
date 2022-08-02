from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello!')

def create(request):
    return HttpResponse('Dayeong!')

def write(request, id):
    return HttpResponse('Smile!' + ' ' + id)