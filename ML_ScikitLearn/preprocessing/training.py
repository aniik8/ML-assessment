from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from text_token import train_data, test_data, tokenize_tweet, clean_text
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

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
    model = LogisticRegression()
    test_accuracy = model.fit(X, y)
    joblib.dump(model, 'logistic_regression_model.pkl')

# Model Evaluation
    accuracy = model.score(X, y)
    print("Training Accuracy:", accuracy)
    testing_model(accuracy)

def testing_model(test_accuracy):
    # Test the trained model on new data
    # Load the trained TF-IDF vectorizer and model
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    model = joblib.load('logistic_regression_model.pkl')
    X_new = vectorizer.transform(test_data['combined_text'])
    y_pred = model.predict(X_new)
    print(" the accuracy of this model", accuracy_score( y_pred[:3000], train_data['target'].head(3000)) * 100)
    print("Precision of this model is :", precision_score(y_pred[:3000], train_data['target'].head(3000)) * 100)
    print("f1 score of model is :", f1_score( y_pred[:3000], train_data['target'].head(3000)))
    print("Confusion matrix of model", confusion_matrix( y_pred[:3000], train_data['target'].head(3000)))
    
convert_tokens()
