from django.db import models
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.TextField()
    description = models.TextField()
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug for the book based on its title.
        if not self.slug:
            self.slug = slugify(self.title)
        # Call the real save() method to save to the database.
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
