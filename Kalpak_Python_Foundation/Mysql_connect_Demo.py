'''
1. Import mysql.connector
2. Connect and Create a Db object
3. Execute Queries
4. Fetch results of a query
5. Update the changes in cursor to database (commit)
'''

#Step1
import dboperations as dbo

#step2
db = dbo.connect("localhost","root","","demodb")

#Create new database
'''
qry = "CREATE DATABASE demodb"
dbcursor = db.cursor()
dbcursor.execute(qry)
print("New database created...")
'''

#Fetch the list of databases
'''
qry = "SHOW DATABASES"
dbcursor = db.cursor()
dbcursor.execute(qry)
databases = dbcursor.fetchall();
for database in databases:
    print(database)
'''

#Create Table
'''
qry = "CREATE TABLE student( sroll int NOT NULL AUTO_INCREMENT PRIMARY KEY, " \
      "sname VARCHAR(50), semail VARCHAR(150), smobile INT)"
dbcursor = db.cursor()
dbcursor.execute(qry)
print("New table created...")
'''

#Fetch the list of tables
'''
qry = "SHOW TABLES"
dbcursor = db.cursor()
dbcursor.execute(qry)
tables = dbcursor.fetchall();
for table in tables:
    print(table)
'''

#INSERT RECORDS
dbo.insert(db, "student", ["sname", "semail", "smobile"],[("demo","demo@gmail.com","11111")])


#Fetch the list of students
students = dbo.getAllRecords(db,"student")
for student in students:
    print(student)











#inserting record
'''qry = "INSERT INTO course(course_name,course_fees,course_duration) " \
      "VALUES('ssss','111','222')"
dbcursor = db.cursor()
dbcursor.execute(qry)
db.commit()
print(dbcursor.rowcount, " rows inserted")
'''


