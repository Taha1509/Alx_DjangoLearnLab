from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView, ListView

# Create your views here.

def List_All_Books(request):
    books = Book.objects.all()  
    context = {'books': books}  
    return render(request, 'relationship_app/list_books.html', context)  

class LibraryDetailView(DetailView): 
    model = Library
    template_name = 'library_detail.html'  
