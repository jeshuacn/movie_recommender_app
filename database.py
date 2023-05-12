import os

from deta import Deta
#from dotenv import load_dotenv

# Load environment variables
#load_dotenv('.env')
DETA_KEY = os.getenv("DETA_KEY")


# Initialize with a database key
deta = Deta(DETA_KEY)

# Connect to database
db = deta.Base('movies_data')
db2 = deta.Base('movie_search_history') 

def insert_data(title, description, avg_description_vector,date):
    '''Returns the movie data on a successful creation'''

    db2.put({'key':title,
                   'description':description,
                   'avg_description_vector':avg_description_vector,
                   'input_date':date
                   })
    return db.put({'key':title,
                   'description':description,
                   'avg_description_vector':avg_description_vector,
                   'input_date':date
                   })

def fetch_movies():
    '''Returns a dict of all movie data'''

    res = db.fetch()
    return res.items

def get_movie(movie_name):
    '''get specific movie, if not found return None'''
    return db.get(movie_name)

def get_all_movies():
    items = fetch_movies()
    movies = [item['key'] for item in items]

    return movies

def remove_movies():
    '''Remove movies after updating df'''
    movies = get_all_movies()
    for movie in movies:
        db.delete(movie)
