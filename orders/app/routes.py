from flask import Blueprint, jsonify, request
from .models import Product
from . import db

products_bp = Blueprint('products', __name__)


@products_bp.route('/home')
def home():
    try:
        db.session.query(Product).first()
        return jsonify({'message': 'conectado a la data base'})
    except Exception as e:
        return jsonify({'error': str(e)})


@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    products_list = [{"id": p.id, "name": p.name, "description": p.description, "price": p.price, "stock": p.stock} for p in products]
    return jsonify(products_list)

@products_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        stock=data['stock']
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully"}), 201
