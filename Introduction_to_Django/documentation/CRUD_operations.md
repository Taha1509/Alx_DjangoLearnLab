# CRUD Operations Documentation

This document summarizes all CRUD operations performed on the Book model.

## Operations Performed:

1. **CREATE** - Created a new book "1984" by George Orwell
2. **RETRIEVE** - Retrieved and displayed the book details
3. **UPDATE** - Updated the title to "Nineteen Eighty-Four"
4. **DELETE** - Deleted the book from the database

## Files:
- [CREATE Operation](create.md)
- [RETRIEVE Operation](retrieve.md)
- [UPDATE Operation](update.md)
- [DELETE Operation](delete.md)

## Model Definition:
The Book model was defined in `bookshelf/models.py` with:
- title: CharField(max_length=200)
- author: CharField(max_length=100)
- publication_year: IntegerField()

All operations were performed successfully and verified.