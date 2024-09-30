from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from reviews.models import Review
from reviews.forms import ReviewForm


# View to display a list of all books
def books_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    # Render the template with the books
    return render(request, 'books/book_list.html', {'books': books})


# View to display a single book using its slug and handle reviews
def book_details_view(request, slug):
    # Fetch the book from the database using its slug
    book = get_object_or_404(Book, slug=slug)

    # Fetch all reviews for the book from the database
    reviews = Review.objects.filter(book=book)

    # Handle review form submission
    if request.method == 'POST':
        reviews_form = ReviewForm(request.POST)
        if reviews_form.is_valid():
            # Save the review to the database
            new_review = reviews_form.save(commit=False)
            new_review.book = book  # Associate the review with the book
            new_review.user = request.user  # Associate the review with the logged-in user
            new_review.save()
            return redirect('book_details_view', slug=book.slug)
    else:
        # Create a blank review form
        reviews_form = ReviewForm()

    # Render the template with the book details and reviews
    context = {
        'book': book,
        'reviews': reviews,
        'reviews_form': reviews_form,  # Form for adding new reviews to the book
    }
    return render(request, 'books/book_detail.html', context)


# View to create a new book
def create_book(request):
    if request.method == 'POST':
        # Create a form object using the POST data
        form = BookForm(request.POST)
        # If the form is valid, save the book to the database
        if form.is_valid():
            form.save()
            # Redirect to the book list page after successfully creating a new book
            return redirect('books_view')
    else:
        # Create a blank form object
        form = BookForm()
    # Render the template with the form for creating a new book
    return render(request, 'books/create_book.html', {'form': form})


# View to update an existing book
def update_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # Redirect to updated book details
            return redirect('book_details_view', slug=book.slug)
    else:
        # Populate the form with the existing book data
        form = BookForm(instance=book)
    # Render the template with the form for updating the book details
    return render(request, 'books/update_book.html', {'form': form})


# View to delete a book
def delete_book(request, slug):
    # Fetch the book from the database using its slug
    book = get_object_or_404(Book, slug=slug)
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        return redirect('books_view')  # Redirect to the book list page
    # Render the template with the book details for confirmation before deletion
    return render(request, 'books/delete_book.html', {'book': book})
