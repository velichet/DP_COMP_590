from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # db = mongo.db
    # datasets_collection = db.datasets
    # datasets_collection.insert_one({"id":1,"test":"success"})
    return render_template('index.html')

from app import mongo