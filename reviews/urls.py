from django.urls import path
from . import views  # Import views from the reviews app

urlpatterns = [
    path('', views.show_reviews, name='reviews_view'),
]
