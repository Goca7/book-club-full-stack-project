from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def wish_list_view(request):
    return HttpResponse("Hello, this is all about Wish List!")
