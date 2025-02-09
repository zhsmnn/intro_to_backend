from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return JsonResponse(list(movies.values()), safe=False)

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    return JsonResponse({
        'title': movie.title,
        'description': movie.description,
        'producer': movie.producer,
        'duration': movie.duration,
    })

def home(request):
    return render(request, 'movie/home.html')