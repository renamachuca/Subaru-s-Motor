from flask import Blueprint, jsonify, request
from .models import Order
from . import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    orders_list = [{"id": o.id, "product_id": o.product_id, "quantity": o.quantity, "total_price": o.total_price} for o in orders]
    return jsonify(orders_list)

@orders_bp.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=data['total_price']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order created successfully"}), 201
