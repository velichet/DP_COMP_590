from flask import Blueprint, render_template, redirect, url_for
from routes.db import mongo
from flask_login import current_user, login_required
from bson import ObjectId

page = Blueprint('page', __name__)

@page.route('/')
def landing_page():
    if current_user.is_authenticated:
        return redirect(url_for('page.index'))
    else:
        return redirect(url_for('auth.login'))

# Base API to return home page
@page.route('/home')
@login_required
def index():
    return render_template('index.html')

# About page
@page.route('/resources')
@login_required
def resources():
    return render_template('resources.html')

# Retrieve all data stat sets from the database
@page.route('/gallery', methods=['GET'])
@login_required
def gallery():

    # Connect to mongo stats collcetion
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    stats = datastats_collection.find()

    return render_template('gallery.html', stats = stats)

# Display MyData page
@page.route('/mydata')
@login_required
def mydata():

    # Connect to mongo stats collcetion
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    # Get signed in users datasets
    user_id = ObjectId(current_user.id)
    stats = datastats_collection.find({"user_id": user_id})

    name = current_user.first_name + " " + current_user.last_name
    email = current_user.email

    return render_template('mydata.html', stats = stats, name = name, email = email)

# Display Upload page for global
@page.route('/upload-global')
@login_required
def upload_page_global():
    return render_template('uploadglobal.html')

# Display Upload page for local
@page.route('/upload-local')
@login_required
def upload_page_local():
    return render_template('uploadlocal.html')