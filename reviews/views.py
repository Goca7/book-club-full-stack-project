from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
ef reviews_view(request):
    # Example logic for displaying reviews
    return render(request, 'reviews/reviews_list.html', {})
