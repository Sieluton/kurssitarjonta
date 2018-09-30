from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class SignupForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired(), validators.length(min=2, message='Name too short')])
    username = StringField("Username", [validators.InputRequired(), validators.length(min=2, message='Username too short')])
    password = PasswordField("Password", [validators.InputRequired(),
                                          validators.EqualTo('passwordConfirmation', message='Passwords must match')])
    passwordConfirmation = PasswordField("Repeat Password", [validators.InputRequired()])

    class Meta:
        csrf = False