from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Fields to display in the user list
    list_display = ['username', 'email', 'date_of_birth', 'role', 'is_staff']
    
    # Fields to search by
    search_fields = ['username', 'email', 'role']
    
    # Fields to filter by
    list_filter = ['role', 'is_staff', 'is_superuser', 'date_of_birth']
    
    # How fields are organized in edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_picture', 'role')}),
    )
    
    # Fields shown when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_picture', 'role')}),
    )

    