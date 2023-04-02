from flask import Blueprint, render_template, request, Response
from scripts.driver.format import csv_format
from scripts.driver.global_driver import driver_global_algo
from bson.objectid import ObjectId
import json
from bson import json_util

main = Blueprint('main', __name__)

# Base API to return home page
@main.route('/')
def index():
    return render_template('index.html')

# Display Gallery page
@main.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Display MyData page
@main.route('/mydata')
def mydata():
    return render_template('mydata.html')

# Display Upload page
@main.route('/upload-global')
def upload_page():
    return render_template('uploadglobal.html')

# Upload CSV to mongo database
@main.route('/upload', methods=['POST'])
def upload():

    # Get data from request
    payload = request.json

    # Format the CSV data for insertion
    data = csv_format(payload['data'])

    # Get mongoDB collection
    db = mongo.get_database('diff-priv-data')
    datasets_collection = db.datasets

    # Insert data into datasets collection
    _id = datasets_collection.insert_one({
        "user_id": 0, # TEMP NEED USER AUTH
        "data": data,
        "title": payload['title'],
        "description": payload['description'],
        "author": "author", # TEMP NEED USER AUTH
        "local": payload['local']
        })

    # If global algorithms if specified
    if(payload['local'] is False):
        stats = driver_global_algo(data, payload['stats'])

        # Get data_stats collection
        datastats_collection = db.data_stats
        datastats_collection.insert_one({
            "datasets_id": _id.inserted_id,
            "stats": stats
        })

    return Response(status=200)

# Retrieve data stats and display
@main.route('/view/<datastatid>', methods=['GET'])
def get_datastats(datastatid):

    # Connect to mongo datastats collection
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    # Connect to mongo datasets collection
    datasets_collection = db.datasets

    # Find datastats
    stats = datastats_collection.find_one({"_id": ObjectId(datastatid)})

    # Find data metadata
    dataset_id = stats['datasets_id']
    metadata = datasets_collection.find_one({"_id": dataset_id})

    stats['title'] = metadata['title']
    stats['author'] = metadata['author']
    stats['description'] = metadata['description']
    stats['local'] = metadata['local']

    return json.loads(json_util.dumps(stats))

from app import mongo