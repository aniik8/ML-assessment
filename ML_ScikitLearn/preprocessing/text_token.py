"""
This file consist of the functions that are used for data converting into 
tokens and removing the stop words and puncuation
"""
import re
from nltk.corpus import stopwords
from data_process import read_data
from nltk.tokenize import word_tokenize
#nltk.download('punkt')
train_data, test_data = read_data()


def clean_text():
    """
    This function is used for word preprocessing - removing special symbols using regular
    expressions, converting them to lower case
    """
    train_data['combined_text'] = train_data['combined_text'].apply(lambda x:
                                                    re.sub(r"'", "", str(x)))
    train_data['combined_text'] = train_data['combined_text'].apply(lambda x:
                                                    re.sub(r'[^a-zA-Z]', ' ', str(x)))
    train_data['combined_text'] = train_data['combined_text'].apply(lambda x:
                                                    re.sub(r'\s+', ' ', str(x)))

    test_data['combined_text'] = train_data['combined_text'].apply(lambda x:
                                                    re.sub(r"'", "", str(x)))
    test_data['combined_text'] = train_data['combined_text'].apply(lambda x:
                                                    re.sub(r'[^a-zA-Z]', ' ', str(x)))
    test_data['combined_text'] = train_data['combined_text'].apply(lambda x:
                                                    re.sub(r'\s+', ' ', str(x)))

    train_data['combined_text']= train_data['combined_text'].apply(remove_stopwords)
    test_data['combined_text'] = test_data['combined_text'].apply(remove_stopwords)
    return train_data, test_data

def remove_stopwords(text):
    """
    This function will remove the stopwords from the cleaned processed data.
    The above function calling this function and sending data in the form of text.
    """
    # Tokenize the text
    stop_words = set(stopwords.words('english'))
    words = text.split()
    # Remove stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]
    # Join the filtered words back into a string
    return ' '.join(filtered_words)

def tokenize_tweet():
    """
    This function will convert the text to the specific tokens (to individual words)
    """
    clean_text()
    train_data['tokens'] = train_data['combined_text'].apply(lambda x: word_tokenize(x))
    test_data['tokens'] = test_data['combined_text'].apply(lambda x: word_tokenize(x))