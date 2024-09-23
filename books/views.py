from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def books_view(request):
    return HttpResponse("Hello, this is all about books!")
