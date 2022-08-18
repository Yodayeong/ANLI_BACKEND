from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()
    new_blog.location=request.POST['location']
    new_blog.writer=request.POST['writer']
    new_blog.pub_date=timezone.now()
    new_blog.image=request.FILES['image']
    new_blog.room_type=request.POST['room_type']
    new_blog.duration=request.POST['duration']
    new_blog.price=request.POST['price']
    new_blog.body=request.POST['body']
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.location=request.POST['location']
    update_blog.writer=request.POST['writer']
    update_blog.pub_date=timezone.now()
    update_blog.room_type=request.POST['room_type']
    update_blog.duration=request.POST['duration']
    update_blog.price=request.POST['price']
    update_blog.body=request.POST['body']
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')