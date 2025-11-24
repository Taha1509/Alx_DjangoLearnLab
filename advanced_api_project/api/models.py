




from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Author model representing a book author.
    
    Attributes:
        name (CharField): Full name of the author (max 100 characters)
        email (EmailField): Contact email address (optional)
        bio (TextField): Author biography (optional)
        date_of_birth (DateField): Author's birth date (optional)
        nationality (CharField): Author's country of origin (max 50 characters, optional)
    """
    name = models.CharField(max_length = 200)


    def __str__(self):
        return self.name
    


class Book(models.Model):

    title = models.CharField(max_length = 200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title