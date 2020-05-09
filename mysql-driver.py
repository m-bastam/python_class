'''
Python needs a MySQL driver to access the MySQL database, so first install it.
python -m pip install mysql-connector 

'''
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="user_class",
  passwd="123456",
  database="demodb"
)
# print(mydb) 
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE classdb")
mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("CREATE TABLE customers1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# ----------Insert a record
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# ------insert multiple records
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)


# !!! Notice the statement: mydb.commit(). It is required to make the changes, 
# otherwise no changes are made to the table.
# mydb.commit()

# print(mycursor.rowcount, "record(s) was inserted.")                 
# mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 


# sql = "SELECT * FROM customers"
# sql = "SELECT * FROM customers LIMIT 4"
# sql = "SELECT * FROM customers LIMIT 3 OFFSET 2"
# sql = "SELECT name, address FROM customers"
# sql = "SELECT * FROM customers ORDER BY id DESC"
# mycursor.execute(sql)

# sql = "SELECT * FROM customers WHERE address = %s"
# sql = "DELETE FROM customers WHERE address = %s"
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# sql = "DROP TABLE customers"
# sql = "DROP TABLE IF EXISTS customers"
# val = ("Yellow Garden 2", )
# val=()
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) was deleted.")  
# We use the fetchall() method, which fetches all rows from the last executed statement.
# myresult = mycursor.fetchall()
# print(type(myresult))
# for x in myresult:
#   print(x)


