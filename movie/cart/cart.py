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
			cart = self.ssession[settings.CART_SESSION_ID] = {}
		self.cart = cart

	def add(self, movie, quantity=1, update_quantity=False):
		'''
		Add a movie to the cart or update its quantity
		'''
		movie_id = str(movie_id)
		if movie_id not in self.cart:
			self.cart[movie_id] = {'quantity':0, 'price': str(movie.price)}
		if update_quantity:
			self.cart[movie_id]['quantity'] = quantity
		else:
			self.cart[movie_id]['quantity'] += quantity
		self.save() 