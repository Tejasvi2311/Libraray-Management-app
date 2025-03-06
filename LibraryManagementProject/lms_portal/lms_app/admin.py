from django.contrib import admin
from .models import add_books
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(add_books)
class userdat(ImportExportModelAdmin):
    pass

from .models import IssuedBook

class IssuedBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'borrower', 'issue_date']
    list_filter = ['issue_date']
    search_fields = ['book__book_name', 'borrower__username']

admin.site.register(IssuedBook, IssuedBookAdmin)