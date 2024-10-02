from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.core.paginator import Paginator


# View to display a list of all books with pagination
def books_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    paginator = Paginator(books, 3)  # Set the number of books per page to 3
    # Get the page number from query string, default to 1
    page_number = request.GET.get('page', 1)
    # Get the correct page of books
    page_books = paginator.get_page(page_number)
    return render(request, 'books/book_list.html', {'page_books': page_books})


# View to allow a logged-in user to add a book to their "Want-to-read" list from the book listing page
@login_required(login_url='login')
def add_to_wish_list_from_list(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    wish_list_entry, created = WishList.objects.get_or_create(
        user=request.user, book=book)

    if created:
        # Message indicating the book was successfully added to the wish list
        messages.success(
            request, f'{book.title} was added to your Want-to-read list.')
        # Redirect to the same book list page after adding the book to the list
        return redirect('books_view')
    else:
        # Message indicating the book was already in the wish list
        messages.info(
            request, f'{book.title} is already in your Want-to-read list.')
        # Redirect back to the same book list page
        return redirect('books_view')


# View to display a single book using its slug and handle reviews
def book_details_view(request, slug):
    # Fetch the book from the database using its slug
    book = get_object_or_404(Book, slug=slug)
    # Fetch all reviews for the book
    reviews = Review.objects.filter(book=book)

    # Handle review form submission
    if 'add_review' in request.POST:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book  # Associate the review with the book
            new_review.user = request.user  # Associate the review with the logged-in user
            new_review.save()
            messages.success(request, 'Review added successfully!')
            return redirect('book_details_view', slug=book.slug)

    # Handle review update
    elif 'edit_review' in request.POST:
        review_id = request.POST.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, 'Review updated successfully!')
            return redirect('book_details_view', slug=book.slug)
    else:
        review_form = ReviewForm()  # Create an empty form for new reviews

    context = {
        'book': book,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'books/book_detail.html', context)


# Delete a review (only the review owner or a superuser can delete)
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Check if the user is either the review owner or a superuser
    if request.user == review.user or request.user.is_superuser:
        review.delete()
        messages.success(request, "Review deleted successfully.")
    else:
        messages.error(
            request, "You do not have permission to delete this review.")

    # Redirect back to the book's detail page with the slug
    return redirect('book_details_view', slug=review.book.slug)


# View to create a new book
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('books_view')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})


# View to update an existing book
def update_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_details_view', slug=book.slug)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})


# View to delete a book
def delete_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        messages.success(request, 'Book deleted successfully!')
        return redirect('books_view')
    return render(request, 'books/delete_book.html', {'book': book})
