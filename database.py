import mysql.connector as mariadb
import config

def GetDataFromDatabase(query):
    try:
        cursor = CreateDBConnection()
        results = cursor.execute(query)
        return results
    except:
        raise Exception("Failed to get data from database!")

def CreateDBConnection():
    address = config['mariadb']['mariadb_ip_address']
    port = config['mariadb']['mariadb_port']
    user = config['mariadb']['mariadb_user']
    password = config['mariadb']['mariadb_password']
    db = config['mariadb']['mariadb_db']
    try:
        conn = mariadb.connect(user=user,
                           password=password,
                           database=db,
                           address=address,
                           port=port)
        return conn.cursor()
    except:
        raise Exception("Failed to connect to database: " + address)