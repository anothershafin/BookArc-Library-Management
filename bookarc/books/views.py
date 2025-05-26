from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book
from .forms import BookForm

def home(request):
    q = request.GET.get('q','')
    books = Book.objects.filter(
        models.Q(name__icontains=q) |
        models.Q(author__icontains=q) |
        models.Q(genre__icontains=q)
    ) if q else Book.objects.all().order_by('-release_date')[:10]
    return render(request, 'books/home.html', {'books': books, 'q': q})

@login_required
def add_book(request):
    if request.user.role != 'librarian':
        return redirect('books:home')
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('books:home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
