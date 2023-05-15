
# word embedding using Gesim
import warnings
import re
import nltk
nltk.download('stopwords')
from gensim.models import Word2Vec

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

warnings.filterwarnings('ignore')


# Loading model
model = Word2Vec.load("model/word2vec.model")

# Loading dataframe
df = pd.read_pickle('data/avg_movies_desc_vectors.pkl')

# getting all average word vectors into an numpy array
df['avg_description_vector'] = df['avg_description_vector'].apply(np.array)
avg_desc_vector_all = np.array(df['avg_description_vector'].to_list())


# Cousine similarity
def similarity_scores(movie, df=df, avg_desc_vector_all=avg_desc_vector_all):
    """
    Gets the similarity scores between the movie and all of the movies in the dataframe.
    
    Parameters:
    -----------
        movie (str): Title of the Movie
        df(DataFrame): DataFrame containing Movie title and Movie Description
        avg_movie_vector_all(numpy array): Average embeddings of all of the Movie Descriptions

    Returns:
    --------
        list: List with similarity scores between the movie and all of the movies in the dataframe
    """
 
    movie_index = df.loc[df.title == movie].index[0]
    movie_avg_desc_vector = df.loc[movie_index,'avg_description_vector']
 
    cosine_similarities =cosine_similarity([movie_avg_desc_vector],avg_desc_vector_all)

    
    return cosine_similarities



# Returns top 5 recommendations based on the cosine similarity
def recommendations(movie, df=df):
    """
    Recommending the top 10 similar movies.

    Parameters:
    -----------
        movie (str): Title of the Movie
        df (DataFrame): DataFrame containing Movie title and Movie Description

    Returns:
    --------
        list: List of top 20 similar Movie title
    """
    cosine_similarities = similarity_scores(movie)

    similarities_scores = list(enumerate(cosine_similarities.squeeze().tolist()))  # index and vector values of cosine similarities
    sorted_similarities_scores = sorted(similarities_scores, key = lambda x: x[1], reverse = True) # sorted in descending order of index and vector values of cosine similarities
    top5_sim_scores = sorted_similarities_scores[1:21] # top 10 indices and similarity scores
    top5_movie_indices = [index for index, score in top5_sim_scores] # top 5 movie indices
    #top5_movie_scores = [score for index, score in top5_sim_scores] # top 5 movie scores
    top5_movie_titles = df.iloc[top5_movie_indices]['title'].tolist() # top 5 movie titles
    
    return list(top5_movie_titles) 


# Averaging Word Embeddings of all of the Words in the Description
def avg_desc_vector(df, model, desc_col):
    """
    Given a dataframe, a pre-trained Word2Vec model, and a column containing descriptions, calculates the
    averaged vector of all of the words in the description, where each word is in the vocab of the word embeddings
    i.e if the word is in `model.wv.vocab.keys()`.
    If there are only words in the descriptions which are not in the vocab of the word embeddings, assigns them to
    array of zeros of 300 dims. i.e (300, )
    
    Parameters:
    -----------
    df (pandas DataFrame): The input dataframe
    model (gensim.models.word2vec.Word2Vec): The pre-trained Word2Vec model
    desc_col (str) : The name of the column containing the descriptions
    
    Returns:
    --------
    pandas DataFrame: A new dataframe with an additional column `avg_description_vector` containing the averaged word vectors for
                      each description
    """
    
    def get_avg_vec(desc):
        """
        Helper function that takes in a string `desc`, calculates the averaged vector of all of the words in the
        description, where each word is in the vocab of the word embeddings i.e if the word is in `model.wv.vocab.keys()`.
        If there are only words in the descriptions which are not in the vocab of the word embeddings, assigns them
        to array of zeros of 300 dims. i.e (300, )
        
        Parameters:
        -----------
        desc (str): The input description
        
        Returns:
        --------
        numpy.ndarray: The averaged vector of all of the words in the description
        """
        vecs = []
        for word in desc:
            if word in model.wv.key_to_index.keys():
                vecs.append(model.wv[word])
        if vecs:
            return np.mean(vecs, axis=0)
        else:
            return np.zeros(300)
        
    df = df.copy()
    df['avg_description_vector'] = df[desc_col].apply(get_avg_vec)
    return df


def new_movie_avg_desc_vector(new_movie_desc):

    """
        Calculates the averaged vector of all of the words in the
        description, where each word is in the vocab of the word embeddings i.e if the word is in `model.wv.vocab.keys()`.
        If there are only words in the descriptions which are not in the vocab of the word embeddings, assigns them
        to array of zeros of 300 dims. i.e (300, )
        
        Parameters:
        -----------
        new_movie_desc (str): The input description
        
        Returns:
        --------
        numpy.ndarray: The averaged vector of all of the words in the description
        """
    vecs = []
    for word in new_movie_desc:
        if word in model.wv.key_to_index.keys():
            vecs.append(model.wv[word])
    if vecs:
        return np.mean(vecs, axis=0)
    else:
        return np.zeros(300)



def new_movie_recommendation(movie_avg_desc_vector,avg_desc_vector_all=avg_desc_vector_all,df=df):  

    """
        Gets the top 20 indices and similarity scores to extract the recommendations.

        Parameters:
        -----------
            movie_avg_desc_vector (numpy array): Averaged vector of all of the words in the description
            avg_desc_vector_all (numpy array): Average embeddings of all of the Movie Descriptions

        Returns:
        --------
        list: List of top 20 similar Movie titles

    """  
    
    cosine_similarities =cosine_similarity([movie_avg_desc_vector],avg_desc_vector_all)
       
    similarities_scores = list(enumerate(cosine_similarities.squeeze().tolist()))  # index and vector values of cosine similarities
    sorted_similarities_scores = sorted(similarities_scores, key = lambda x: x[1], reverse = True) # sorted in descending order of index and vector values of cosine similarities
    top5_sim_scores = sorted_similarities_scores[1:21] # top 20 indices and similarity scores
    top5_movie_indices = [index for index, score in top5_sim_scores] # top 5 movie indices
    #top5_movie_scores = [score for index, score in top5_sim_scores] # top 5 movie scores
    top5_movie_titles = df.iloc[top5_movie_indices]['title'].tolist() # top 5 movie titles
    
    return list(top5_movie_titles) 
