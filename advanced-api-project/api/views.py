from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework


# Create your views here.

class BookListView(generics.ListAPIView):
    """
    API view to retrieve all books with advanced filtering, searching, and ordering capabilities.
    
    Filtering:
    - author: Filter by author ID (exact match)
    - publication_year: Filter by exact year
    - publication_year__gte: Books published from this year onwards
    - publication_year__lte: Books published up to this year
    
    Searching:
    - Searches in title and author name fields
    
    Ordering:
    - Order by any book field: title, publication_year, etc.
    - Use hyphen for descending: -publication_year (newest first)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    
    # Step 1: Filtering Backend
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # Filter configuration
    filterset_fields = {
        'author': ['exact'],
        'publication_year': ['exact', 'gte', 'lte'],
    }
    
    # Step 2: Search configuration
    search_fields = ['title', 'author__name']
    
    # Step 3: Ordering configuration
    ordering_fields = ['title', 'publication_year', 'author__name']
    ordering = ['-publication_year']  # Default ordering
    
    def get_queryset(self):
        """
        Additional custom filtering logic can be added here if needed
        """
        queryset = super().get_queryset()
        
        # You can add any additional custom filtering here
        # For example, only show books from certain years range
        min_year = self.request.query_params.get('min_year')
        max_year = self.request.query_params.get('max_year')
        
        if min_year:
            queryset = queryset.filter(publication_year__gte=min_year)
        if max_year:
            queryset = queryset.filter(publication_year__lte=max_year)
            
        return queryset

def get_queryset(self):
        """
        Customize the queryset to include filtering
        """
        queryset = Book.objects.all()
        
        # Filter by author if provided in query parameters
        author_id = self.request.query_params.get('author_id')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        
        # Order by publication year (newest first)
        queryset = queryset.order_by('-publication_year')
        
        return queryset


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a single book by ID (Read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Must be logged in

    def perform_create(self, serializer):
        print(f"Creating new book: {serializer.validated_data.get('title')}")
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Must be logged in

    def perform_update(self, serializer):
        print(f"Updating book: {serializer.instance.title}")
        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delete a book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Must be logged in

    def perform_destroy(self, instance):
        """
        Customize what happens when a book is deleted
        """
        print(f"Deleting book: {instance.title}")
        instance.delete()
