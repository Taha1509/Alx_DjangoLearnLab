from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login

# Create your views here.

def List_All_Books(request):
    books = Book.objects.all()  
    context = {'books': books}  
    return render(request, 'relationship_app/list_books.html', context)  

class LibraryDetailView(DetailView): 
    model = Library
    template_name = 'relationship_app/library_detail.html'  


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

#class login(CreateView):
    
    #LoginClass =  LoginView
  
#class logout(CreateView):

    #LogoutClass = LogoutView