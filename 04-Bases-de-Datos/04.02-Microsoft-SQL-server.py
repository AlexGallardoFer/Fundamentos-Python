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