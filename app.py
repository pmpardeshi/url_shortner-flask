from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def index():
	return "hello world"


@app.route('/about')
def about():
	return "this is a url shortner website"


