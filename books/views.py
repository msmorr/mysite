from django.shortcuts import render
from django.http import HttpResponse
from books.models import Book

def search_form(request):
    return render(request, 'books/search_form.html')

def search(request):
    """searches the database for a certain book"""
    errors = []
    if 'q' in request.GET: # check to make sure 'q' exists, and make sure q is a non-empty value
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.') # if no search term passed, pass this error
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q) # query book table for all books whose title includes the submission
            return render(request, 'books/search_results.html', {'books': books, 'query': q})
    return render(request, 'books/search_form.html', {'errors': errors})