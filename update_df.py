# Updates dataframe
import os
import database as db
import pandas as pd
from github import Github #pip install PyGithub

df = pd.read_pickle('data/avg_movies_desc_vectors.pkl')


data = db.fetch_movies()

for movie in range(len(data)):

    new_movie = {'title':data[movie]['key'],
                 'description': data[movie]['description'],
                 'avg_description_vector':data[movie]['avg_description_vector']
                 }
    
    df.loc[len(df)] = new_movie


# Authenticate to GitHub using a personal access token
g = Github(os.environ['${{ github.token }}'])

# Get the repository you want to add the file to
repo = g.get_repo('jeshuacn/movie_recommender_app')

# Create the file in the repository
repo.create_file('data/avg_movies_desc_vectors.pkl', 'Updated dataframe', df)


db.remove_movies()
