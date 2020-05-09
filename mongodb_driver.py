'''
--One of the most popular NoSQL database is MongoDB. MongoDB stores data in 
    JSON-like documents, which makes the database very flexible and scalable.
--To install mogodb follow: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
--Python needs a MongoDB driver to access the MongoDB database.
--install this package: python -m pip install pymongo
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
''' In MongoDB, a database is not created until it gets content! MongoDB waits 
until you have created a collection(table), with at least one document(record)
before it actually creates the database (and collection).
A collection in MongoDB is the same as a table in SQL databases.
A document in MongoDB is the same as a record in SQL databases.
'''
mycol = mydb["customers"]
# In MongoDB, a collection is not created until it gets content!

# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# print(x.inserted_id) 

# dblist = myclient.list_database_names()
# print(dblist)
# collist = mydb.list_collection_names()
# print(collist)
# if "customers" in collist:
#   print("The collection exists.")

# If you do not specify an _id field, then MongoDB will add one for you and
# assign a unique id for each document.
# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# If you do not want MongoDB to assign unique ids for you document, 
# you can specify the _id field when you insert the document(s).
# mylist = [
#   { "_id": 1, "name": "John", "address": "Highway 37"},
#   { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
#   { "_id": 3, "name": "Amy", "address": "Apple st 652"},
#   { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
#   { "_id": 5, "name": "Michael", "address": "Valley 345"},
#   { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
#   { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
#   { "_id": 8, "name": "Richard", "address": "Sky st 331"},
#   { "_id": 9, "name": "Susan", "address": "One way 98"},
#   { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
#   { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
#   { "_id": 12, "name": "William", "address": "Central st 954"},
#   { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
#   { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)
# print list of the _id values of the inserted documents:
# print(x.inserted_ids) 



'''In MongoDB we use the find and findOne methods to find data in a collection.
Just like the SELECT statement is used to find data in a table in a MySQL database.
The find() method returns all occurrences in the selection.
The first parameter of the find() method is a query object. In this example we use
an empty query object, which selects all documents in the collection.
No parameters in the find() method gives you the same result as SELECT * in MySQL.
'''
# result = mycol.find_one()
# result = mycol.find()
''' 
You are not allowed to specify both 0 and 1 values in the same object
(except if one of the fields is the _id field). If you specify a field
with the value 0, all other fields get the value 1, and vice versa.
The first argument of the find() method is a query object, and is used to limit the search.
'''
myquery = {}
# find_dic = {}
find_dic = { "_id": 0, "name": 1, "address": 1 }
# myquery = { "address": "Park Lane 38" }
# myquery = { "address": { "$regex": "^S" } }
# result = mycol.find(myquery,find_dic)
'''
Use the sort() method to sort the result in ascending or descending order.
sort("field", 1) #ascending
sort("field", -1) #descending 
'''
result = mycol.find(myquery,find_dic).sort("address", -1)

# The limit() method takes one parameter, a number defining how many documents to return.
# result = mycol.find(myquery,find_dic).sort("address").limit(4)

# You can update a record, or document as it is called in MongoDB, 
# by using the update_one() method.
# myquery = { "address": "Valley 345" }
# newvalues = { "$set": { "address": "Babolsar 123" } }
# mycol.update_one(myquery, newvalues)

# To update all documents that meets the criteria of the query, use the update_many() method.
# myquery = { "address": { "$regex": "^S" } }
# newvalues = { "$set": { "name": "Minnie" } }
# x = mycol.update_many(myquery, newvalues)
# print(x.modified_count, "documents updated.")

'''
To delete one document, we use the delete_one() method.
The first parameter of the delete_one() method is a query object
defining which document to delete.If the query finds more than
one document, only the first occurrence is deleted.
To delete more than one document, use the delete_many() method.
'''
# myquery = { "address": "Mountain 21" }
# myquery = { "address": {"$regex": "^P"} }
# x = mycol.delete_one(myquery)
# x = mycol.delete_many(myquery)
# To delete all documents in a collection, pass an empty query
# object to the delete_many() method:
x = mycol.delete_many({})

# print(x.deleted_count, " documents deleted.") 

# You can delete a table, or collection as it is called in MongoDB, by using the drop() method.
# mycol.drop() 

print(type(result)) 
for doc in result:
      print(doc) 
      
# this code return the list of Tables in database      
collist = mydb.list_collection_names()
print(collist)

  


  
  