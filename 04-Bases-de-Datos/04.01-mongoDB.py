###################################################
# Trabajando con mongoDB                          #
###################################################

from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

###################################################
# Conectar con un servidor mongoDB                #
###################################################

#client = MongoClient("127.0.0.1", "27017")
#client = MongoClient("localhost", "27017")
#client = MongoClient("mongodb://USER:PASSWORD@<IP>:<PORT>/")
#client = MongoClient("mongodb://127.0.0.1:27017/")

###################################################
# Ejecutar comando - Mostrar estado del servidor  #
###################################################

# Creamos un objeto que almacenamos en la variable clientDB
# El objeto representa el cliente para trabajar con las bases de datos de mongoDB
# Se requiere una cadena de conexión
clientDB = MongoClient("mongodb://localhost:27017/")

# Nos posicionamos sobre una base de datos, en el ejemplo sobre la base de datos ADMIN
db = clientDB.admin

# Ejecutamos un comando utilizando la función COMMAND
# El comando serverStatus nos retorna el estado del servidor en formato JSON
result = db.command("serverStatus")

# Mostramos el resultado de la ejecución del comando
pprint(result)

###################################################
# Trabajar con bases de datos y sus colecciones   #
###################################################

# Mostrar el nombre de las bases de datos
print(clientDB.list_database_names())

# El listado de bases de datos es una LISTA de python que podemos recorrer con un FOR
for db in clientDB.list_database_names():
    print(f"Nombre: {db}")
    print(f"-> {clientDB[db].list_collection_names()}\n")

# Seleccionar una base de datos con la que vamos a trabajar
db = clientDB.northwind             # Sintaxis de Objeto
db2 = clientDB["northwind"]         # Sintaxis de Colección

# Mostrar las colecciones que tiene una base de datos
# Las colecciones son equivalente a las tablas en las bases de datos realcionales 
print(db.list_collection_names())
print(db2.list_collection_names())

# Seleccionar una colección con la que vamos a trabajar
# collection = clientDB["northwind"]["customers"]
# collection = clientDB.northwind.customers
# collection = db["customers"]
collection = db.customers           # Todas son formas de hacer lo mismo

# Mostramos el número de documentos
# Los documentos son equivalentes a los registros en bases de datos relacionales
print(f"La colección {collection.name} tiene {collection.estimated_document_count()} documentos.")

###################################################
# Trabajar con los documentos de las colecciones  #
###################################################

# Mostrar el documento por identificador del objeto
# Filtro: _id = 
result = collection.find_one({"_id": ObjectId("663a1062bcd71e98892bf2a6")})
pprint(result)
print("")

# Mostrar el primer documento que coincide con el filtro
# Filtro: Country = USA
result = collection.find_one({"Country": "USA"})
pprint(result)
print("")

# Mostrar todos los documentos que coinciden con el filtro
# Filtro: Country = USA
# Retorna un cursor
cursor = collection.find({"Country": "USA"})

# Mostrar el número de documentos de una búsqueda
# print(f"Resultado de la búsqueda son {cursor.count()} documentos")    # No disponible desde la versión ___
print(f"Resultado de la búsqueda son {collection.count_documents({"Country": "USA"})} documentos\n")

# Cuando ALIVE retorna TRUE significa que tenemos documentos pendientes de leer en el cursor
print(f"¿Quedan documentos pendientes de leer? {cursor.alive}\n")

# Utilizamos WHILE para mostrar los documentos del cursor
# el WHILE se ejecuta mientras ALIVE retorne TRUE
# Con la función .NEXT() para posicionarnos en el siguiente documento del cursor
while cursor.alive:
    pprint(cursor.next())
    print("")

print(f"¿Quedan documentos pendientes de leer? {cursor.alive}\n")


