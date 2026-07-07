import mysql.connector


def get_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Berra2004?",
        database="predictx_db"
    )

    return connection