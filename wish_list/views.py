from django.shortcuts import render, redirect
from .models import WishList
from books.models import Book
# Use the simple built-in UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create a new entry in the "Want-to-read" list


def add_to_wish_list(request, book_id):
    if request.user.is_authenticated:
        # Fetch the book with the given ID and create a new entry in the WishList model
        book = Book.objects.get(id=book_id)
        wish_list_entry, created = WishList.objects.get_or_create(
            user=request.user, book=book)
        if created:
            # Redirect to the Wish List page after successfully adding the book to the Wish List
            return redirect('wish_list')
        else:
            # Redirect to the book details page if the book is already in the Wish List
            return redirect('book_details_view', slug=book.slug)
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('login')
