from routes.db import mongo
from flask import Blueprint, redirect, url_for, render_template, request,flash
from flask_login import login_user,current_user ,logout_user
from werkzeug.urls import url_parse
from scripts.user import *
from routes.login import login_manager

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(email):
    user = User().get_by_email(email)
    if not user:
        return None
    return User(email=user["email"])

# Redirect
@auth.route('/')
def landing_page():
    if(False): # IF USER IS SIGNED IN GOTO HOME PAGE
        return redirect(url_for('page.home'))
    else: # ELSE GOTO SIGNIN PAGE
        return redirect(url_for('auth.signin'))


# Display page for sign-up
@auth.route('/sign-up')
def signup():
    return render_template('signup.html')


@auth.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('page.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = User().get_by_email(email=login_form.Email.data)
        if email is not None and User.check_password(hashed_password=email["password"], password=login_form.password.data):
            user_obj = User(email=email["email"])
            login_user(user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('page.index')
            return redirect(next_page)
        else:
            flash("Invalid username or password")

    return render_template('signin.html', title='Sign In', login_form=login_form) 

# Add new user
@auth.route('/new-user')
def new_user():

    if current_user.is_authenticated:

        return redirect(url_for('page.index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(firstName = form.firstName.data,lastName = form.lastName.data, email=form.Email.data, password=form.password.data)
        # Hashing the password here
        user.set_password(password=form.password.data)
        # Saving into database
        user.register()
        flash('Your are now a registered user!')
        return redirect(url_for('auth.login'))

# API for logging out
@auth.route('/sign-out')
def signout():
    logout_user()
    return render_template('signin.html')
