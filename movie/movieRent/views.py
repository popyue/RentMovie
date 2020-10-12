from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, MovieProduct


# Create your views here.
def index(request):
	#return HttpResponse("Hello, world. You're at the Movie Rent Store index.")
	return render(request, 'index.html')

def movie_content(request, movie_id):
	content = "This site use to display the detail of %s's movie!!"
	return HttpResponse(content % movie_id)

def category_content(request, category_id):
	content = "This is a list view for %s's category content"
	return HttpResponse(content % category_id)


def rentcar(request):
	response = "This is the rent car before payment"
	return HttpResponse(response)