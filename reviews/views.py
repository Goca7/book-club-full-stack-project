from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from books.models import Book


# View to handle adding a new review
@login_required(login_url='login')
def add_review(request, slug):
    book = get_object_or_404(Book, slug=slug)

    if request.method == 'POST':
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


# View to handle editing an existing review
@login_required(login_url='login')
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    # Ensure only the review owner can edit
    if review.user != request.user:
        messages.error(
            request, 'You do not have permission to edit this review.')
        return redirect('book_details_view', slug=review.book.slug)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review updated successfully!')
        else:
            messages.error(
                request, 'There was a problem updating your review.')
        return redirect('book_details_view', slug=review.book.slug)
    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'review': review,
        'book': review.book,
    }

    return render(request, 'reviews/edit_review.html', context)


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
