from pymongo import MongoClient, collection
from bson.json_util import dumps, loads

server = "localhost"
port = 27017
db = "northwind"

def _get_collection(collection, server=server, port=port, db=db):
    return MongoClient(f"mongodb://{server}:{port}/")[db][collection]

def getCustomersList() -> list:
    try:
        return list(_get_collection("customers").find({}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}

def getCustomer(id) -> dict:
    try:
        return _get_collection("customers").find_one({"CustomerID": id}, {"_id": 0})
    except Exception as e:
        return {"Error": e}
    
def getOrdersList() -> list:
    try:
        return list(_get_collection("orders").find({}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}

def getOrder(id) -> dict:
    try:
        return _get_collection("orders").find_one({"OrderID": id}, {"_id": 0})
    except Exception as e:
        return {"Error": e}
    
def getOrdersFromCustomer(id) -> list:
    try:
        return list(_get_collection("orders").find({"CustomerID": id}, {"_id": 0}))

    except Exception as e:
        return {"Error": e}














# def get_customers_list():
#     clientDB = MongoClient("mongodb://localhost:27017/")
#     db = clientDB.northwind    
#     collection = db.customers 

#     clientes = collection.find()
#     listaClientes = []
    
#     while clientes.alive:
#         cliente = clientes.next()        
#         listaClientes.append(cliente)

#     for cliente in listaClientes:
#         cliente['_id'] = str(cliente['_id'])

#     return listaClientes

        
# def get_customer(id):
#     clientDB = MongoClient("mongodb://localhost:27017/")
#     db = clientDB.northwind
#     collection = db.customers

#     cliente = collection.find_one({"_id": id})
#     cliente['_id'] = str(cliente['_id'])


#     return cliente
