from flask import Blueprint, redirect, url_for, render_template, request,flash
from flask_login import login_user, current_user, logout_user
from werkzeug.urls import url_parse
from scripts.user import *

auth = Blueprint('auth', __name__)


# Redirect
# @auth.route('/login')
# def login():
#     return render_template('signin.html')


# Display page for sign-up
# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('page.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User().get_by_email(email=login_form.email.data)
        if user is not None and User.check_password(hashed_password=user["password"], password=login_form.password.data):
            user_obj = User(email=user["email"], first_name=user['first_name'], last_name=user['last_name'], id=str(user['_id']))
            login_user(user_obj)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('page.index')
            return redirect(next_page)
        else:
            flash("Invalid username or password")

    return render_template('signin.html', title='Sign In', form=login_form) 

# Add new user
@auth.route('/signup', methods=['GET', 'POST'])
def new_user():

    if current_user.is_authenticated:

        return redirect(url_for('page.index'))

    form = RegistrationForm()

    # print(form.email.data)
    if form.validate_on_submit():
        user = User(first_name = form.first_name.data,last_name = form.last_name.data, email=form.email.data, password=form.password.data)
        # Hashing the password here
        user.set_password(password=form.password.data)
        # Saving into database
        user.register()
        flash('Your are now a registered user!')
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html', form = form, title = 'Sign Up')
    

# API for logging out
@auth.route('/sign-out')
def signout():
    logout_user()
    return redirect(url_for('auth.login'))
