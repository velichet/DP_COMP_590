from routes.db import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email
from bson import ObjectId


class User():
    def __init__(self, first_name=None, last_name=None, email=None, password=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.id = id
        self.db = mongo.get_database('users')

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_email(self):
        return self.email
    
    def get_id(self):
        return self.id

    @classmethod
    def set_password(cls, password):
        cls.password_hash = generate_password_hash(password)

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

    def get_by_email(self, email):
        return self.db["profiles"].find_one({"email": email})
    
    def get_by_id(self, id):
        return self.db["profiles"].find_one({"_id": ObjectId(id)})

    def register(self):
        _id = self.db["profiles"].insert_one(self.to_dict())
        self.id = _id.inserted_id
        print(f"{self.to_dict()} entry created.")

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            # Storing hashed password, you should NEVER store the password itself in the database
            "password": self.password_hash,
        }


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    # submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    # submit = SubmitField('Register')

