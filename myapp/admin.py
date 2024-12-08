from django.contrib import admin

# Register your models here.
from .models import Document

admin.site.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')