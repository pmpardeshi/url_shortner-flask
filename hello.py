from flask import Flask

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
	returtn "hello world"


@app.route('/about')
def about():
	return "this is a url shortner"