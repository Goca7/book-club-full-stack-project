urlpatterns = [
    path('create/', views.create_book, name='create_book'),  # Create a new book
    # Book listing page with pagination
    path('list/', views.books_view, name='books_view'),  # List all books
    # Add to wish list (from the book listing page)
    path('<int:book_id>/add-to-wish-list/',
         views.add_to_wish_list_from_list, name='add_to_wish_list_from_list'),
    path('<slug:slug>/update/', views.update_book,
         name='update_book'),  # Update a book
    path('<slug:slug>/delete/', views.delete_book,
         name='delete_book'),  # Delete a book
    path('detail/<slug:slug>/', views.book_details_view,
         name='book_details_view'),  # View book details
    path('<slug:slug>/review/delete/<int:review_id>/',
         views.delete_review, name='delete_review'),  # Delete a review
]
