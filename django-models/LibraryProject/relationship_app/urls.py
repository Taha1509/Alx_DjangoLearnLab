from django.urls import path
from .views import (
     List_All_Books, 
     LibraryDetailView, 
     RegisterView ,
     admin_view,
     librarian_view,
     member_view,
     add_book,           
     edit_book,
     delete_book
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('books/', List_All_Books, name='all-books'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),  
    path('books/add_book/', add_book, name='add-book'),
    path('books/edit_book/<int:book_id>/', edit_book, name='edit-book'),
    path('books/delete/<int:book_id>/', delete_book, name='delete-book'),
]


#views.register