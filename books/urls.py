from django.urls import path  # Make sure this import is present
from . import views
from reviews import views as review_views  # Import views from the reviews app

urlpatterns = [
    path('create/', views.create_book, name='create_book'),  # Create a new book
    # List all books with pagination
    path('list/', views.books_view, name='books_view'),
    path('<int:book_id>/add-to-wish-list/', views.add_to_wish_list_from_list,
         name='add_to_wish_list_from_list'),  # Add to wish list
    path('<slug:slug>/update/', views.update_book,
         name='update_book'),  # Update a book
    path('<slug:slug>/delete/', views.delete_book,
         name='delete_book'),  # Delete a book
    path('detail/<slug:slug>/', views.book_details_view,
         name='book_details_view'),  # View book details
    # Delete a review from reviews app
    path('<slug:slug>/review/delete/<int:review_id>/',
         review_views.delete_review, name='delete_review'),
]
