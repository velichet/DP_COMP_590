from routes.db import mongo
from flask import Blueprint, redirect, url_for, render_template

auth = Blueprint('auth', __name__)

# Redirect
@auth.route('/')
def landing_page():
    if(False): # IF USER IS SIGNED IN GOTO HOME PAGE
        return redirect(url_for('page.home'))
    else: # ELSE GOTO SIGNIN PAGE
        return redirect(url_for('auth.signin'))

# Display page for sign-in
@auth.route('/sign-in')
def signin():
    return render_template('signin.html')

# Display page for sign-up
@auth.route('/sign-up')
def signup():
    return render_template('signup.html')

# Log in API
@auth.route('/login')
def login():
    # CHANDRA CODE
    return 

# Add new user
@auth.route('/new-user')
def new_user():
    # CHANDRA CODE
    return

# API for logging out
@auth.route('/sign-out')
def signout():
    return