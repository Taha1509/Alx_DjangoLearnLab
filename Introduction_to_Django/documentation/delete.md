# DELETE Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
all_books = Book.objects.all()
print("Remaining books:", list(all_books))
try:
    Book.objects.get(title="Nineteen Eighty-Four")
    print("Book still exists")
except Book.DoesNotExist:
    print("Book successfully deleted - DoesNotExist exception raised")

Remaining books: []
Book successfully deleted - DoesNotExist exception raised