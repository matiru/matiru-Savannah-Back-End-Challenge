# routes

from flask import Blueprint, request, jsonify
from models import db, Customer, Order
from sms import send_sms

routes = Blueprint('routes', __name__)

@routes.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(name=data['name'], code=data['code'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "Customer added successfully!"}), 201

@routes.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(item=data['item'], amount=data['amount'], time=data['time'], customer_id=data['customer_id'])
    db.session.add(new_order)
    db.session.commit()

    # Send SMS
    customer = Customer.query.get(new_order.customer_id)
    send_sms(to=customer.code, message=f"Order placed for {new_order.item}")
    
    return jsonify({"message": "Order placed successfully!"}), 201

@routes.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([{ "id": c.id, "name": c.name, "code": c.code } for c in customers])

@routes.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{ "id": o.id, "item": o.item, "amount": o.amount, "time": o.time, "customer_id": o.customer_id } for o in orders])
