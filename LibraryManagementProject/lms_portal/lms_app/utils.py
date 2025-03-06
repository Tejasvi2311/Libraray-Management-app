# utils.py

from .models import add_books

def searching_books(query):
    """
    Function to search for books in the database based on a query string.

    Args:
        query (str): The search query.

    Returns:
        QuerySet: A queryset containing the books that match the search query.
    """
    # Assuming you want to search by book title
    # You can modify this to search by other attributes like author, genre, etc.
    return add_books.objects.filter(book_name__icontains=query)
