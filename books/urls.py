from django.urls import path
from . import views

urlpatterns = [
    # URL for the book list
    path('', views.books_view, name='books_view'),
    # URL for a single book
    path('<slug:slug>/', views.book_details_view, name='book_details_view'),
]
