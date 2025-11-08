

# Query all books by a specific author.

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author) 

# List all books in a library.

library = Library.objects.get(name="Central Library")
books = library.books.all()

# Retrieve the librarian for a library.

librarian = Library.objects.get(name=library_name)
print(f"Librarian: {librarian.name}")

