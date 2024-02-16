

---

# Flask Disaster Tweet Prediction Project

This project aims to develop a Flask web application for predicting whether a tweet is about a disaster or not. The application uses a machine learning model trained on a dataset of tweets.

## Folder Structure

The repository contains the following folder structure:

```
ML_ScikitLearn/
│
├── app.py                   # Flask application file
│
├── dataset/                 # Folder containing dataset files
│   ├── train.csv            # Training dataset file
│   └── test.csv             # Testing dataset file
│
├── feature_engineering/     # Folder for feature engineering
│   └── __init__.py          # File to mark the directory as a Python package
│
├── processing/              # Folder for data processing scripts and models
│   ├── data_process.py      # Script for data preprocessing
│   ├── text_token.py        # Script for tokenizing text data
│   ├── training.py          # Script for model training
│   ├── tfidf_vectorizer.pkl # Pre-trained TF-IDF vectorizer model
│   └── logistic_regression_model.pkl # Pre-trained logistic regression model
│
└── templates/                # Folder containing HTML templates for the web application
    └── index.html           # HTML template for the home page
```

## Running the Flask Application

To run the Flask application, follow these steps:

1. Ensure Python and Flask are installed on your system.
2. Navigate to the `ML_ScikitLearn` directory in your terminal.
3. Run the `app.py` file using the command `python app.py`.
4. Open a web browser and navigate to `http://127.0.0.1:5000` to access the application.

## How It Works

The Flask application allows users to input a tweet, which is then processed and passed through a machine learning model trained on the provided dataset. The model predicts whether the tweet is about a disaster or not, and the result is displayed on the web page.

---