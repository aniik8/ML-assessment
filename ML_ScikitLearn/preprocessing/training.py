"""
This module is used for training of the model and predicting the accuracy of the model.
also the testing of the model is done in this module and whole accuracy, precision and
f1 score of the model is being displayed 
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from text_token import train_data, test_data, tokenize_tweet
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix

import joblib

def convert_tokens():
    """This function converts the tweet to tokens in a new column"""
    tokenize_tweet()
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(train_data['combined_text'])
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    y = train_data['target']
    training_model(X, y)

def training_model(X, y):
    """
    As the name suggests, this function is used to train the logistic regression model
    and the model is dumped into the file named logistic_regression.pkl
    """
    model = LogisticRegression()
    test_accuracy = model.fit(X, y)
    print(test_accuracy)
    joblib.dump(model, 'logistic_regression_model.pkl')

# Model Evaluation
    accuracy = model.score(X, y)
    print("Training Accuracy:", accuracy)
    testing_model()

def testing_model():
    """
    Test the trained model on new data
    Load the trained TF-IDF vectorizer and model
    """
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('logistic_regression_model.pkl')
    X_new = vectorizer.transform(test_data['combined_text'])
    y_pred = model.predict(X_new)
    print(" the accuracy of this model",
          accuracy_score( y_pred[:3000], train_data['target'].head(3000)) * 100)
    print("Precision of this model is :",
          precision_score(y_pred[:3000], train_data['target'].head(3000)) * 100)
    print("f1 score of model is :",
          f1_score( y_pred[:3000], train_data['target'].head(3000)))
    print("Confusion matrix of model",
          confusion_matrix( y_pred[:3000], train_data['target'].head(3000)))
convert_tokens()
