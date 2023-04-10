from flask import Blueprint, render_template
from routes.db import mongo

page = Blueprint('page', __name__)

# Base API to return home page
@page.route('/home')
def index():
    return render_template('index.html')

# About page
@page.route('/about')
def about():
    return render_template('about.html')

# Retrieve all data stat sets from the database
@page.route('/gallery', methods=['GET'])
def gallery():

    # Connect to mongo stats collcetion
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    stats = datastats_collection.find()

    return render_template('gallery.html', stats = stats)

# Display MyData page
@page.route('/mydata')
def mydata():

    # Connect to mongo stats collcetion
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    # Get signed in users datasets
    user_id = 0 # GET USER ID // THIS IS TEMP
    stats = datastats_collection.find({"user_id": user_id})

    return render_template('mydata.html', stats = stats)

# Display Upload page for global
@page.route('/upload-global')
def upload_page_global():
    return render_template('uploadglobal.html')

# Display Upload page for local
@page.route('/upload-local')
def upload_page_local():
    return render_template('uploadlocal.html')