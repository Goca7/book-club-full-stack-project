from django.urls import path
from . import views

urlpatterns = [
    # URL for creating a new book (Create a new book)
    path('create/', views.create_book, name='create_book'),

    # URL for the book list (Read list of all books)
    path('', views.books_view, name='books_view'),

    # URL for updating an existing book (Update a book's details)
    path('<slug:slug>/update/', views.update_book, name='update_book'),

    # URL for deleting an existing book (Delete a book)
    path('<slug:slug>/delete/', views.delete_book, name='delete_book'),

    # URL for a single book (Read a single book's details)
    path('<slug:slug>/', views.book_details_view, name='book_details_view'),

    # URL for deleting a review
    path('review/delete/<int:review_id>/',
         views.delete_review, name='delete_review'),

]
