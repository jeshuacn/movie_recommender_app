import os
from dotenv import load_dotenv

import streamlit as st
import imdb # pip install imdbpy
from pytube import Search # pip install pytube

#from dotenv import load_dotenv # pip install python-dotenv
from tmdbv3api import TMDb # pip install tmdbv3api
from tmdbv3api import Movie
import requests
import json

# Load environment variables
load_dotenv('.env')

# --------------- IMDB --------------

# create an instance of the IMDb class
imdb_instance = imdb.IMDb()

@st.cache_data
def get_movie_data(movie_name,size = 'full-size cover url'):
    '''Search for movie and retreive movie info'''

    # search for a movie name
    search_results = imdb_instance.search_movie(movie_name)

    # get the first search result (assuming it's the correct movie)
    movie_id = search_results[0].getID()

    # get the movie object for the given movie ID
    movie = imdb_instance.get_movie(movie_id)
    imdb_instance.update(movie,info = ['keywords'])

    # get the movie object cover url
    poster_url  = movie[size]

    return {'keywords':movie['keywords'][:5],'poster_url':poster_url}

@st.cache_data
def get_trailer(movie_name):
    trailers = Search(movie_name + ' Trailer')
    trailer_url = trailers.results[0].watch_url

    return trailer_url


# ------------- TMDB CONFIG -----------------

TMDB_KEY = os.getenv('TMDB_KEY')

tmdb = TMDb()
tmdb.api_key = TMDB_KEY
tmdb.language = 'en'

# ------------- TMBD API---------------

tmdb = Movie()

@st.cache_data
def tmdb_search(movie_name):
    """ Returns movie information, such as: Title, Overview, Taglines, 
        Production companies names, movie language, genres
    """

    search = tmdb.search(movie_name)[0]
    details = tmdb.details(search['id'])

    title = details.title
    overview = details.overview
    taglines = details.tagline
    production_companies = details.production_companies
    language = details.original_language
    genres = details.genres
    
    # movie id from TMdb
    id = search['id']
     
    return {'title':title,
            'overview':overview,
            'tagline':taglines,
            'production_companies':production_companies,
            'original_language':language,
            'genres': genres,
            'poster_url': 'https://image.tmdb.org/t/p/w500/'+details.poster_path,
            'id':id}

@st.cache_data
def tmdb_trailer(movie_name):

    """ Gets the movie name and search for the trailer url on Youtube and return it"""

    # get trailer
    id = tmdb_search(movie_name)['id']
    trailer_response = requests.get(f'https://api.themoviedb.org/3/movie/{id}/videos?api_key={TMDB_KEY}&language=en-US')
    trailer_json = json.loads(trailer_response.text)
    trailer_key = trailer_json['results'][0]['key']

    return (f'https://www.youtube.com/watch?v={trailer_key}')
    

