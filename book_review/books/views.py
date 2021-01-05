from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books':books})
