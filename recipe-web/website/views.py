from django.shortcuts import render
from core.models import Book

# Create your views here.
def index(request):
    return render(
        request,
        'website/index.html',
    )

def recipes(request):
    # context = {
    #     'books': books,
    # }
    return render(
        request,
        'website/recipes.html',
        # context,
    )
