from flask import Blueprint, request, Response, redirect, url_for, render_template
from scripts.driver.format import csv_format
from scripts.driver.global_driver import driver_global_algo
from bson.objectid import ObjectId
import json
from bson import json_util

data = Blueprint('data', __name__)

# Upload CSV to mongo database
@data.route('/upload', methods=['POST'])
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
        "local": payload['local']
        })

    # If global algorithms if specified
    if(payload['local'] is False):
        stats = driver_global_algo(data, payload['stats'])

        # Get data_stats collection
        datastats_collection = db.data_stats
        datastats_collection.insert_one({
            "datasets_id": _id.inserted_id,
            "user_id": 0, # TEMP NEED USER AUTH
            "stats": stats,
            "title": payload['title'],
            "description": payload['description'],
            "author": "author", # TEMP NEED USER AUTH,
            "stats_data": payload['stats']
        })
    
    return url_for('page.mydata')

# Retrieve data stats and display
@data.route('/view/<datastatid>', methods=['GET'])
def get_datastats(datastatid):

    # Connect to mongo datastats collection
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    # Find datastats
    stats = datastats_collection.find_one({"_id": ObjectId(datastatid)})

    return render_template('viewdata.html', stats = stats)

# Retrieve all data stat sets from the database
@data.route('/gallery', methods=['GET'])
def gallery():

    # Connect to mongo stats collcetion
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats

    stats = datastats_collection.find()

    # for s in stats:
    #     print(s['title'] + s['description'] + str(s['_id']))

    return render_template('gallery.html', stats = stats)

from app import mongo