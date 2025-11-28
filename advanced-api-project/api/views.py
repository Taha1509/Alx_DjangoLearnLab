from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
# Create your views here.

class BookListView(generics.ListAPIView):
    """
    API view to retrieve all books (Read-only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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
