"""
This particular file consist of data preprocessing process.
"""
import pandas as pd
import numpy as np

TRAIN_DATA_PATH = '../dataset/train.csv'
TEST_DATA_PATH = '../dataset/test.csv'

def read_data():
    """ This particular function is used to read the csv file dataset and converting it into 
     the dataset."""
    train_file = pd.read_csv(TRAIN_DATA_PATH)
    test_file = pd.read_csv(TEST_DATA_PATH)
    df_train = pd.DataFrame(train_file)
    df_test = pd.DataFrame(test_file)
    return clean_data(df_train, df_test)


#function for cleaning the data
def clean_data(df_train, df_test):
    """this function performs data cleaning and processing.
    """
    #Here what i did, I filled the null values of columns to ''
    #inplace will make the changes in the actual dataframe
    df_train.fillna('', inplace=True) 
    df_test.fillna('', inplace=True)
    return combine_text(df_train, df_test)

#function to combine the text, all of the three columns into one  
def combine_text(df_train, df_test):
    """
    This function will combine the text of all three columns into one single columns
    that'll help in the training and testing of our model.
    """
    df_train['combined_text'] = df_train['text'] + ' ' + df_train['location'] + ' ' + df_train['keyword']
    df_test['combined_text'] = df_test['text'] + ' ' + df_test['location'] + ' ' + df_test['keyword']
    df_test['combined_text'] = df_test['combined_text'].astype(str)
    df_train['combined_text'] = df_train['combined_text'].astype(str)
    return df_train, df_test