###################################################
# Ejemplos: Búsquedas, Utilización de operadores  #
###################################################
dbNorthwind = clientDB.northwind
coleccionClientes = dbNorthwind.customers
coleccionPedidos = dbNorthwind.orders
coleccionProductos = dbNorthwind.products
"""
===================================================
 Listado de operadores relacionales
===================================================
$eq     - equal - igual
$ne     - not equal - distinto

$lt     - low than - menor que
$lte    - low than equal - menor o igual que

$gt     - greater than - mayor que
$gte    - greater than equal - mayor o igual que

$in     - in - dentro de
$nin    - not in - no dentro de
$regex  - cumple con la expresión regular
"""

#clientesFiltrados = coleccionClientes.find({"Country": "USA"})
#clientesFiltrados = coleccionClientes.find({"Country": "USA"}).limit(3)
#clientesFiltrados = coleccionClientes.find({"Country": "USA"}).skip(5)
#clientesFiltrados = coleccionClientes.find({"Country": "USA"}).sort("City")      # Ordenados de A a W
#clientesFiltrados = coleccionClientes.find({"Country": "USA"}).sort({"City": 1}) # Ordenados de A a W
clientesFiltrados = coleccionClientes.find({"Country": "USA"}).sort({"City": -1}) # Ordenados de W a A

# Buscar clientes de USA, ejemplos con y sin operador
clientesFiltrados = coleccionClientes.find({"Country": "USA"})                    # Sin operador
clientesFiltrados = coleccionClientes.find({"Country": {"$eq": "USA"}})           # Con operador

# Buscar clientes fuera de USA
clientesFiltrados = coleccionClientes.find({"Country": {"$ne": "USA"}})

# Buscar clientes de USA y MExico, ordenados por país y ciudad
clientesFiltrados = coleccionClientes.find({"Country": {"$in": ["USA", "Mexico"]}}).sort([("Country", 1), ("City", 1)])

# Buscar clientes que contienen DE en la clave CustomerID
clientesFiltrados = coleccionClientes.find({"CustomerID": {"$regex": "DE"}})

# Buscar clientes que el CustomerID empieza por A y finaliza con 4 caracteres más 
clientesFiltrados = coleccionClientes.find({"CustomerID": {"$regex": "A[A-Z]{4}"}})

# Buscar clientes de la ciudad de San Francisco en USA 
clientesFiltrados = coleccionClientes.find({"Country": "USA", "City": "San Francisco"})

# Buscar clientes de la ciudad de San Francisco en USA utilizando el operador AND
clientesFiltrados = coleccionClientes.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})

# Buscar clientes de GERMANY o USA utilizando el operador OR
clientesFiltrados = coleccionClientes.find({"$or": [{"Country": "Germany"}, {"Country": "USA"}]})

# Buscar los clientes de Mexico y sus pedidos
clientesFiltrados = coleccionClientes.find({"Country": "Mexico"})

while clientesFiltrados.alive:
    cliente = clientesFiltrados.next()
    print(f"ID del Cliente: {cliente["CustomerID"]}# - Nombre de la Compañía: {cliente["CompanyName"]} - País: {cliente["Country"]} - Ciudad: {cliente["City"]}")

    pedidosFiltrados = coleccionPedidos.find({"CustomerID": cliente["CustomerID"]})
    while pedidosFiltrados.alive:
        pedido = pedidosFiltrados.next()
        print(f">>> ID del Pedido: {pedido["OrderID"]}# - Fecha del Pedido: {pedido["ShippedDate"]}")

    print("--------------------")

# Buscar los clientes de Mexico y sus pediddos utilizando la función AGGREGATE
clientesConPedidosFiltrados = coleccionClientes.aggregate([
    {"$match": {"Country": "Mexico"}},
    {"$sort": {"City": 1}},
    {"$lookup": {
        "from": "orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Pedidos"
    }}
])

while clientesConPedidosFiltrados.alive:
    clienteConPedidos = clientesConPedidosFiltrados.next()
    print(f"ID del Cliente: {clienteConPedidos["CustomerID"]}# - Nombre de la Compañía: {clienteConPedidos["CompanyName"]} - País: {clienteConPedidos["Country"]} - Ciudad: {clienteConPedidos["City"]}")

    for pedido in clienteConPedidos["Pedidos"]:
        print(f">>> ID del Pedido: {pedido["OrderID"]}# - Fecha del Pedido: {pedido["ShippedDate"]}")
    
    print("")

