"""Model for tables in dtabase"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from env import PASSWORD, DATABASE, USERNAME


app = Flask(__name__)
app.secret_key = "Secret Key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' +USERNAME+ ':' +PASSWORD+ '@localhost/' +DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()
db.init_app(app)


class Parent(db.Model):
    """Model for parent table"""
    __tablename__ = "parent"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.Integer, nullable=False)

    child_relation = db.relationship(
        "Child", cascade="all, delete-orphan", backref="Parent", lazy=True)

    def __init__(self, first_name, last_name, street, city, state, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def add_child(self, first_name, last_name):
        """Add child to database

        Args:
            first_name (string): Form data
            last_name (string): Form data
        """
        new_child = Child(first_name=first_name, last_name=last_name, parent_id=self.id)
        db.session.add(new_child)
        db.session.commit()



class Child(db.Model):
    """Child tabel model"""
    __tablename__ = "child"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey(
        "parent.id", ondelete='CASCADE'), nullable=False)
