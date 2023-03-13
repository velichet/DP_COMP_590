from flask import Flask, render_template
from routes.routes import main
import pymongo


app = Flask(__name__)

mongo = pymongo.MongoClient('mongodb+srv://mattsg:c9X692mAK5fzmUee@diff-privacy.o8huhxp.mongodb.net/?retryWrites=true&w=majority')

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(port=8000,debug=True)