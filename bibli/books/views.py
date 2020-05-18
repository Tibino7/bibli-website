from django.shortcuts import render

from .models import Book

def table(request):
    books_list = Book.objects.order_by('genre')
    context = {
        'books_list': books_list,
    }
    return render(request, 'books/table.html', context)

