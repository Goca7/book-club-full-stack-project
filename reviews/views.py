from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from books.models import Book


# View to handle adding and editing reviews
@login_required(login_url='login')
def add_review(request, slug):
    book = get_object_or_404(Book, slug=slug)

    # Check if the user has already reviewed the book
    existing_review = Review.objects.filter(
        book=book, user=request.user).first()

    if request.method == 'POST':
        # Handle editing an existing review
        if existing_review:
            form = ReviewForm(request.POST, instance=existing_review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Review updated successfully!')
            else:
                messages.error(
                    request, 'There was a problem updating your review.')
        # Handle adding a new review
        else:
            form = ReviewForm(request.POST)
            if form.is_valid():
                new_review = form.save(commit=False)
                new_review.book = book
                new_review.user = request.user
                new_review.save()
                messages.success(request, 'Review added successfully!')
            else:
                messages.error(
                    request, 'There was a problem submitting your review.')
        return redirect('book_details_view', slug=book.slug)
    return redirect('book_details_view', slug=book.slug)


# Delete a review (only the review owner or a superuser can delete)
@login_required(login_url='login')
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Check if the user is either the owner of the review or a superuser
    if request.user == review.user or request.user.is_superuser:
        review.delete()  # Delete the review if the condition is met
        messages.success(request, "Review deleted successfully.")
    else:
        # Show an error message if the user is neither the owner nor a superuser
        messages.error(
            request, "You do not have permission to delete this review.")

    # Redirect back to the book's detail page using the slug of the book
    return redirect('book_details_view', slug=review.book.slug)
