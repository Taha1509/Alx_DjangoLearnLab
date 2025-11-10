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
from django.contrib.auth.decorators import user_passes_test, login_required, user_passes_test
from django.shortcuts import render
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

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')



#class login(CreateView):
    
    #LoginClass =  LoginView
  
#class logout(CreateView):

    #LogoutClass = LogoutView