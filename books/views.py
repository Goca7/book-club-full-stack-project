from django.shortcuts import render, get_object_or_404
from .models import Book


# View to display a list of all books
def books_view(request):
    books = Book.objects.all()  # Fetch all books from the database
    context = {'books': books}  # Pass the books to the template
    # Render the template with the books
    return render(request, 'books/book_list.html', context)


# View to display a single book using its slug
def book_details_view(request, slug):
    # Fetch the book from the database using its slug
    book = get_object_or_404(Book, slug=slug)
    context = {'book': book}  # Pass the book to the template
    # Render the template with the book details
    return render(request, 'books/book_detail.html', context)
