import mysql.connector as mariadb
import config

def GetDataFromDatabase(query):
    try:
        conn = CreateDBConnection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        CloseDBConnection(conn)
        return results
    except:
        raise Exception("Failed to get data from database!")

def DropTable(TableName):
    try:
        conn = CreateDBConnection()
        query = "DROP TABLE IF EXISTS " + TableName
        try:
            conn.cursor().execute(query)
            CloseDBConnection(conn)
        except mariadb.Warning:
            CloseDBConnection(conn)
    except:
        raise Exception("Failed to drop table " + str(TableName))

def DeleteElementFromDB(element):
    try:
        conn = CreateDBConnection()
        UsersTable = config.mariadb.__getitem__("users_table")
        query = "DELETE FROM " + UsersTable + " WHERE id = '" + element[0] + "'"
        conn.cursor().execute(query)
        CloseDBConnection(conn)
        print "Deleted id: " + element[0] + " from database"
    except:
        raise Exception("Unable to delete data from DB!")

def CreateDBConnection():
    user = config.mariadb.__getitem__("user")
    password = config.mariadb.__getitem__("password")
    db = config.mariadb.__getitem__("db")
    address = config.mariadb.__getitem__("ip_address")
    port = config.mariadb.__getitem__("port")
    try:
        conn = mariadb.connect(user=user,
                               password=password,
                               host=address,
                               port=port,
                               database=db)
        return conn
    except:
        raise Exception("Failed to connect to database: " + str(address))

def CloseDBConnection(conn):
    conn.commit()
    conn.close()

def ExecuteMultipleStatements(generator, query):
    try:
        for result in generator.cursor().execute(query, multi=True):
            pass
    except:
        raise Exception("Failed to Execute Statements!")