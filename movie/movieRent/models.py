from django.db import models
from django.urls  import reverse
# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=20, default="Action")
	item_num = models.PositiveIntegerField(default=1)
	slug = models.SlugField(max_length=200,
		db_index=True,
		unique=True,
		default=None)
	
	class Meta:
		ordering = ('category_name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	
	def __str__(self):
		return self.category_name
	
	def get_absolute_url(self):
		return reverse('movieRent:movie_list_by_category',
			args=[self.slug])

class Movie(models.Model):
	category = models.ForeignKey(
			Category,
			related_name='movies', 
			on_delete=models.CASCADE)
	movie_name = models.CharField(max_length=20, default="Fast Frious")
	slug = models.SlugField(max_length=200, db_index=True,default=None)
	movie_describe = models.TextField(max_length=1000)
	movie_score = models.FloatField(default= 10.0)
	in_stock = models.PositiveIntegerField(default=0)
	price = models.FloatField(default=500.0)
	picture = models.ImageField(upload_to='static/movie_pic/', null=True)
	videofile= models.FileField(upload_to='static/videos/', null=True, verbose_name="")
	pub_date = models.DateTimeField(auto_now_add=True)
	available = models.BooleanField(default=True)
	
	class Meta:
		ordering = ('movie_name',)
		index_together = (('id', 'slug'),)
	
	def __str__(self):
		return self.movie_name
	
	def get_absolute_url(self):
		return reverse('movieRent:movie_content', args=[self.id, self.slug])

