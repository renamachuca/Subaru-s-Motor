# Subaru's Motor

## Descripción del Proyecto

Subaru's Motor es un proyecto basado en microservicios que gestiona una tienda de autopartes Subaru. El sistema está diseñado para manejar productos y pedidos a través de APIs RESTful, utilizando Flask como framework web y PostgreSQL como base de datos.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

subaru's motor/
├── products/
│   ├── app/
│   │   ├── __init__.py       
│   │   ├── models.py         
│   │   ├── routes.py       
│   ├── Dockerfile           
│   ├── requirements.txt     
├── orders/
│   ├── app/
│   │   ├── __init__.py      
│   │   ├── models.py       
│   │   ├── routes.py       
│   ├── Dockerfile            
│   ├── requirements.txt      
├── docker-compose.yml 

## Funcionalidades

- **Gestión de Productos**: Permite la creación y consulta de productos en la tienda.
- **Gestión de Pedidos**: Facilita la creación y consulta de pedidos realizados por los usuarios.

## Rutas de la API

### Pedidos

- `GET /orders`: Obtiene la lista de todos los pedidos.
- `POST /orders`: Crea un nuevo pedido. Requiere un JSON con `product_id`, `quantity` y `total_price`.

## Configuración

Para configurar el proyecto:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/renamachuca/Subaru-s-Motor.git



   Navega a la carpeta del proyecto:

bash
Copy code
cd 'subaru's motor'
Crea un entorno virtual e instala las dependencias:

bash
Copy code
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
Configura las variables de entorno para la base de datos y Flask:

bash
Copy code
export FLASK_APP=wsgi.py
export FLASK_ENV=development
Ejecuta la aplicación:

bash
Copy code
flask run
