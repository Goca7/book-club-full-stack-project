from django.urls import path
from . import views  # Import views from the wish_list app
from .views import CustomLoginView

urlpatterns = [

    # Custom login view pointing to wish_list/login.html
    path('login/', CustomLoginView.as_view(), name='login'),

    # URL for the signup page
    path('signup/', views.signup_view, name='signup'),

    # URL for adding a book to the wish list
    path('add/<int:book_id>/', views.add_to_wish_list, name='add_to_wish_list'),

    # URL for removing a book from the wish list
    path('remove/<int:wish_list_id>/', views.remove_from_wish_list,
         name='remove_from_wish_list'),


    # URL for displaying the wish list
    path('', views.wish_list_view, name='wish_list_view'),

]
