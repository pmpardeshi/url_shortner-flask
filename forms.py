from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError, URL
from wtforms.fields.html5 import URLField

class URL_shortner_form(FlaskForm):
	website = URLField("website url",validators=[DataRequired(), URL()])
	short_name = StringField("Short name", validators=[DataRequired()])
	submit = SubmitField("Create Link")
	