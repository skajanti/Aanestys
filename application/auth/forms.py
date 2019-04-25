from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(max=24)])
    password = PasswordField("Password", [validators.Length(max=24)])

    class Meta:
        csrf = False

class Account_CreateForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=4, message='Username must be between 4 and 24 characters long.'), validators.Length(max=24, message='Username must be between 4 and 24 characters long.')])
    password = PasswordField("Password", [validators.Length(min=4, message='Password must be between 4 and 24 characters long.'), validators.Length(max=24, message='Password must be between 4 and 24 characters long.')])
    name = StringField("Name", [validators.Length(min=4, message='Name must be between 4 and 24 characters long.'), validators.Length(max=24, message='Name must be between 4 and 24 characters long.')])

    class Meta:
        csrf = False