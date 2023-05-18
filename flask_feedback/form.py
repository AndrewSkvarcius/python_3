from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email


class UserForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    
    password = PasswordField("Password", validators=[InputRequired(), Length(min=6, max=55)])

    email = StringField("Email", validators=[InputRequired(), Length(max=50)])

    first_name = StringField("First Name", validators=[InputRequired(),Length(max=30)])
    
    last_name = StringField("Last Name", validators=[InputRequired(),Length(max=30)])
    
   
class Login(FlaskForm):
    """Login form."""

    username = StringField(
        "Username",
        validators=[InputRequired(), Length(min=1, max=20)],
    )
    password = PasswordField(
        "Password",
        validators=[InputRequired(), Length(min=6, max=55)],
    )
class FeedForm(FlaskForm):
    """Feedback Form"""
    
    title = StringField("Title", validators=[InputRequired(), Length(max=100)])

    content = StringField("Content", validators=[InputRequired(), ])



class Deleted(FlaskForm):
        """blank"""""