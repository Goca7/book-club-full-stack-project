from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


# View to display a list of all books
def books_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    # Render the template with the books
    return render(request, 'books/book_list.html', {'books: books})'})


# View to display a single book using its slug
def book_details_view(request, slug):
    # Fetch the book from the database using its slug
    book = Book.objects.get(slug=slug)
    # Render the template with the book details
    return render(request, 'books/book_detail.html', {book: book})


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
    book = Book.objects.get(slug=slug)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # Redirect to updated book details
            return redirect('book_details_view', slug=book.slug)
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})

# View to delete a book


def delete_book(request, slug):
    book = Book.objects.get(slug=slug)
    if request.method == 'POST':
        book.delete()  # Delete the book from the database
        return redirect('books_view')  # Redirect to the book list page
    return render(request, 'books/delete_book.html', {'book': book})
