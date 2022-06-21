from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Post(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=120)])
    body = TextAreaField('Your body here.. ', validators=[DataRequired(), Length(min=1, max=255)])
    submit = SubmitField('Submit')