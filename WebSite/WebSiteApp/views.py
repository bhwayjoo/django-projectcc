from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import BookForms ,CategoryForm
# Create your views here.
def index(request):
    if request.method == 'POST':
        add_book=BookForms(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
        add_book=CategoryForm(request.POST)
        if add_book.is_valid():
            add_book.save()

    context={
    'category' : Category.objects.all(),
    'books' : Book.objects.all(),
    'form': BookForms(),
    'formcat': CategoryForm(),
    'allbooks': Book.objects.filter(active=True).count(),
    'booksold': Book.objects.filter(status='sold').count(),
    'bookrental': Book.objects.filter(status='rental').count(),
    'bookacailble': Book.objects.filter(status='availble').count(),
    }
    print (Book.objects.count())
    return render(request,'pages/index.html',context=context)

def books(request):
    search=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title= request.GET['search_name']
    if title:
        search=search.filter(title__icontains=title)





    if request.method == 'POST':
        add_book=CategoryForm(request.POST)
        if add_book.is_valid():
            add_book.save()
    context={
    'category' : Category.objects.all(),
    'books' : search,
    'formcat': CategoryForm(),
    
    }
    return render(request,'pages/books.html',context=context)




def delete(request, id):
    book_delete= get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')

def update(request, id):
    book_id= Book.objects.get(id=id)
    if request.method =='POST':
        book_save= BookForms(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save=BookForms(instance=book_id)
    context={
        'form':book_save,
    }
    return render(request,'pages/update.html', context=context)
