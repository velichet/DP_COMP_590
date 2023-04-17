from flask import Blueprint, request, Response, redirect, url_for, render_template
from scripts.driver.format import csv_format
from scripts.driver.global_driver import driver_global_algo
from bson.objectid import ObjectId
from routes.db import mongo
import json
from bson import json_util

data = Blueprint('data', __name__)

# Upload CSV to mongo database
@data.route('/upload', methods=['POST'])
def upload():

    # Get data from request
    payload = request.json

    # Format the CSV data for insertion
    if(payload['local'] is False):
        data = csv_format(payload['data'])
    else:
        data = []

    # Get mongoDB collection
    db = mongo.get_database('diff-priv-data')
    datasets_collection = db.datasets

    # Insert data into datasets collection
    _id = datasets_collection.insert_one({
        "user_id": 0, # TEMP NEED USER AUTH
        "data": data,
        "local": payload['local']
        })


    stats = {}
    # If global algorithms if specified
    if(payload['local'] is False):
        stats = driver_global_algo(data, payload['stats'])
    else:
        field = payload['stats'].keys()
        field = list(field)[0].lower()
        stats[field] = {"count": json.loads(payload['data'])}

    datastats_collection = db.data_stats
    datastats_collection.insert_one({
        "datasets_id": _id.inserted_id,
        "user_id": 0, # TEMP NEED USER AUTH
        "stats": stats,
        "title": payload['title'],
        "description": payload['description'],
        "author": "Safely Stat", # TEMP NEED USER AUTH,
        "stats_data": payload['stats']
    })
    
    return url_for('page.mydata')

# Retrieve data stats and display
@data.route('/view/<datastatid>', methods=['GET'])
def get_datastats(datastatid):

    # Connect to mongo datastats collection
    db = mongo.get_database('diff-priv-data')
    datastats_collection = db.data_stats
    datasets_collection = db.datasets

    # Find datastats
    stats = datastats_collection.find_one({"_id": ObjectId(datastatid)})

    metadata = datasets_collection.find_one({"_id": stats['datasets_id']})
    local = metadata['local']

    return render_template('viewdata.html', stats = stats, local = local)