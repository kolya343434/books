from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AreaOfExpertise, Author, Book, Document

admin.site.register(AreaOfExpertise)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Document)  # Убедитесь, что эта строка есть только один раз


