# Movie Recommender using Word Embeddings
-----------------------------------------------

Welcome to the Movie Recommendation App! This app is designed to help users discover new movies and tv-shows based recommendations using word embedding.

Movies/TV-Shows recommendations using [Gensim](https://radimrehurek.com/gensim/) library and based on features extracted containing description or information about the movie in text format we stimate the word embeddings for each word in the description using [Gensim](https://radimrehurek.com/gensim/) and based on the cosine similarity between the similar description we built a recommendation algorithm.

Recommended movies are from 2017 and before due to the information available in the database. The app will be automatically updated weekly as more recent movies are incorporated into the search.

# Data Collection
-----------------------------------------------
The data was obtained from [The movie dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) from Kaggle. The dataset contains metadata for 45,000 movies listed in the Full MovieLens Dataset. The dataset consists of movies released on or before July 2017.

This dataset consists of the following files:

movies_metadata.csv: This is the main Movies Metadata file. It contains information about 45,000 movies featured in the Full MovieLens dataset.
The features of the `movies_metadata.csv` include:
* genres
* overview
* tagline
* posters
* backdrops
* budget
* review
* release dates
* languages
* production countries
* production companies

keywords.csv: Contains the movie plot keywords for MovieLens movies.

credits.csv: Consists of Cast and Crew Information for the movies.

links.csv: The file that contains the TMDB and IMDB IDs of all the movies featured in the Full MovieLens dataset.

links_small.csv: Contains the TMDB and IMDB IDs of a small subset of 9,000 movies of the Full Dataset.

ratings_small.csv: The subset of 100,000 ratings from 700 users on 9,000 movies.

**Licence**:  [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

For this project the movies_metadata.csv and keywords.csv files were used.

# Model 
------------------------------------------------------------------------------
Used the Word2vec technique for generating word embeddings for the movie descriptions. Word2vec is a neural network-based technique that learns high-quality distributed vector representations of words from large amounts of text data.

To train our Word2vec model, we used the [gensim](https://radimrehurek.com/gensim/) library. The gensim implementation provides an efficient implementation of the skip-gram and continuous bag of words (CBOW) models. We used the Word2Vec algorithm with skip-gram architecture to train our word embeddings. Skip-gram aims to predict the context words given a target word, and it has been shown to work well with large datasets and in capturing semantic relationships between words. We used the Gensim library to train our model on the movie descriptions and other metadata.

The hyperparameters for the Word2vec model were set as follows:

sg: 1
Vector size: 300
Window size: 5
Minimum word count: 3
Seed: 14

Overall, the Word2vec model was trained to generate high-quality word embeddings that could capture the semantic and syntactic relationships between words in the movie descriptions. These word embeddings were then used to calculate the cosine similarity between the movie descriptions and generate movie recommendations.
 
# Deployment
--------------------------------------------------------------------------------
App was deployed using Streamlit.io community cloud. [Website](link).

# How to Run the App
----------------------------------------------------------------------------------
To run the app localy, follow these steps:

1- Download the required paackages by running the following command in your terminal:
  pip install -r requirements.txt
 
2- Get the TMDB API key to retrieve the movie posters and trailers URLs from the TMDB API. You can get one for free by creating an account on [TMDB](https://www.themoviedb.org/) and navigating to your account settins. Copy your API key and store it in the `.env` file unther the **'TMDB_KEY'** variable.

3- Create an account on [Deta Space](https://deta.space/) and get a Base API key to store new movie information in a database. Copy your Base API key and store it in the `.env` file under the **'DETA_KEY'** variable.

4- Choose an image file to use as the background of the app. The file path of the image can be passed to the `settings.add_bg_from_local` function in the **'SETTINGS'** section in the `movie_recommender.py` file to set it as the background.

5- Once you have all the requirements, launch the app by running the following command in your terminal: streamlit run <your_path>/movie_recommender.py

 Replace **<your_path>** with the file path to the Python file containing the app code.


# App features:
----------------------------------------------------------------------------------
The app has the ability to update itselfe. Everytime a new movie is seached that was not previously present in the database, that new movie/tv-show will be recorded in a [Deta.space](https://deta.space/) Base database with its title, description and the description average word embedding vector to then update the dataframe with a github action that will be triggered weekly.

The movie poster's and trailer's URLs are retreived from the TMDB API ![image](https://github.com/jeshuacn/movie_recommender_app/assets/33787097/c3984046-7c1d-4f14-b41e-7be458b0768f)
If the poster and/or the trailer URL is not available on TMDB the app gets the poster URL from IMDB API and the app will perform a youtube search to get the trailer URL.

<img src="https://github.com/jeshuacn/movie_recommender_app/assets/33787097/c3984046-7c1d-4f14-b41e-7be458b0768f" width="30%" height="25%">

## Recommendation Examples:

# License
----------------------------------------------------
This project is licensed under the [MIT License](https://opensource.org/license/mit/)
