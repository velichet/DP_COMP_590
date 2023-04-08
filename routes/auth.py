from routes.db import mongo
from flask import Blueprint, redirect, url_for

auth = Blueprint('auth', __name__)

# Redirect
@auth.route('/')
def redirect():
    if(False):
        return redirect(url_for('page.home'))
    else:
        return redirect(url_for('auth.signin'))

# Sign in to account
@auth.route('/signin', methods = ['POST'])
def signin():
    return redirect(url_for('page.index'))

# Sign up for account
@auth.route('/signiup', methods = ['POST'])
def signup():
    return