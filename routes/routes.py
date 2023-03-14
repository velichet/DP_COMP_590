from flask import Blueprint, render_template, request, Response
from scripts.driver.format import csv_format
from scripts.driver.global_driver import driver_global_algo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # db = mongo.db
    # datasets_collection = db.datasets
    # datasets_collection.insert_one({"id":1,"test":"success"})
    return render_template('index.html')

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
        "user_id": payload['user_id'],
        "data": data,
        "private": payload['private'],
        "description": payload['description'],
        "author": payload['author'],
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


from app import mongo