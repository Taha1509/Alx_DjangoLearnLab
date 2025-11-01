# CREATE Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book.title} by {book.author}")

Book created with ID: 1
Book created: 1984 by George Orwell
"Book.objects.create"