from django.shortcuts import render, redirect
from .models import *

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        available_copies = request.POST['available_copies']
        Book.objects.create(title=title, author=author, isbn=isbn, available_copies=available_copies)
        return redirect('home')
    return render(request, 'add_book.html')
