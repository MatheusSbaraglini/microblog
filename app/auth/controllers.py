""" controller """
from flask import Blueprint, request, render_template
from flask import flash, session, redirect, url_for

from werkzeug.security import check_password_hash

from .forms import LoginForm
from .models import User


MOD_AUTH = Blueprint('auth', __name__, url_prefix='/auth')


@MOD_AUTH.route('/signin/', methods=['GET', 'POST'])
def signin():
    """login"""

    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.id
            flash('Welcome %s' % user.name)
            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)
