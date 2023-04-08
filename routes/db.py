import pymongo
import os

mongo = pymongo.MongoClient(os.environ.get('MONGO_URI'))