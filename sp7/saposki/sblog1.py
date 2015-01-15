#create a SQLite3 table and populate it with data

import sqlite3

#create a new database if the database doesn't already exist
with sqlite3.connect("sblog.db") as connection:

	#get a cursor 
	c = connection.cursor()

	#create the table 
	c.execute("""CREATE TABLE posts
		(fname TEXT, lname TEXT, email TEXT)
			""")

	#insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Orobosa", "Omorgie", "Orobosa@yahoo.com")')
	
