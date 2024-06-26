###################################################
# Trabajando con Microsoft SQL Server             #
###################################################

import pymssql


# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb-eoi.database.windows.net",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

# Creamos un cursor para ejecutar comandos en la base de datos
# Creamos un cursor que retorna Tuplas
cursor = connection.cursor()

# Creamos un cursor que retorna Diccionarios
cursor = connection.cursor(as_dict=True)


###################################################
# SELECT, leer registros de la base de datos      #
###################################################

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")

# Mostrar el contenido del cursor utilizando un WHILE
row = cursor.fetchone()
while(row):
    print(f"ID:      {row["CustomerID"]}")
    print(f"Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})\n")
    row = cursor.fetchone()

# El siguiente ejemplo comentado muestra como tratar los registros cuando se 
# entregan Tuplas en lugar de Diccionarios
row = cursor.fetchone()
while(row):
    print(f"ID:      {row[0]}")
    print(f"Empresa: {row[1]} - {row[5]} ({row[8]})\n")
    row = cursor.fetchone()

# Mostrar el contenido del cursor utilizando un FOR
clientes = cursor.fetchall()

for cliente in clientes:
    print(f"ID:      {cliente["CustomerID"]}")
    print(f"Empresa: {cliente["CompanyName"]} - {cliente["City"]} ({cliente["Country"]})\n")


# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "USA")

#pais = input("Nombre del país: ")
#cursor.execute(f"SELECT * FROM dbo.Customers WHERE Country = '{pais}'")
#cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", pais)

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' AND City = 'San Francisco'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany'")

cursor.execute("SELECT CompanyName, CustomerID, City, Country FROM dbo.Customers WHERE Country = 'USA'")

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country ASC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country DESC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country, City")


clientes = cursor.fetchall()
for cliente in clientes:
    print(f"ID:      {cliente["CustomerID"]}")
    print(f"Empresa: {cliente["CompanyName"]} - {cliente["City"]} ({cliente["Country"]})\n")



cursor = connection.cursor(as_dict=True)

# Ejemplo que comienza con una consulta y realiza 830 subconsultas dentro del FOR
cursor.execute("SELECT * FROM dbo.Orders")

for row in cursor.fetchall():
    print(f"-> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")

    cursor2 = connection.cursor(as_dict=True)
    #cursor2.execute("SELECT * FROM dbo.Employees WHERE EmployeeID = %d", row["EmployeeID"])     # Son lo mismmo
    cursor2.execute(f"SELECT * FROM dbo.Employees WHERE EmployeeID = {row["EmployeeID"]}")
    employee = cursor2.fetchone()

    print(f"   Pedido gestionado por {row["EmployeeID"]}: {employee["FirstName"]} {employee["LastName"]}")


# Ejemplo que se realiza con una sola consulta

#cursor.execute("SELECT * FROM dbo.Orders AS o, dbo.Employees AS e")                             # Es lo mismo
#cursor.execute("SELECT * FROM dbo.Orders o, dbo.Employees e")

cursor.execute("SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName FROM dbo.Orders o, dbo.Employees e WHERE o.EmployeeID = e.EmployeeID")

for row in cursor.fetchall():
    print(f"-> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")
    print(f"   Pedido gestionado por {row["EmployeeID"]}: {row["FirstName"]} {row["LastName"]}")

###################################################
# SELECT, ejemplos de JOIN                        #
###################################################

query = """
    SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName 
    FROM dbo.Orders o
    JOIN dbo.Employees e
    ON o.EmployeeID = e.EmployeeID
"""
cursor.execute(query)

for row in cursor.fetchall():
    print(f"-> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")
    print(f"   Pedido gestionado por {row["EmployeeID"]}: {row["FirstName"]} {row["LastName"]}")


###################################################
# SELECT, las agrupaciones                        #
###################################################

# Listado de clientes de USA y el número de pedidos de cada cliente
# NO ES UNA AGRUPACIÓN, es una subconsulta dentro del FOR que DEBEMOS evitar por rendimiento
query = "SELECT * FROM dbo.Customers WHERE Country = 'USA'"
cursor.execute(query)

for row in cursor.fetchall():
    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute(f"SELECT COUNT(*) FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()[0]} pedidos")

"""
    Opcionalmente podemos trabajar con cursores que retornan diccionarios, pero estamos
    obligados a definir alias para el dato calculado usando AS

    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute(f"SELECT COUNT(*) AS numPedidos FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()["numPedidos]} pedidos")    
"""

# Listado de clientes de USA y el número de pedidos de cada cliente
# Solo los clientes con más de 10 pedidos
query = """
    SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) as NumPedidos
    FROM dbo.Customers c
    JOIN dbo.Orders o
    ON c.CustomerID = o.CustomerID
    WHERE c.Country = 'USA'
    GROUP BY c.CustomerID, c.CompanyName
    HAVING COUNT(o.OrderID) > 10
"""
cursor.execute(query)

for row in cursor.fetchall():
    print(f"-> {row["CustomerID"]}# - {row["CompanyName"]} -> {row["NumPedidos"]} pedidos")


######################################################
# INSERT, insertar nuevo registros
######################################################

# Definición de un objeto que representa el registro CUSTOMER 
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

