from django.shortcuts import render, HttpResponse

def NAVBARTemplate():
    return HttpResponse(f'''
    
    ''')

def home(articleTag):
    return HttpResponse(NAVBARTemplate())