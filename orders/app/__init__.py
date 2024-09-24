from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicialización de la base de datos
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuración de la base de datos PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:penguin@localhost/products_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicialización de la base de datos
    db.init_app(app)
    
    # Registrar las rutas
    from .routes import products_bp
    app.register_blueprint(products_bp)
    
    return app
