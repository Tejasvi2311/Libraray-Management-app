from django.db import models
from django.contrib.auth.models import User

class add_books(models.Model):
    def __str__(self):
        return self.book_name
    book_name=models.TextField()
    author_name=models.CharField(max_length=200)
    publication=models.TextField()
    count=models.IntegerField()
    class Meta:
        db_table='add_books'

class IssuedBook(models.Model):
    book = models.ForeignKey(add_books, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=200,default="Unknown")
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issued {self.book} to {self.borrower.username} on {self.issue_date}"