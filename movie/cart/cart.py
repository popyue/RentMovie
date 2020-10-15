from decimal import Decimal
from django.conf import settings
from movieRent.models import Movie 

class Cart(object):
	def __init__(self, request):
		'''
		Initialize the cart
		'''
		self.session = request.session
		cart = self.session.get(settings.CART_SESSION_ID)
		if not cart:
			# save an empty cart in the session
			cart = self.session[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, movie, quantity=1, update_quantity=False):
		'''
		Add a movie to the cart or update its quantity
		'''
		movie_id = str(movie.id)
		if movie_id not in self.cart:
			self.cart[movie_id] = {'quantity':0, 'price': str(movie.price)}
		if update_quantity:
			self.cart[movie_id]['quantity'] = quantity
		else:
			self.cart[movie_id]['quantity'] += quantity
		self.save()

	def save(self):
		# Update the session cart
		self.session[settings.CART_SESSION_ID] = self.cart
		#Mark the session as "modified" to make sure it is saved
		self.session.modified = True

	def remove(self, movie):
		'''
		Remove a movie from the cart 
		'''
		movie_id = str(movie.id)
		if movie_id in self.cart:
			del self.cart[movie_id]
			self.save()

	def __iter__(self):
		'''
		Iterate over the items in the cart and get the movies from the database
		'''
		movie_ids = self.cart.keys()
		# Get the movie objects and add them to the cart 
		movies = Movie.objects.filter(id__in=movie_ids)
		for movie in movies:
			self.cart[str(movie.id)]['movie'] = movie
		for item in self.cart.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		'''
		Count all items in the cart 
		'''
		# movieRent/templates/base_generic.html  {% with total_item=cart|length %}
		return sum(item['quantity'] for item in self.cart.values())

	def get_total_price(self):
		return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

	def clear(self):
		# Remove cart from session
		del self.session[settings.CART_SESSION_ID]
		self.session.modified = True