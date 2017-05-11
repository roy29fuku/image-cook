from django.shortcuts import render
from core.models import Book

# Create your views here.
def index(request):
    return render(
        request,
        'website/index.html',
    )

def books(request):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(
        request,
        'website/books.html',
        context,
    )