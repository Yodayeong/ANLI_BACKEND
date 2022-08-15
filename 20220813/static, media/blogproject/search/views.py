from django.shortcuts import render
from blog.models import Blog
from django.db.models import Q

def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        results = Blog.objects.all().filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
        )
    
    return render(request, 'search.html', {'query': query, 'results': results})