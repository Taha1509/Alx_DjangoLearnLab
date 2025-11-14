from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Get content type for Book model
content_type = ContentType.objects.get_for_model(Book)

# Get permissions
can_view = Permission.objects.get(codename='can_view', content_type=content_type)
can_create = Permission.objects.get(codename='can_create', content_type=content_type)
can_edit = Permission.objects.get(codename='can_edit', content_type=content_type)
can_delete = Permission.objects.get(codename='can_delete', content_type=content_type)

# Create groups and assign permissions
viewers, created = Group.objects.get_or_create(name='Viewers')
viewers.permissions.add(can_view)

editors, created = Group.objects.get_or_create(name='Editors')
editors.permissions.add(can_view, can_create, can_edit)

admins, created = Group.objects.get_or_create(name='Admins')
admins.permissions.add(can_view, can_create, can_edit, can_delete)