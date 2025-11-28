from django.urls import path
from .views import (
     BookListView, 
     BookDetailView, 
     BookCreateView ,
     BookUpdateView,
     BookDeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books', BookListView.as_view()(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view()(), name = 'book-details'),
    path('book/new/', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>/edit/',BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete/',BookDeleteView.as_view(), name='book-delete'),

]
