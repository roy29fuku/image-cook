from django.contrib import admin

# Register your models here.
@admin.register(Book)
class UserAdmin(admin.ModelAdmin):
    pass