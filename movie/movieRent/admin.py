from django.contrib import admin
from .models import Category, Movie

# Register your models here.
# Login 
# U : admin
# P : movieadmin!QAZ


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['category_name', 'item_num', 'slug']
	prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category,CategoryAdmin)

class MovieAdmin(admin.ModelAdmin):
	list_display = ['movie_name', 'slug', 'in_stock', 'price',
					'pub_date', 'available', 'category']
	list_filter = ['pub_date', 'available']
	list_editable = ['in_stock', 'price', 'available']
	prepopulated_fields = {'slug': ('movie_name',)}


admin.site.register(Movie,MovieAdmin)

