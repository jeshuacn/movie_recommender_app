# Movie Recommender using Word Embeddings

[![Go to WebPage]](https://moviematch.streamlit.app/)  

[Go to WebPage]: https://img.shields.io/badge/Notebook-informational?style=for-the-badge


![](images/MovieMatch.gif)

Are you tired of endlessly scrolling through streaming platforms, trying to find your next favorite movie or TV show? With MovieMatch that won’t be a problem anymore! Welcome to this amazing app where you can easily discover new titles that are tailored to your personal taste. With our movie recommendation algorithm, you can discover by simply input the name of a movie or TV show that you love, and we'll recommend the top 20 similar titles for you to check out. Our app uses advanced word embedding techniques to analyze the plot and themes of each title, ensuring that our recommendations are as accurate and relevant as possible. So, sit back, relax, and let us help you discover your next favorite flick!

Movies/TV-Shows recommendations using [Gensim](https://radimrehurek.com/gensim/) library and based on features extracted containing the description or information about the movie in text format we estimate the word embeddings for each word in the description using [Gensim](https://radimrehurek.com/gensim/) and based on the cosine similarity between the similar description, we built a recommendation algorithm.

Recommended movies are from 2017 and before due to the information available in the database. The app will be automatically updated weekly as more recent movies are incorporated into the search.

# Data Collection

The data was obtained from [The movie dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset) from Kaggle. The dataset contains metadata for 45,000 movies listed in the Full MovieLens Dataset. The dataset consists of films released on or before July 2017.

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

For this project, I used the movies_metadata.csv and keywords.csv files.

# Model 

I used the Word2vec technique for generating word embeddings for the movie descriptions. Word2vec is a neural network-based technique that learns high-quality distributed vector representations of words from large amounts of text data.

To train the Word2vec model, I used the [gensim](https://radimrehurek.com/gensim/) library. The gensim implementation efficiently implements the skip-gram and continuous bag of words (CBOW) models. I used the Word2Vec algorithm with skip-gram architecture to train the word embeddings. Skip-gram aims to predict the context words given a target word, and it has been shown to work well with large datasets and capture semantic relationships between words. I used the Gensim library to train our model on the movie descriptions and other metadata.

The hyperparameters for the Word2vec model were set as follows:

sg: 1

Vector size: 300

Window size: 5

Minimum word count: 3

Seed: 14

Overall, the Word2vec model was trained to generate high-quality word embeddings that could capture the semantic and syntactic relationships between words in the movie descriptions. These word embeddings were then used to calculate the cosine similarity between the movie descriptions and generate movie recommendations.
 
# Deployment

The app was deployed using the Streamlit.io community cloud. [Go to MovieMatch](https://moviematch.streamlit.app/).

## How to Run the App

To run the app locally, follow these steps:

1- Download the required packages by running the following command in your terminal:
  pip install -r requirements.txt
 
2- Get the TMDB API key to retrieve the movie posters and trailer URLs from the TMDB API. You can get one for free by creating an account on [TMDB](https://www.themoviedb.org/) and navigating to your account settings. Copy your API key and store it in the `.env` file under the **'TMDB_KEY'** variable.

3- Create an account on [Deta Space](https://deta.space/) and get a Base API key to store new movie information in a database. Copy your Base API key and store it in the `.env` file under the **'DETA_KEY'** variable.

4- Choose an image file to use as the app's background. The file path of the image can be passed to the `settings.add_bg_from_local` function in the **'SETTINGS'** section in the `movie_recommender.py` file to set it as the background.

5- Once you have all the requirements, launch the app by running the following command in your terminal: `streamlit run <your_path>/movie_recommender.py`

 Replace **<your_path>** with the file path to the Python file containing the app code.


# App features:

The app can update itself. Every time a new movie/tv-show is searched that was not previously present in the database, will be recorded in a [Deta.space](https://deta.space/) Base database with its title, description and the description average word embedding vector to then update the dataframe with a Github action that will be triggered weekly.

The movie poster's and trailer's URLs are retrieved from the TMDB API.

If the poster or trailer URL is unavailable on TMDB, the app gets the poster URL from IMDB API and will perform a youtube search to get the trailer URL.


<img src="https://github.com/jeshuacn/movie_recommender_app/assets/33787097/b4159afb-eeea-4c39-87a1-c54b74a59941" width="10%" height="10%">

## Recommendation Examples:

![image](https://github.com/jeshuacn/movie_recommender_app/assets/33787097/fc033365-69c2-44d6-9483-65c99d1baa10)
![image](https://github.com/jeshuacn/movie_recommender_app/assets/33787097/566be596-f819-4d59-9a4d-6b68b3ec1458)
![image](https://github.com/jeshuacn/movie_recommender_app/assets/33787097/0d44c337-77c0-4ceb-a1f8-b13657da857e)

# License
This project is licensed under the [MIT License](https://opensource.org/license/mit/)
