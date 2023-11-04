import streamlit as st
import numpy as np
from datetime import datetime
from streamlit_player import st_player #pip install streamlit-player

import movie_data
import app_settings as settings
import model
import preprocessing
import database as db

# ----------- SETTINGS -------
title = settings.app_settings()['title']
icon = settings.app_settings()['icon']
layout = settings.app_settings()['layout']
style = settings.app_settings()['style']
hyperlink_settings = settings.app_settings()['hyperlink_settings']

st.set_page_config(page_title=title,page_icon=icon,layout=layout)
st.markdown(style,unsafe_allow_html=True)
st.markdown(hyperlink_settings,unsafe_allow_html=True)

settings.add_bg_from_local('images/back_ground.jpg') 

st.title(title) # Title
st.write('Discover your next favorite flick based on your personal taste. Just input the name of your favorite TV Show or Movie and let us do the rest!')

#--------- SIDEBAR --------------
st.sidebar.title(f'{title} \n \n')
st.sidebar.markdown('### Welcome to MovieMatch, a movie recommendation app!')


with st.sidebar: 
    n = st.number_input('**Select Grid Width:**',1,8,5) # Select number of grid for recommendation posters

with st.sidebar.expander("About the app"):
    st.write("""
        Recommendations are movies from 2017 and before due to the information available in the database. 
        The app will automatically update weekly as more recent films are incorporated into the search.
    """)

# --------------SEARCH COLUMNS ------------
col4,_ = st.columns(2)
col1,_,col2 = st.columns([5,1,4])
data = None

with col1:
    movie_name = st.text_input("Enter a movie name:",placeholder='Movie name..',key ='prueba').title()
    if movie_name: 
        try:
            data = movie_data.tmdb_search(movie_name)
            ''
            ''
            ''
            ''        
            try:
                st_player(movie_data.tmdb_trailer(data['title']),height = 300) # Get trailer from tmdb api if not video fund use IMdb api

            except:
                st_player(movie_data.get_trailer(data['title']),height = 300)
        except:
            st.write('Please enter a valid Movie or TV-Show name')

with col2:
    if data:
        
        st.markdown(f'#### {data["title"]}')
        if data["poster_url"]:
            st.image(data["poster_url"],width=300)

#-------------- GET RECOMMENDATIONS ------------------------------

view_posters = []

if data:
    st.markdown('### Recommendations:')
    try:
        recommend = model.recommendations(data['title'])
        
        # ADD search to history database
        db.add_search_to_history(data['title'],recommend,datetime.today().strftime('%Y-%m-%d'))

    except: # If movie not found in dataframe
        description= preprocessing.new_movie(movie_name) # Get description from new movie and process it
        vect =model.new_movie_avg_desc_vector(description) 
        recommend = model.new_movie_recommendation(vect)
        
        # INSERT data to database
        db.insert_data(data['title'],
                       description,
                       np.ndarray.tolist(vect),
                       datetime.today().strftime('%Y-%m-%d'))
        # ADD search to history database
        db.add_search_to_history(data['title'],recommend,datetime.today().strftime('%Y-%m-%d'))

    # Recomendations will be the model output
    for movie in recommend:
        #st.write(movie)
        view_posters.append(movie)

    # ---------- DISPLAY RECOMMENDATIONS ------------------
    
    groups = []
    # creating grid
    for i in range(0,len(view_posters),n):
        groups.append(view_posters[i:i+n])

    for group in groups:
        cols = st.columns(n)
        for i, movie in enumerate(group):

            try:
                try:
                    cols[i].image(movie_data.tmdb_search(movie)['poster_url']) # Seach movie poster on TMDb     

                except:
                    cols[i].image(movie_data.get_movie_data(movie)["poster_url"]) # If movie not found seach on IMDb
            except:
                cols[i].image('https://upload.wikimedia.org/wikipedia/commons/c/c2/No_image_poster.png') # If no movie poster URL found, show default "no image" poster
                
            with cols[i]:
              
                try:
                    st.markdown(f"[{movie}]({movie_data.tmdb_trailer(movie)})")
                except:
                    st.write(f"[{movie}]({movie_data.get_trailer(movie)})")
    


