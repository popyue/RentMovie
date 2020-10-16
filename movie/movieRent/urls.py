from django.urls import path
from . import views

app_name = 'movieRent'

urlpatterns = [
	path('', views.index, name='index'),
	path('home/', views.index, name='index'),
	path('home/<slug:category_slug>/', views.index, name='movie_list_by_category'),
	path('movie/<int:movie_id>/<slug:slug>/', views.movie_content, name='movie_content'),
	path('searchbar/', views.searchbar, name='searchbar'),
]