from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, category, BookAuthor, Review
from .forms import ProductForm

def get_info(request):      
    Category = category.objects.all()
    context = {
        'Category': Category,
    }
    return render(request, 'index.html', context=context)



from django.shortcuts import render
from .models import Book

def get_book(request, pk):
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'books.html', context=context)

def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'Book': book,
    }
    return render(request, 'detail.html', context=context)

def add_book(request):
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('project:get_info')
    context = {
        'form': form
    }
    return render(request, 'create.html',context=context)

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('project:get_info') 
    else:
        form = ProductForm(instance=book)

    context = {'form': form}
    return render(request, 'update.html', context)

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('project:get_info')
    return render(request, 'delete.html', {'book':book})