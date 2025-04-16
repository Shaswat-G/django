from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre


def index(request): #takes in a request and returns a response
    movies = Movie.objects.all() # SELECT * FROM movies_movie
    movie_titles = ", ".join([m.title for m in movies]) # returns a string of all movie titles
    genres = Genre.objects.all() # SELECT * FROM movies_genre
    movie = Movie.objects.get(id=1)
    output = f"{movie_titles} <br> {movie.title} <br> {movie.description} <br> {movie.release_date} <br> {movie.genre.name} <br>"
    # return HttpResponse(f"Hello, world. You're at the movies index.{output}") #returns a simple response with a string
    return render(request, 'index.html', {'movies': movie_titles})

# Create your views here.
