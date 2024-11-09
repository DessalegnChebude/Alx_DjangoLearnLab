from relationship_app.models import Book,Library, Librarian

# Query to get all books by a specific author
def get_books_by_author(author_name):
    books = Book.objects.filter(author=author_name)
    return books

# Query to get all books in a specific library
def get_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()  # 'books' is the related name used in Library model
    return books

#  Retrieve the Librarian for a Library
def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    librarian = library.librarian  # 'librarian' is the ForeignKey field in Library model
    return librarian

# Putting It All Together
def get_books_by_author(author_name):
    books = Book.objects.filter(author=author_name)
    return books

def get_books_in_library(library_id):
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books

def get_librarian_for_library(library_id):
    library = Library.objects.get(id=library_id)
    librarian = library.librarian
    return librarian