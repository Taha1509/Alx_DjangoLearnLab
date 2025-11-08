

# Query all books by a specific author.

author = Author.objects.get(name="J.K. Rowling") 
books_by_author = Book.objects.filter(author=author) 

# List all books in a library.

library = Library.objects.get(name="Central Library")
books = library.books.all()

# Retrieve the librarian for a library.

librarian = Library.objects.get(library__name="Central Library")
print(f"Librarian: {librarian.name}")

