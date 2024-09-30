from django.shortcuts import render, redirect
from .models import WishList
from books.models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


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


# Display the "Want-to-read" list of books for the current user
def wish_list_view(request):
    if request.user.is_authenticated:
        # Fetch all books from the WishList model associated with the current user
        user__books = WishList.objects.filter(user=request.user)
        context = {
            'user_books': user__books
        }
        # Render the template with the books in the wish list
        return render(request, 'wish_list/wish_list.html', context)
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('login')


# Remove a book from the "Want-to-read" list
def remove_from_wish_list(request, wish_list_id):
    if request.user.is_authenticated:
        # Fetch the specific WishList entry by its ID and ensure it belongs to the authenticated user
        wish_list_entry = WishList.objects.get(
            id=wish_list_id, user=request.user)
        # Delete the WishList entry (remove the book from the user's "Want-to-read" list)
        wish_list_entry.delete()
        # Redirect the user back to their Wish List page after successfully removing the book
        return redirect('wish_list')
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('login')


# Signup view to allow new users to register
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to the login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    # Render the signup page with the form
    return render(request, 'registration/signup.html', {'form': form})
