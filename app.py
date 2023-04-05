from flask import Flask
from routes.data import data
from routes.pages import page
import pymongo
import os


app = Flask(__name__)

mongo = pymongo.MongoClient(os.environ.get('MONGO_URI'))

app.register_blueprint(data)
app.register_blueprint(page)

if __name__ == "__main__":
    app.run(port=8000,debug=True)