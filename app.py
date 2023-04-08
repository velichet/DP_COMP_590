from flask import Flask
from routes.data import data
from routes.pages import page
from routes.auth import auth


app = Flask(__name__)

app.register_blueprint(data)
app.register_blueprint(page)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(port=8000,debug=True)