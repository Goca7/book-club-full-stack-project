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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('admin/', admin.site.urls),  # Admin URLs
    path('books/', include('books.urls')),  # Book-related URLs
    path('reviews/', include('reviews.urls')),  # Reviews URLs
    path('wish-list/', include('wish_list.urls')),  # Wish List URLs
    path("", TemplateView.as_view(template_name="books/index.html"),
         name="home"),  # Home page URL
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
