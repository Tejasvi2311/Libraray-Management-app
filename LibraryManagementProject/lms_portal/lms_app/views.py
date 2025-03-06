from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from django.template import context

from .models import *
from .utils import searching_books

from django.utils import timezone
from datetime import timedelta

from django.contrib import messages
from django.db.models import Sum

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def calculate_total_book_count():
    # Retrieve the total count of books in the library
    total_count = add_books.objects.aggregate(total_count=Sum('count'))['total_count']
    # If there are no books, return 0 to avoid NoneType errors
    return total_count if total_count else 0

def calculate_unique_book_titles_count():
    # Retrieve all books from the database
    all_books = add_books.objects.all()

    unique_books = set()  # Use a set to store unique book identifiers

    # Iterate over each book
    for book in all_books:
        # Construct a unique identifier for the book using its name and author
        book_identifier = (book.book_name, book.author_name)
        # Add the book identifier to the set
        unique_books.add(book_identifier)

    # Return the count of unique books
    return len(unique_books)

def home(request):
    return render(request,"home.html",context={})

def add_book(request):
    total_book_count = calculate_total_book_count()
    total_book_title= calculate_unique_book_titles_count()
    return render(request,"add_book.html",context={"current_tab":"add_book","total_book_count": total_book_count,"total_book_title": total_book_title})

def search_book(request):
    return render(request,"search_book.html",context={"current_tab":"search_book"})

'''def issue_book(request):
    return render(request,"issue_book.html",context={"current_tab":"issue_book"})'''

def delete_book(request):
    return render(request,"delete_book.html",context={"current_tab":"delete_book"})

def shopping(request):
    return HttpResponse("Welcome Shopping!")

def save_student(request):
    stu_name=request.POST['Student_name']
    return render(request,"welcome.html",context={'stu_name':stu_name})
    '''stu_age = request.POST['Student_age']
    return render(request, "welcome.html", context={'stu_age': stu_age})'''



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Assuming 'index' is the name of the URL pattern for index.html
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def index_view(request):
    return render(request, 'index.html')


def addbook_tab(request):
    add_book=add_books.objects.all()
    total_book_count = calculate_total_book_count()
    total_book_title = calculate_unique_book_titles_count()
    print(total_book_count)
    return render(request,"add_book.html",
                  context={"current_tab":"add_book",
                                                "add_book":add_book,"total_book_count": total_book_count,"total_book_title": total_book_title})
def save_book(request):
    book_name = request.POST['bookName']
    author_name = request.POST['authorName']
    publication = request.POST['publication']

    # Check if the book already exists in the database
    existing_book = add_books.objects.filter(book_name=book_name, author_name=author_name, publication=publication).first()

    if existing_book:
        # If the book exists, increment its count
        existing_book.count += int(request.POST['count'])
        existing_book.save()
        messages.success(request, f'Book {existing_book.book_name} added successfully')
    else:
        # If the book doesn't exist, create a new entry
        book_item = add_books(
            book_name=book_name,
            author_name=author_name,
            publication=publication,
            count=request.POST['count']
        )
        book_item.save()
        messages.success(request, f'Book {book_item.book_name} added successfully')
    total_book_count = calculate_total_book_count()
    total_book_title= calculate_unique_book_titles_count()

    return redirect('/add_book')
def search_view(request):
    query = request.GET.get('q')  # Assuming the search query is passed as a GET parameter
    books = None
    if query:
        # Linear search
        books = searching_books(query)

        # Sort books by name using an efficient sorting algorithm (e.g., merge sort)
        if books:
            books = merge_sort(books)

    return render(request, 'search_book.html', {'books': books, 'query': query})

def searching_books(query):
    # Get all books from the database
    all_books = add_books.objects.all()

    # Separate books that start with the query from those that contain the query
    #start_with_query = [book for book in all_books if book.book_name.lower().startswith(query.lower())]
    contains_query = [book for book in all_books if query.lower() in book.book_name.lower() or query.lower() in book.author_name.lower()]

    # Sort the books that start with the query alphabetically by name
    #merge_sort(start_with_query)

    # Sort the books that contain the query alphabetically by name
    merge_sort(contains_query)

    # Concatenate the two lists with books starting with the query appearing first
    matching_books = contains_query

    return matching_books



def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].book_name < right[right_index].book_name:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left and right halves
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result




