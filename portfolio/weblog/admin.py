from django.contrib import admin
from .models import Category

@admin.register(Category)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id","title","created_at","update_at"]
    
