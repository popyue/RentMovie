from django.contrib import admin
from .models import Category, MovieProduct

# Register your models here.
# Login 
# U : admin
# P : movieadmin!QAZ

admin.site.register(Category)
admin.site.register(MovieProduct)

