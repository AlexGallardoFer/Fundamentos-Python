from flask import Flask, request, Response, jsonify, session
from DemoModulo import *

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

@app.route("/api/customers", methods=["GET"])
def get_customers():
    return jsonify(getCustomersList()), 200

@app.route("/api/customers/<id>", methods=["GET"])
def get_customer(id):
    return jsonify(getCustomer(id)), 200

@app.route("/api/customers/<id>/orders", methods=["GET"])
def get_order_from_customer(id):
    return jsonify(getOrdersFromCustomer(id)), 200

@app.route("/api/orders", methods=["GET"])
def get_orders():
    return jsonify(getOrdersList()), 200

@app.route("/api/orders/<id>", methods=["GET"])
def get_order(id):
    return jsonify(getOrder(id)), 200


#########################################################################
# Control de errores aplicación Flask
#########################################################################

# Código para manejar la solicitud no encontrada
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({f"Error {e.code} ({e.name})": f"{e.description}"}), 404

# Código para manejar el error interno de código
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({f"Error {e.code} ({e.name})": f"{e.description}"}), 500

# Código para manejar errores genericos
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({f"Error": f"{e}"}), 500


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()