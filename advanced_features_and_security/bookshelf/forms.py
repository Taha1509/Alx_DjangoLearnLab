from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
    
    # SECURE: Custom validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")
        return title.strip()  # SECURE: Input sanitization

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 2:
            raise forms.ValidationError("Author name must be at least 2 characters long.")
        return name.strip()