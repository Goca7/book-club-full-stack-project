from django.urls import path
from . import views  # Import views from the wish_list app

urlpatterns = [
    # URL for the wish list page
    path('', views.wish_list_view, name='wish_list_view'),

]