# Buscamos todos los productos con UnitsInStock distinto de cero
# Convertir UnitInStock y UnitPrice en valores numéricos
# Calcular la suma de multiplicar el precio por unidades de cada producto

productosFiltrados = coleccionProductos.find({"UnitsInStock": {"$ne": 0}})

total = 0
while productosFiltrados.alive:
    producto = productosFiltrados.next()
    unidadesEnStock = int(producto["UnitsInStock"])
    precio = float(producto["UnitPrice"])
    total += unidadesEnStock * precio

print(f"Valor del Stock: {total:1.2f}")

# Utilizamos AGGREGATE para calcular el valor del stock
query = [
    {"$match": {"UnitsInStock": {"$ne": "0"}}},
    {"$addFields": {
        "Precio": {"$toDouble": "$UnitPrice"},
        "Unidades": {"$toInt": "$UnitsInStock"}
    }},
    {"$group": {
        "_id": "Valor del Stock",
        "Total": {"$sum": {"$multiply": ["$Precio", "$Unidades"]}},
        "Productos": {"$sum": 1}
    }}
]

productosFiltrados = coleccionProductos.aggregate(query)
pprint(productosFiltrados.next())


###################################################
# CRUD con documentos                             #
###################################################

# Creamos la clase Customer que define un cliente de nuestra base de datos
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None
    
    def __init__(self, customerID, companyName, contactName, contactTitle, adress, city, region, postalCode, country, phone, fax) -> None:
        self.CustomerID = customerID
        self.CompanyName = companyName
        self.ContactName = contactName
        self.ContactTitle = contactTitle
        self.Address = adress
        self.City = city
        self.Region = region
        self.PostalCode = postalCode
        self.Country = country
        self.Phone = phone
        self.Fax = fax

###################################################
# Insertar documentos                             #
###################################################

# Insertamos partiendo de la clase Customer
#cliente = Customer("DEMO1", "Empresa Uno, SL", "Alejandro", "Gerente", "Calle Uno, S/N", "Granada", "Granada", "18195", "España", "900100100", "900100200")

# Todos los objetos de python tienen una propiedad que es __dict__
# que retorna un diccionario de todas sis variables
#pprint(cliente.__dict__)

#id = coleccionClientes.insert_one(cliente.__dict__).inserted_id
#print(f"ID del nuevo documento: {id}")

# Insertamos partiendo de un diccionario
#cliente2 = {
#    "CustomerID": "DEMO2",
#    "CompanyName": "Empresa Dos, SL",
#    "ContactName": "Borja Cabeza",
#    "ContactTitle": "Gerente",
#    "Address": "Calle Dos S/N",
#    "City": "Madrid",
#    "Region": "Madrid",
#    "PostalCode": "28019",
#    "Country": "España",
#    "Phone": "910 101 102",
#    "Fax": "910 101 103"}

#id = coleccionClientes.insert_one(cliente2).inserted_id
#print(f"ID del nuevo documento: {id}")

###################################################
# Actualizar documentos                           #
###################################################

query = {"CustomerID": "DEMO2"}
clienteFiltrado = coleccionClientes.find_one(query)
pprint(clienteFiltrado)

# Actualizamos uno o varios documentos de una colección

# Nuevos valores para el documento o documentos que vamos a actualizar
newValues = {"$set": {
    "ContactName": "Ana Sanz",
    "PostalCode": "28013"
}}

# Actualizar el primer documento que retorna la consulta
result = coleccionClientes.update_one(query, newValues)

# Actualizar todos los documentos que retorna la consulta
result = coleccionClientes.update_many(query, newValues)

print(f"{result.matched_count} documentos encontrados")
print(f"{result.modified_count} documentos modificados")
print(result)

pprint(coleccionClientes.find_one(query))