# Instanciamos el objeto CUSTOMER
cliente = Customer()
cliente.CustomerID = "DEMO1"
cliente.CompanyName = "Empresa Uno, SL"
cliente.ContactName = "Borja"
cliente.ContactTitle = "Gerente"
cliente.Address = "Calle Uno, S/N"
cliente.City = "Madrid"
cliente.Region = "Madrid"
cliente.PostalCode = "28016"
cliente.Country = "España"
cliente.Phone = "900100100"
cliente.Fax = "900100200"

# cliente2 es un diccionario que también representa el registro CUSTOMER
cliente2 = {"CustomerID": "DEMO2",
            "CompanyName": "Empresa Dos, SL",
            "ContactName": "Borja Cabeza",
            "ContactTitle": "Gerente",
            "Address": "Calle Dos S/N",
            "City": "Madrid",
            "Region": "Madrid",
            "PostalCode": "28019",
            "Country": "España",
            "Phone": "910 101 102",
            "Fax": "910 101 103"}

# INSERT comando de inserción
command = """
    INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactTitle, City, Country)
    VALUES('BCR01', 'Company SL', 'Borja Cabeza', 'Madrid', 'España')
"""

# Insertamos nuevos registros ejecutado el comando INSERT
cursor.execute(command)

# Utilizamos la función commit() de la conexión para CONFIRMAR la transacción
# tanto para operaciones de inserción, actualización y borrado
connection.commit()

# Utilizamos la función rollback() de la conexión para ANULAR la transacción
# tanto para operaciones de inserción, actualización y borrado
connection.rollback()

# Ejemplo de un comando INSERT que indica las columnas o campos y sus valores
command = """
    INSERT INTO dbo.Customers(
        CustomerID, 
        CompanyName, 
        ContactTitle, 
        City, 
        Country) VALUES('BCR01', 'Company SL', 'Borja Cabeza', 'Madrid', 'España')
"""
# Ejemplo de un comando INSERT que indica las columnas o campos y comodines para los valores
command2 = """
    INSERT INTO dbo.Customers(
        CustomerID, 
        CompanyName, 
        ContactName,
        ContactTitle, 
        City, 
        Country) VALUES(%s, %s, %s, %s, %s, %s)
"""

# Al ejecutar el comando con comodines, pasamos como segundo parámetro los valores en una lista
cursor.execute(command2, ["BCR02", "Company Demo, SL", "Borja", "CEO", "Valencia", "España"])

# El mismo ejemplo donde pasamos los valores en una tupla
cursor.execute(command2, ("BCR03", "Company Demo, SL", "Borja", "CEO", "Valencia", "España"))
connection.commit()

# Para insertar varios registros al mismo tiempo creamos una lista que contiene en cada posición
# una tupla con los valores de cada registro que vamos a insertar
data = []
data.append(("BCR10", "Company Demo 10, SL", "Borja", "CEO", "Sevilla", "España"))
data.append(("BCR11", "Company Demo 11, SL", "Carlos", "CEO", "Bilbao", "España"))
data.append(("BCR12", "Company Demo 12, SL", "Julian", "CEO", "Málaga", "España"))    

# Utilizamos la función .executemany() para insertar varios registros y pasamos como segundo
# parámetro la lista de tuplas con los valores de los diferentes registros
cursor.executemany(command2, data)
connection.commit()

# La propiedad o variable .rowcount nos devuelve el número de registros insertados, actualizados o borrados
print(f"{cursor.rowcount} registros insertados.")

# Ejemplo de un INSERT donde se especifican valores para todos los campos o columnas del registro
command = """
    INSERT INTO dbo.Customers VALUES(
        'DEMO2',
        'Empresa Dos, SL',
        'Borja Cabeza',
        'Gerente',
        'Calle Dos S/N',
        'Madrid',
        'Madrid',
        '28019',
        'España',
        '910 101 102',
        '910 101 103')
"""

# Ejemplo de un INSERT donde se especifican comodines para los valores para todos los 
# campos o columnas del registro
command = """
    INSERT INTO dbo.Customers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


######################################################
# UPDATE, actulizar registros
######################################################

command = """
    UPDATE dbo.Customers
    SET Address = 'Calle Uno, S/N', ContactName = 'Carlos Sánchez'
    WHERE CustomerID = 'BCR11'
"""

# cursor.execute(command)
connection.commit()

print(f"{cursor.rowcount} registros actualizados.")


command = """
    UPDATE dbo.Customers
    SET Address = %s, ContactName = %s
    WHERE CustomerID = 'BCR12'
"""

cursor.execute(command, ("Calle Principal, 10", "María José Sanz"))
connection.commit()

print(f"{cursor.rowcount} registros actualizados.")


command = """
    UPDATE dbo.Customers
    SET Address = %s, ContactName = %s
    WHERE CustomerID = %s
"""

cursor.execute(command, ("Calle Principal, 10", "María Sanz", "BCR12"))
connection.commit()

print(f"{cursor.rowcount} registros actualizados.")


######################################################
# DELETE, eliminar registros
######################################################

command = """
    DELETE FROM dbo.Customers
    WHERE CustomerID = 'BCR10'
"""

try:
    cursor.execute(command)
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f"Error: {e}")
finally:
    print(f"{cursor.rowcount} registros eliminados.")
    connection.close()


command = """
    DELETE FROM dbo.Customers
    WHERE CustomerID = %s
"""

try:
    cursor.execute(command, ("BCR11"))
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f"Error: {e}")
finally:
    print(f"{cursor.rowcount} registros eliminados.")
    connection.close()