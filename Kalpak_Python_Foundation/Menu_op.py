import mysql.connector

#step2


def connect(hostname, username, password, database):

    db = mysql.connector.connect(
        host = hostname,
        user = username,
        passwd = password,
        database = database
    )

    return db



def insert(db, table, columns, values):

    qry = "INSERT INTO "+table+ " ("
    for col in columns:
        qry = qry + col + ","
    qry = qry[0:len(qry)-1]

    qry = qry + ") VALUES ("
    for col in columns:
        qry = qry + "%s,"
    qry = qry[0:len(qry)-1]

    qry = qry + ")"
    dbcursor = db.cursor()
    dbcursor.executemany(qry, values)
    db.commit()


def delete(db,table,id):
    qry="DELETE FROM " +table+ " WHERE rno=" +id
    dbcursor=db.cursor()
    dbcursor.execute(qry)
    db.commit()




def display(db, table):

    qry = "SELECT * FROM "+table
    dbcursor = db.cursor()
    dbcursor.execute(qry)

    return dbcursor.fetchall();


def update(db,table,id,nam):

    qry= "UPDATE" +table+ "SET name ="+nam+  "WHERE"+table+"rno = " +id
    dbcursor = db.cursor()
    dbcursor.execute(qry)
    db.commit()

def search(db,table,id):
    qry="SELECT * FROM "+table+ "WHERE rno="+id
    dbcursor = db.cursor()
    dbcursor.execute(qry)
    return dbcursor.fetchall();
