from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Category, MovieProduct


# Create your views here.
def index(request, category_slug=None):
	#return HttpResponse("Hello, world. You're at the Movie Rent Store index.")
	category = None
	categories = Category.object.all()
	movie = MovieProduct.object.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		movie = movie.filter(category=category)
	return render(request, 
		'movieRent/templates/index.html',
		{ 
		'category' : category,
		'categories': categories,
		'movie': movie 
		} )

def movie_content(request, movie_id, slug):
	#content = "This site use to display the detail of %s's movie!!"
	movie = get_object_or_404(MovieProduct,
		id=movie_id,
		slug=slug,
		available=True)

	return render(request,
		'movieRent/templates/detail.html')

