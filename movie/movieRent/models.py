from django.db import models

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=20, default="Action")
	item_num = models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.category_name

class MovieProduct(models.Model):
	categorye = models.ForeignKey(Category, on_delete=models.CASCADE)
	movie_name = models.CharField(max_length=20, default="Fast Frious")
	movie_describe = models.TextField(max_length=100)
	movie_score = models.FloatField(default= 10.0)
	in_stock = models.PositiveIntegerField(default=0)
	price = models.FloatField(default=500.0)
	picture = models.ImageField(upload_to=None)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.movie_name
