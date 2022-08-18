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
    new_blog.image=request.FILES['image']
    new_blog.title=request.POST['title']
    new_blog.price=request.POST['price']
    new_blog.select_home=request.POST['select_home']
    new_blog.location=request.POST['location']
    new_blog.smaller_period=request.POST['smaller_period']
    new_blog.startDay=request.POST['startDay']
    new_blog.lastDay=request.POST['lastDay']
    new_blog.floor_space=request.POST['floor_space']
    new_blog.bathroom=request.POST['bathroom']
    new_blog.room=request.POST['room']
    new_blog.bed=request.POST['bed']
    new_blog.bed=request.POST['basic_info']
    new_blog.option=request.POST['option']
    new_blog.description=request.POST['description']
    new_blog.registered_dttm=timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog': edit_blog})

def update(request, id):
    update_blog = Blog()
    update_blog.images=request.FILES['images']
    update_blog.title=request.POST['title']
    update_blog.price=request.POST['price']
    update_blog.select_home=request.POST.get('select_option', False)
    update_blog.location=request.POST['location']
    update_blog.smaller_period=request.POST['smaller_period']
    update_blog.startDay=request.POST['startDay']
    update_blog.lastDay=request.POST['lastDay']
    update_blog.floor_space=request.POST['floor_space']
    update_blog.bathroom=request.POST['bathroom']
    update_blog.room=request.POST['room']
    update_blog.bed=request.POST['bed']
    update_blog.bed=request.POST['basic_info']
    update_blog.option=request.POST['option']
    update_blog.description=request.POST['description']
    update_blog.registered_dttm=timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')