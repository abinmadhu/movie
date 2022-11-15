from django.shortcuts import render, redirect

from home.form import MovieForm
from .models import Movie
# Create your views here.


def update(request, movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST or None,request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST or None, instance=movie)
        return render(request, 'update.html', {'movie': movie, 'form': form})


def delete(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    movie.delete()
    return redirect('/')


def edit_movies(request, movie_id):
    m = Movie.objects.get(pk=movie_id)
    movie = Movie.objects.all()
    return render(request, 'edit.html', {'m': m, 'movie': movie})


def home(request):
    movie = Movie.objects.all()
    return render(request, 'home.html', {'movie': movie})


def add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = MovieForm()
        return render(request, "add.html", {"form": form})
