from flask import Flask
from routes.data import data
from routes.pages import page
from routes.auth import auth
from scripts.user import User
import os


app = Flask(__name__)

# Will move this to env
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from routes.login import login_manager

login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    user = User().get_by_id(id)
    if not user:
        return None
    return User(email=user["email"], first_name=user['first_name'], last_name=user['last_name'], id=user['_id'])

app.register_blueprint(auth)
app.register_blueprint(data)
app.register_blueprint(page)


if __name__ == "__main__":
    app.run(port=8000,debug=True)