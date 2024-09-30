from django.urls import path
from . import views  # Import views from the reviews app

urlpatterns = [
    # List all reviews
    path('', views.reviews_view, name='reviews_view'),
]
