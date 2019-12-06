#Step1
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

    '''
    qry = "INSERT INTO student (sname, semail, smobile) VALUES(%s,%s,%s)"

    dbcursor = db.cursor()
    dbcursor.executemany(qry, values)
    db.commit()
    '''

def getAllRecords(db, table):

    qry = "SELECT * FROM "+table
    dbcursor = db.cursor()
    dbcursor.execute(qry)

    return dbcursor.fetchall();
