"""
URL configuration for book_club project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # Django admin site URL
    path('admin/', admin.site.urls),
    # Delegate URLs starting with 'books/' to the books app
    path('books/', include('books.urls')),
    # Delegate URLs starting with 'reviews/' to the reviews app
    # path('reviews/', include('reviews.urls')),
    # Delegate URLs starting with 'wish-list/' to the wish_list app
    path('wish-list/', include('wish_list.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home_page'),
    # Add more paths as needed...
]
