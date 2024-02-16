# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from flask import render_template
import joblib
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/', methods=['GET'])
# ‘/’ URL is bound with render_html() function.
def render_html():
	"""This function renders the homepage template"""
	return render_template("homepage.html")

@app.route('/result', methods=['POST'])
def get_data():
	"""
	Here we take the input from the respective frontend in the form of string and 
	convert them to the list of inputs
	"""
	tweet = request.form['tweetText']
	keyword = request.form['keyword']
	location = request.form['location']
	y_pred = prediction(list((tweet, keyword, location)))
	#checking if 1 is in the prediction list 
	if 1 in y_pred:
		return render_template("homepage.html", prediction = "Yes the tweet is related to Disaster")
	else:
		return render_template("homepage.html", prediction="No, the tweet isn't about disaster")

def prediction(combined_text):
	"""
Predicts if a given combined text represents a disaster tweet using a pre-trained model.
Parameters - combined_text (str): The combined text of a tweet containing 
information like location, keyword, and tweet text.
Returns:- y_pred (array): Predicted labels 
indicating whether the tweet is classified as a disaster (1) or not (0).
    """
   
	# Load the pre-trained TF-IDF vectorizer and logistic regression model
	vectorizer = joblib.load('./preprocessing/saved_model/tfidf_vectorizer.pkl')
	model = joblib.load('./preprocessing/saved_model/logistic_regression_model.pkl')
	vectorized_new = vectorizer.transform(combined_text)
	y_pred = model.predict(vectorized_new)
	return y_pred

	
# prediction is going maybe wrong
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
