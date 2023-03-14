from flask import Flask, render_template
from routes.routes import main
import pymongo
import os


app = Flask(__name__)

mongo = pymongo.MongoClient(os.environ.get('MONGO_URI'))

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(port=8000,debug=True)