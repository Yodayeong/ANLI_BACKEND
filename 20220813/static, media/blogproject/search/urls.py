from django.urls import path
from . import views

urlpatterns = [
    path('searchResult/', views.searchResult, name="searchResult")
]