from django.contrib import admin
from management.models import Books, Patron, Borrowing

# Register your models here.
admin.site.register(Books)
admin.site.register(Patron)
admin.site.register(Borrowing)