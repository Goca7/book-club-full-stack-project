from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.TextField()
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    cover_image = models.ImageField(
        upload_to='book_covers/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Automatically generate slug if not provided
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
