from django.contrib import admin
from library.books.models import Books


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Books, BookAdmin)
