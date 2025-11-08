
from django.urls import path
from .views import List_All_Books, LibraryDetailView  # Specific imports
from .views import list_books
urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('books/', List_All_Books, name='all-books'),
]