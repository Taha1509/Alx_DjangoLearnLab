# RETRIEVE Operation

## Command:
```python
from bookshelf.models import Book
all_books = Book.objects.all()
print("All books:", list(all_books))
book = Book.objects.get(title="1984")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")

All books: [<Book: 1984>]
Title: 1984
Author: George Orwell
Publication Year: 1949