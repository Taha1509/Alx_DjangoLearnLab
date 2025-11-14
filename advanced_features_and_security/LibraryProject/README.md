
"""
PERMISSIONS AND GROUPS SETUP GUIDE
===================================

1. CUSTOM PERMISSIONS (models.py):
   - Added to Book model: can_view, can_create, can_edit, can_delete
   - These control access to book-related operations

2. GROUPS CONFIGURATION (Django Admin):
   - Viewers Group: can_view permission only
   - Editors Group: can_view, can_create, can_edit permissions  
   - Admins Group: All permissions (can_view, can_create, can_edit, can_delete)

3. PROTECTED VIEWS (views.py):
   - /books/ (book_list): requires 'bookshelf.can_view'
   - /books/create/ (book_create): requires 'bookshelf.can_create'
   - /books/<id>/edit/ (book_edit): requires 'bookshelf.can_edit' 
   - /books/<id>/delete/ (book_delete): requires 'bookshelf.can_delete'

4. TESTING:
   - Create users and assign to groups in Django Admin
   - Login as each user type to verify permissions work correctly
   - Viewers: Can only list books
   - Editors: Can list, create, and edit books
   - Admins: Full access to all book operations
"""