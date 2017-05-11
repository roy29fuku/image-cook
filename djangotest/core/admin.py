from django.contrib import admin
from core.models import Book

# Register your models here.
@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    pass