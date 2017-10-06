from django.contrib import admin
from .models import Publisher, Author, Book, AuthorAdmin, BookAdmin

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
