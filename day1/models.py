from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)

class test2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(100))