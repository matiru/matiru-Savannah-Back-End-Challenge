# models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    code = db.Column(db.String(15))  # Phone number

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    amount = db.Column(db.Float)
    time = db.Column(db.String(100))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
