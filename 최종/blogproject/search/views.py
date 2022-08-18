from django.shortcuts import render
from blog.models import Blog
from django.db.models import Q

def searchResult(request):
    if 'place' in request.GET:
        query_1 = request.GET.get('place')
    if 'type' in request.GET:
        query_2 = request.GET.get('type')

        results = Blog.objects.filter(
            Q(location__icontains=query_1) &
            Q(select_home__icontains=query_2)
        )
    
    return render(request, 'search.html', {'query_1': query_1, 'query_2': query_2, 'results': results})