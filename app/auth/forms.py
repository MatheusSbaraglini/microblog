"""login form"""
from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email


class LoginForm(Form):
    """ Login form with wtforms"""

    email = TextField('Email Addres', [Email(),
                                       Required(message='Forgot your email addres?')])

    password = PasswordField('Password', [Required(message='Must provide a password.')])
