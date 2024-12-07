from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie


def home(request):
    return render(request, 'index.html')

def movie_list(request):
    movies = Movie.objects.all()
    ctx = {'movies': movies}
    return render(request, 'movies/movie-list.html', ctx)

def movie_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        if title and director and release_year and genre:
            Movie.objects.create(
                title=title,
                director=director,
                release_year=release_year,
                genre=genre,
            )
            return redirect('movies:list')
    return render(request, 'movies/movie-form.html')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    ctx = {'movie': movie}
    return render(request, 'movies/movie-detail.html', ctx)

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        release_year = request.POST.get('release_year')
        genre = request.POST.get('genre')
        if title and director and release_year and genre:
            movie.title=title
            movie.director=director
            movie.release_year=release_year
            movie.genre=genre
            movie.save()
            return redirect(movie.get_detail_url())
    ctx = {'movie': movie}
    return render(request, 'movies/movie-form.html', ctx)

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:list')


