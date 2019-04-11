from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(max=24)])
    password = PasswordField("Password", [validators.Length(max=24)])

    class Meta:
        csrf = False

class Account_CreateForm(FlaskForm):
    username = StringField("Username", [validators.Length(max=24)])
    password = PasswordField("Password"), [validators.Length(max=24)]
    name = StringField("Name", [validators.Length(max=24)])

    class Meta:
        csrf = False