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

# Sign in to account
@auth.route('/sign-in')
def signin():
    return render_template('signin.html')

# Sign up for account
@auth.route('/sign-up')
def signup():
    return render_template('signup.html')

@auth.route('/sign-out')
def signout():
    return