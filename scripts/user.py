from routes.db import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class User():
    def __init__(self, firstName=None, lastName=None, email=None, password=None):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
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

    def get_id(self):
        return self.email

    @classmethod
    def set_password(cls, password):
        cls.password_hash = generate_password_hash(password)

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

    def get_by_email(self, email):
        return self.db["profiles"].find_one({"email": email})

    def register(self):
        self.db["profile"].insert_one(self.to_dict())
        print(f"{self.to_dict()} entry created.")

    def to_dict(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "email": self.email,
            # Storing hashed password, you should NEVER store the password itself in the database
            "password": self.password_hash,
        }


class LoginForm(FlaskForm):
    Email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


class RegistrationForm(FlaskForm):
    firstName = StringField('firstName', validators=[DataRequired()])
    lastName = StringField('lastName', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