# views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import add_books, IssuedBook
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.http import JsonResponse
from .models import add_books, IssuedBook
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

@csrf_exempt


def issue_book(request):
    success_message = None
    error_message = None

    # Retrieve all issued books
    issued_books = IssuedBook.objects.all()

    # Define the return period (e.g., 15 days)
    return_period = 15  # Change this value as needed

    # Calculate the time left for return for each issued book
    for issued_book in issued_books:
        # Calculate the difference between the current date/time and the issue date/time
        time_difference = timezone.now() - issued_book.issue_date
        # Subtract the time difference from the return period
        time_left = return_period - time_difference.days

        # Add the time left for return to the issued book instance
        issued_book.time_left_for_return = time_left

    # Pass the issued books to the template for rendering
    context = {
        'issued_books': issued_books,
        'success_message': success_message,
        'error_message': error_message,
        'current_tab': 'issue_book'
    }

    if request.method == 'POST':
        action = request.POST.get('action', None)  # Determine if it's an issue or return action
        book_name = request.POST.get('book_name', None)
        author_name = request.POST.get('author_name', None)
        borrower_roll_no = request.POST.get('borrower_roll_no', None)  # Get the borrower's roll number from the request

        if action == 'issue':
            # Issue Book Process
            if book_name is None or author_name is None or borrower_roll_no is None:
                error_message = 'Please provide book name, author name, and borrower\'s roll number.'
            else:
                # Retrieve all books with the given name and author
                books = add_books.objects.filter(book_name__iexact=book_name, author_name__iexact=author_name)


                if not books.exists():
                    error_message = f'Book with name "{book_name}" by author "{author_name}" not found.'
                else:
                    # Choose one of the books if multiple exist
                    book = books.first()  # Choose the first book for simplicity, you can add more logic here if needed

                    if book.count <= 0:
                        error_message = f'Sorry, the book "{book_name}" by author "{author_name}" is currently not available for issuing.'
                    else:
                        # Create the borrower if not already exists
                        borrower, _ = User.objects.get_or_create(username=borrower_roll_no)

                        # Get the current date and time
                        issuance_datetime = timezone.now()

                        # Create an IssuedBook instance with book, borrower, and issuance datetime
                        issued_book = IssuedBook.objects.create(
                            book=book,
                            borrower=borrower,
                            issue_date=issuance_datetime
                        )

                        # Update count of the book
                        book.count -= 1
                        book.save()

                        success_message = f'Book "{book_name}" by author "{author_name}" issued successfully to {borrower.username} on {issuance_datetime}.'

        elif action == 'return':
            # Return Book Process
            if book_name is None or author_name is None or borrower_roll_no is None:
                error_message = 'Please provide book name, author name, and borrower\'s roll number'
            else:
                # Retrieve the issued book to return
                issued_book_to_return = get_object_or_404(IssuedBook, book__book_name__iexact=book_name, book__author_name__iexact=author_name, borrower__username=borrower_roll_no)

                # Update count of the book
                issued_book_to_return.book.count += 1
                issued_book_to_return.book.save()

                # Delete the issued book instance
                issued_book_to_return.delete()

                success_message = f'Book "{book_name}" by author "{author_name}" returned successfully by {borrower_roll_no}'

    context['success_message'] = success_message
    context['error_message'] = error_message
    total_book_count = calculate_total_book_count()

    return render(request, "issue_book.html", context)


def book_list(request):
    query = request.GET.get('q')
    books = add_books.objects.all()

    if query:
        books = books.filter(book_name__icontains=query)

    # Convert queryset to a list
    books_list = list(books)

    # Apply merge sort algorithm to sort books by book name
    sorted_books = merge_sort(books_list)

    return render(request, 'delete_book.html', {'books': sorted_books, 'query': query})
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].book_name < right[right_index].book_name:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Append any remaining elements from left and right halves
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def deleting_book(request):

    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(add_books, id=book_id)
        book_name = book.book_name
        book.delete()
        messages.success(request, f'Book "{book_name}" has been deleted successfully')
        print(f'Deleted book: {book_name}')  # Add this line for debugging

    total_book_count = calculate_total_book_count()
    total_book_title = calculate_unique_book_titles_count()
    return redirect('book_list')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    # Redirect to a desired page after logout, e.g., the login page
    return redirect('login')