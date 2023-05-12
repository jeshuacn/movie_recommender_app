
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
import ast

import movie_data

# Model preprocessing functions

# Define the stopwords to be removed
stop_words = set(stopwords.words('english'))

# Define the blacklist words to be removed
blacklist_words = set(['id', 'name', 'nan'])

# Define the tokenizer to remove punctuations
tokenizer = RegexpTokenizer(r'\w+')

def clean_description(description):

    """
    Remove punctuations, numbers and stopwords from description. Additionally set description to lowercase.

    Parameters:
    -----------
        movie_name(str): Movie name.

    Returns:
    --------
        clean_description(list): List of words in the description after removing puntuations, numbers, stopwords
        and setting the text to lowercase.
    """

    # Lowercase the text
    description = description.lower()

    # Tokenize the text and remove stopwords and blacklist words
    description_tokens = tokenizer.tokenize(description)
    description_tokens = [token for token in description_tokens if token not in stop_words and token not in blacklist_words]

    # Remove numbers
    description_tokens = [re.sub(r'\d+', '', token) for token in description_tokens]

    # Join the tokens back to form a string
    description = ' '.join(description_tokens)

    # Remove punctuations
    description = tokenizer.tokenize(description)
    description = ' '.join(description)

    return description

import movie_data
import ast
def new_movie(movie_name):

    """
    Get the concatenated desciption for 

    Parameters:
    -----------
        movie_name(str): Movie name.

    Returns:
    --------
        clean_description(list): List of words in the description after removing puntuations, numbers, stopwords
        and setting the text to lowercase.
    """

    new_movie = movie_data.tmdb_search(movie_name)
    movie_keywords = movie_data.get_movie_data(movie_name)['keywords']

    parsed_pruduction_companies = str(new_movie['production_companies']).replace("'","\"")
        
    production_companies = ast.literal_eval(parsed_pruduction_companies)
    production_companies = [company['name'] for company in production_companies]
    
    new_description = str(movie_keywords) + str(new_movie['genres']) + str(new_movie['original_language']) +\
                        str(production_companies) + str(new_movie['tagline']) + str(new_movie['overview'])


    return clean_description(new_description).split()

