from django.db import models

# Create your models here.
# The Author model is used to create the author instance  
# It contains basic details about the author like te name of the author.
class Author(models.Model):
    name = models.CharField(max_length=200) 
    
    def __str__(self):
        return f"{self.name}"
    
    
# The book model is used to create the books instance of the app
# It contains basic details about the book instance like title, publication_year, and author.
class Book(models.Model):
    title = models.CharField(max_length=100)  # title of the book instance
    publication_year = models.DateField(auto_now_add=True) # publication year when the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') # The author who wrote the book.
    """
    # ForeignKey relationship to the Author model.
    # Establishes a one-to-many relationship from Author to Books. 
    # # If an author is deleted, all their related books will also be 
    # deleted (on_delete=models.CASCADE). 
    """
    
def __str__(self):
    return f"{self.title} by {self.author} {self.publication_year}"