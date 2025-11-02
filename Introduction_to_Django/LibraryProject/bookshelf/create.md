# CREATE Operation

## Command:
```python
from bookshelf.models import Book
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book.save()
print(f"Book created with ID: {book.id}")

Book created with ID: 1