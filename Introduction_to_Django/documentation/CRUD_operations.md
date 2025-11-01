# CRUD Operations Documentation

This document summarizes all CRUD operations performed on the Book model.

## Operations Performed:

1. **CREATE** - Created a new book "1984" by George Orwell using `Book.objects.create()`
2. **RETRIEVE** - Retrieved and displayed the book details using `Book.objects.get()`
3. **UPDATE** - Updated the title to "Nineteen Eighty-Four"
4. **DELETE** - Deleted the book from the database

## Detailed Documentation:
- [CREATE Operation](create.md)
- [RETRIEVE Operation](retrieve.md)
- [UPDATE Operation](update.md)
- [DELETE Operation](delete.md)

## Methods Used:
- **Create**: `Book.objects.create()`
- **Retrieve**: `Book.objects.all()` and `Book.objects.get()`
- **Update**: Direct attribute assignment and `.save()`
- **Delete**: `.delete()` method

## Verification:
All CRUD operations were performed successfully and verified through the Django shell.