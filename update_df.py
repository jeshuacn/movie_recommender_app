# Updates dataframe

import database as db
import pandas as pd


df = pd.read_pickle('data/avg_movies_desc_vectors.pkl')

data = db.fetch_movies()

for movie in range(len(data)):

    new_movie = {'title':data[movie]['key'],
                 'description': data[movie]['description'],
                 'avg_description_vector':data[movie]['avg_description_vector']
                 }
    
    df.loc[len(df)] = new_movie


df.to_pickle('data/avg_movies_desc_vectors.pkl')

db.remove_movies()

