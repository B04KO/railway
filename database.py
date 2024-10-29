import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='autorack.proxy.rlwy.net',
            user='root',
            password='iEEjTTJTbcVSVFnPNOzTzqYSDFBpmHIc',
            database='HTP_1',
            port='48476'
        )
        return connection
    except Error as e:
        print(f"Error: '{e}'")
        return None
