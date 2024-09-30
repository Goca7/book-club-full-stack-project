from django.shortcuts import render, redirect
from .models import WishList
from books.models import Book
from django.contrib.auth.models import User

# Create your views here.


# Create a new entry in the "Want-to-read" list
def add_to_wish_list(request, book_id):
    if request.user.is_authenticated:
        book = Book.objects.get(id=book_id)
        wish_list_entry, created = WishList.objects.get_or_create(
            user=request.user, book=book)
        if created:
            return redirect('wish_list')
        else:
            return redirect('book_detail', book_id=book_id)
    else:
        return redirect('login')


def wish_list_view(request):
    return HttpResponse("Hello, this is all about Wish List!")
