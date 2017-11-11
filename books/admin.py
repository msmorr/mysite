from django.contrib import admin
from .models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date') # Shows fields in list
    list_filter = ('publication_date',) # orders entries by publication_date
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',) # orders entries by publication_date
    fields = ('title', 'authors', 'publisher')  # shows certain fields in the edit form
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher',) # displays fields in the admin with a simple text box. 
    #  Improves performance when there is a large amount of data.

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin) # links Author class with AuthorAdmin subclass/ModelAdmin
admin.site.register(Book, BookAdmin)