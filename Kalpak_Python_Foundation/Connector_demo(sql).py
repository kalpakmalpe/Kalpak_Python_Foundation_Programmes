
#Connector demo
#Connect to mysql



import mysql.connector


db=mysql.connector.connect( host='localhost',user='root',password="",database='sample')



# inserting method

#qry=" INSERT INTO course  VALUES('5','PHP','4','10000')"

#dbcursor=db.cursor()
#dbcursor.execute(qry)
#db.commit()

#print(dbcursor.rowcount,"rows inserted")



qry=" INSERT INTO course  VALUES(%s,%s,%s,%s)"

val=("6","java","4","5000")
dbcursor=db.cursor()
dbcursor.execute(qry,val)
db.commit()

print(dbcursor.rowcount,"rows inserted")



