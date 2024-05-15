from django.contrib import admin
from .models import Author, Book, category, BookAuthor, Review
# Register your models here.


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(category)
admin.site.register(BookAuthor)
admin.site.register(Review)