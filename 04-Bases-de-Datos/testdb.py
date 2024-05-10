import pymssql


# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb-eoi.database.windows.net",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

cursor = connection.cursor(as_dict=True)

###################################################
# INSERT, las agrupaciones                        #
###################################################

cliente2 = {
    "ClientID": "BCR01",
    "CompanyName": "Empresa Dos, SL",
    "ContactName": "Borja Cabeza",
    "ContactTitle": "Gerente",
    "Address": "Calle Dos S/N",
    "City": "Madrid",
    "Region": "Madrid",
    "PostalCode": "28019",
    "Country": "España",
    "Phone": "910 101 102",
    "Fax": "910 101 103"
}

command = """
    INSERT INTO dbo.Customers(CustomerID, CompanyName)
    VALUES('AGF01', 'Alejandro Company SL')
"""

cursor.execute(command)

connection.commit()
#connection.rollback()
connection.close()