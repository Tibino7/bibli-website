# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book

def index(request):
    books_list = Book.objects.order_by('author_last_name')
    context = {'books_list': books_list}
    return render(request, 'app/index.html', context)

