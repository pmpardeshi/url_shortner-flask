from flask import Flask, render_template, url_for, redirect
from forms import URL_shortner_form

app = Flask(__name__)
app.config['SECRET_KEY']="9OLWxND4o83j4K4iuopO"

# @app.route('/home')
# @app.route('/')
# def index():
# 	return "hello world"


@app.route('/home')
@app.route('/')
def index():
	
	return render_template('home.html')


@app.route('/about')
def about():
	return "this is a url shortner website"


@app.route('/short_ln',methods=['POST','GET'])
def short_ln():
	form = URL_shortner_form()
	if form.validate_on_submit():
		print('validates')
		return redirect(url_for('about'))
	return render_template('short.html',form=form)
