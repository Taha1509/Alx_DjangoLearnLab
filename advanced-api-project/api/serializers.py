from .models import Book, Author
from rest_framework import serializers
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model that handles serialization of all book fields
    and includes custom validation for the publication year.
    
    Validation:
        - Ensures publication_year is not in the future
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_date(self, value):
        """
        Validate that the publication year is not in the future.
        
        Args:
            value (int): The publication year to validate
            
        Returns:
            int: The validated publication year
            
        Raises:
            ValidationError: If the publication year is in the future
        """
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication date cannot be in the future.")
        
        return value
    

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    
    Currently serializes all author fields. In a more advanced implementation,
    this would include nested BookSerializer to represent the one-to-many
    relationship where one author can have multiple books.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = '__all__'