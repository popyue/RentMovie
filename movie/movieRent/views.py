from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Category, Movie
from cart.forms import CartAddMovieForm
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(request, category_slug=None):
	#return HttpResponse("Hello, world. You're at the Movie Rent Store index.")
	category = None
	categories = Category.objects.all()
	movies = Movie.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		movies = movies.filter(category=category)
	print("request: {}".format(request))
	return render(request, 
		'index.html',
		{ 
		'category' : category,
		'categories': categories,
		'movies': movies
		} )

@csrf_exempt
def movie_content(request, movie_id, slug):
	#content = "This site use to display the detail of %s's movie!!"
	movie = get_object_or_404(Movie,
		id=movie_id,
		slug=slug,
		available=True)
	cart_movie_form = CartAddMovieForm()
	return render(request,
		'movie/detail.html', {'movie': movie,
		'cart_movie_form': cart_movie_form})

@csrf_exempt
def searchbar(request):
	if request.method == 'GET':
		search = request.GET.get('search')
		#movie = Movie.objects.all().filter(movie_name__contains=search)
		movie = Movie.objects.raw("SELECT * FROM MOVIE WHERE movie_name = '%s' " % search)
		print(movie)
		#category = Category.objects.raw('SELECT * FROM MOVIE WHERE category_name LIKE %s' % search )
		
		return render(request, 
			'movie/result_list.html', 
			{
			'movie' : movie
			})

