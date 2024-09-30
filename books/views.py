from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


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
