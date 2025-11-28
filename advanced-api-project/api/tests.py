from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User
"""
Testing Strategy for Book API

Test Coverage:
1. Authentication & Permissions
   - Unauthenticated users can read but not write
   - Authenticated users can perform all CRUD operations

2. CRUD Operations
   - Create books with valid data
   - Retrieve single books and lists
   - Update existing books
   - Delete books

3. Data Validation
   - Publication year cannot be in future
   - Required fields validation

4. Advanced Features
   - Filtering by author and publication year
   - Searching by title and author name
   - Ordering by various fields

Running Tests:
- Run all tests: python manage.py test api
- Run specific test case: python manage.py test api.tests.BookAPITestCase
- Verbose output: python manage.py test api -v 2

Test Database:
- Tests use a separate SQLite database
- Database is created fresh for each test run
- All test data is cleaned up automatically
"""


class BookAPITestCase(APITestCase):
    """
    Test case for Book API endpoints
    """
    
    def setUp(self):
        """
        Set up test data that will be used across all test methods
        """
        # Create test users
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword123'
        )
        self.admin_user = User.objects.create_superuser(
            username='admin',
            password='adminpassword123',
            email='admin@example.com'
        )
        
        # Create test authors
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George Orwell')
        
        # Create test books
        self.book1 = Book.objects.create(
            title='Harry Potter',
            publication_year=1997,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author2
        )
        self.book3 = Book.objects.create(
            title='Animal Farm',
            publication_year=1945,
            author=self.author2
        )
        
        # Initialize API client
        self.client = APIClient()
    
    def test_list_books_unauthenticated(self):
        """
        Test that unauthenticated users can list books
        """
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Should return all 3 books
    
    def test_create_book_unauthenticated(self):
        """
        Test that unauthenticated users cannot create books
        """
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_create_book_authenticated(self):
        """
        Test that authenticated users can create books
        """
        self.client.force_authenticate(user=self.user)
        
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2020,
            'author': self.author1.id
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)  # Should have 4 books now
        self.assertEqual(response.data['title'], 'New Book')
    
    def test_retrieve_single_book(self):
        """
        Test retrieving a single book by ID
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.id})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Harry Potter')
        self.assertEqual(response.data['publication_year'], 1997)
    
    def test_update_book_authenticated(self):
        """
        Test that authenticated users can update books
        """
        self.client.force_authenticate(user=self.user)
        
        url = reverse('book-update', kwargs={'pk': self.book1.id})
        data = {
            'title': 'Harry Potter - Updated',
            'publication_year': 1997,
            'author': self.author1.id
        }
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Harry Potter - Updated')
    
    def test_delete_book_authenticated(self):
        """
        Test that authenticated users can delete books
        """
        self.client.force_authenticate(user=self.user)
        
        url = reverse('book-delete', kwargs={'pk': self.book1.id})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)  # Should have 2 books left
    
    def test_validation_future_publication_year(self):
        """
        Test that books with future publication years are rejected
        """
        self.client.force_authenticate(user=self.user)
        
        url = reverse('book-create')
        data = {
            'title': 'Future Book',
            'publication_year': 2030,  # Future year
            'author': self.author1.id
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('publication_year', response.data)


class BookFilterSearchOrderTest(APITestCase):
    """
    Test filtering, searching, and ordering functionality
    """
    
    def setUp(self):
        self.author1 = Author.objects.create(name='J.K. Rowling')
        self.author2 = Author.objects.create(name='George Orwell')
        
        self.book1 = Book.objects.create(
            title='Harry Potter',
            publication_year=1997,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author2
        )
        self.book3 = Book.objects.create(
            title='Animal Farm',
            publication_year=1945,
            author=self.author2
        )
        
        self.client = APIClient()
    
    def test_filter_by_author(self):
        """
        Test filtering books by author
        """
        url = reverse('book-list')
        response = self.client.get(url, {'author': self.author2.id})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books by Orwell
    
    def test_search_books(self):
        """
        Test searching books by title and author name
        """
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'harry'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Harry Potter')
    
    def test_order_books_by_title(self):
        """
        Test ordering books by title
        """
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'title'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should be ordered alphabetically: 1984, Animal Farm, Harry Potter
        self.assertEqual(response.data[0]['title'], '1984')
        self.assertEqual(response.data[2]['title'], 'Harry Potter')
    
    def test_order_books_by_year_desc(self):
        """
        Test ordering books by publication year descending
        """
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-publication_year'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Should be ordered by newest first: 1997, 1949, 1945
        self.assertEqual(response.data[0]['publication_year'], 1997)
        self.assertEqual(response.data[2]['publication_year'], 1945)


class AuthorAPITestCase(APITestCase):
    """
    Test case for Author API endpoints (if you have them)
    """
    
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        self.client = APIClient()
    
    def test_list_authors(self):
        """
        Test listing all authors
        """
        url = reverse('author-list')  # Make sure you have this URL pattern
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)