from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_book, name='create_book'),
    path('list/', views.books_view, name='books_view'),  # Book listing page
    path('<int:book_id>/add-to-wish-list/', views.add_to_wish_list_from_list,
         name='add_to_wish_list_from_list'),  # Add to wish list
    path('<slug:slug>/update/', views.update_book, name='update_book'),
    path('<slug:slug>/delete/', views.delete_book, name='delete_book'),
    path('detail/<slug:slug>/', views.book_details_view, name='book_details_view'),
    path('<slug:slug>/review/delete/<int:review_id>/',
         views.delete_review, name='delete_review'),
]
