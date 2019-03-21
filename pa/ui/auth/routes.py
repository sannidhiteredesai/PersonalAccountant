from flask_login import current_user, login_user, logout_user
from flask import render_template, redirect, url_for, flash
from pa.ui import app
from pa.ui import login_manager
from pa.pa.user import Users, User
from pa.ui.auth.forms import RegistrationForm, LoginForm
from pa.ui.auth.login import LoginUser


@login_manager.unauthorized_handler
def unauthorized_callback():
    flash('Please login before accessing any other pages !!')
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        users = Users()
        user = User(dict(username=form.username.data,
                         password=form.password.data,
                         mobile=form.mobile.data,
                         dob=form.dob.data,
                         question=form.question.data,
                         answer=form.answer.data))
        users.add(user)
        flash('Congratulations, new user registered successfully !!')
        return redirect(url_for('login'))

    return render_template('auth/register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():

        if Users().are_valid_credentials(username=form.username.data, password=form.password.data):
            login_user(LoginUser(username=form.username.data))
            return redirect(url_for('index'))

        flash('Unable to login, invalid username or password !!')
        return redirect(url_for('login'))

    return render_template('auth/login.html', title='Login', form=form)


@app.route('/logout', methods=['GET'])
def logout():
    if current_user.is_authenticated:
        user = current_user.username
        logout_user()
        return render_template('auth/logout.html', user=user)

    return redirect(url_for('login'))
