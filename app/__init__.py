""" init"""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import config


APP = Flask(__name__)
APP.config.from_object('config')
DB = SQLAlchemy(APP)

from app.auth.controllers import MOD_AUTH as auth_module


@APP.errorhandler(404)
def not_found():
    """ error handler """
    return render_template('404.html'), 404

# Register blueprint(s)
APP.register_blueprint(auth_module)

DB.create_all()
