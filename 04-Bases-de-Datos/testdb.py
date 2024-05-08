from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

clientDB = MongoClient("mongodb://localhost:27017/")
db = clientDB.northwind
coleccionClientes = db.customers
coleccionPedidos = db.orders
coleccionProductos = db.products

###################################################
# Eliminar documentos                             #
###################################################
