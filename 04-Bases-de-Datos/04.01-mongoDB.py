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

client = MongoClient("mongodb://localhost:27017/")
db = client.admin
result = db.command("serverStatus")

pprint(result)