from flask import Blueprint, render_template, request, Response
from scripts.driver.format import csv_format
import json

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # db = mongo.db
    # datasets_collection = db.datasets
    # datasets_collection.insert_one({"id":1,"test":"success"})
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload():

    payload = request.json
    data = csv_format(payload['data'])

    db = mongo.get_database('diff-priv-data')
    datasets_collection = db.datasets
    datasets_collection.insert_one({
        "user_id": payload['user_id'],
        "data": data,
        "private": payload['private'],
        "description": payload['description'],
        "author": payload['author'],
        "local": payload['local']
        })

    return Response(status=200)


from app import mongo