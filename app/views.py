from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from app.forms.forms import BookQueryForm, BookForm
from app.models import Author, Publisher, Book


# Create your views here.

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)

def author(request):
    authors = Author.objects.all()  # Retrieve all authors
    return render(request, 'author.html', {'authors': authors})

def publishers(request):
    publishers = Publisher.objects.all()  # Retrieve all publishers
    return render(request, 'publishers.html', {'publishers': publishers})

def books(request):
    books = Book.objects.all()  # Retrieve all books
    return render(request, 'books.html', {'books': books})


def bookquery(request):
    # if POST request, process form data
    if request.method == 'POST':
        # create form instance and pass data to it
        form = BookQueryForm(request.POST)
        if form.is_valid():  # is it valid?
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'books.html', {'books': books, 'query': query})
    # if GET (or any other method), create blank form
    else:
        form = BookQueryForm()

    return render(request, 'bookquery.html', {'form': form})

def author_books(request, author_name):
    # Retrieve the author by name (case-insensitive lookup)
    author = get_object_or_404(Author, name__iexact=author_name)

    # Query the books that have this author
    books = Book.objects.filter(authors=author)  # Filter books by this author

    return render(request, 'author_books.html', {'author': author, 'books': books})


 # Only logged-in users can access this page
def add_book(request):

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():

            form.save()  # Save the new book
            return redirect('Books')  # Redirect to the books list page
    else:
        form = BookForm()

    return render(request, 'add_books.html', {'form': form})


def buy_book(request,book_name):
    book = get_object_or_404(Book, name_iexact=book_name)

    # Get the purchased books from session or create a new list
    purchased_books = request.session.get('purchased_books', [])

    # Add the book ID to the purchased books list
    if book_name not in purchased_books:
        purchased_books.append(book_name)
        request.session['purchased_books'] = purchased_books  # Save back to session

    return redirect('books')  # Redirect to the books page


def purchased_books(request):
    purchased_ids = request.session.get('purchased_books', [])
    purchased_books = Book.objects.filter(id__in=purchased_ids)  # Get books by purchased IDs

    return render(request, 'purchased_books.html', {'purchased_books': purchased_books})
