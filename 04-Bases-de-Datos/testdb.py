import pymssql


# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="sqlserver-eoi.database.windows.net",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)
cursor = connection.cursor(as_dict=True)


###################################################
# SELECT, leer registros de la base de datos      #
###################################################

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
