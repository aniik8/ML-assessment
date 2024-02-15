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
	"""this is the simple function to display hello world"""
	return render_template("homepage.html")

@app.route('/result', methods=['POST'])
def get_data():
	tweet = request.form['tweetText']
	keyword = request.form['keyword']
	location = request.form['location']
	y_pred = prediction(list((tweet, keyword, location)))
	print(y_pred)
	if 1 in y_pred:
		return render_template("homepage.html", prediction = "Yes the tweet is related to Disaster")
	else:
		return render_template("homepage.html", prediction="No, the tweet isn't about disaster")

def prediction(combined_text):
	print(type(combined_text))
	print(combined_text)
	vectorizer = joblib.load('./preprocessing/tfidf_vectorizer.pkl')
	model = joblib.load('./preprocessing/logistic_regression_model.pkl')
	X_new = vectorizer.transform(combined_text)
	y_pred = model.predict(X_new)
	return y_pred

	
# prediction is going maybe wrong
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application 
	# on the local development server.
	app.run()
