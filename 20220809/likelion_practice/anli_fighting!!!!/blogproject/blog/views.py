from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, id):
    #detail page는 id에 맞는 것들을 들고옴.
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})