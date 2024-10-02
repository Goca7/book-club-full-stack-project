from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import WishList
from books.models import Book


# Custom Login view that redirects based on user role
class CustomLoginView(LoginView):
    template_name = 'wish_list/login.html'

    def form_valid(self, form):
        user = form.get_user()
        # If the user is an admin, redirect them to the admin panel
        if user.is_superuser:
            return redirect('/admin/')
        # Otherwise, redirect them to their Want-to-read list
        else:
            return redirect('wish_list_view')


# Create a new entry in the "Want-to-read" list
# Redirect to login if the user is not authenticated
@login_required(login_url='login')
def add_to_wish_list(request, book_id):
    # Fetch the book or return a 404 if it doesn't exist
    book = get_object_or_404(Book, id=book_id)
    wish_list_entry, created = WishList.objects.get_or_create(
        user=request.user, book=book)
    if created:
        # Redirect to the Wish List page after successfully adding the book to the Wish List
        return redirect('wish_list_view')
    else:
        # Redirect to the book details page if the book is already in the Wish List
        return redirect('book_details_view', slug=book.slug)


# Display the "Want-to-read" list of books for the current user
# Redirect to login if the user is not authenticated
@login_required(login_url='login')
def wish_list_view(request):
    # Fetch the books in the user's "Want-to-read" list
    user_books = WishList.objects.filter(user=request.user)
    context = {
        'user_books': user_books
    }
    # Render the template with the books in the wish list
    return render(request, 'wish_list/wish_list.html', context)


# Delete a book from the "Want-to-read" list
# Redirect to login if the user is not authenticated
@login_required(login_url='login')
def remove_from_wish_list(request, wish_list_id):
    wish_list_entry = get_object_or_404(
        WishList, id=wish_list_id, user=request.user)
    # Delete the WishList entry (remove the book from the user's "Want-to-read" list)
    wish_list_entry.delete()
    # Redirect the user back to their Wish List page after successfully removing the book
    return redirect('wish_list_view')


# Signup view to allow new users to register
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            # Redirect to the login page after successful signup
            return redirect('login')
    else:
        form = UserCreationForm()
    # Render the signup page with the form
    return render(request, 'wish_list/signup.html', {'form': form})


# Custom Login view that uses a template in the wish_list directory
class CustomLoginView(LoginView):
    template_name = 'wish_list/login.html'
