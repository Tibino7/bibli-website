from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def table(request):
    return render(request, 'books/table.html')

def index(request):
    return HttpResponse("Hello, world. You're at the books index.")
