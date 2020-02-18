import config
from database import CreateDBConnection, CloseDBConnection, ExecuteMultipleStatements, DropTable
from main import WriteDataToLocalFile
from writer import ReadDataFromFile


def TestAssignment(sqldumpname, query, filename):
    try:
        ExecuteSQLDump(sqldumpname)
        WriteDataToLocalFile(query, filename)
        print "Test Success!"
    except:
        raise

def ExecuteSQLDump(sqldumpname):
    conn = CreateDBConnection()
    sqldumpQuery = ReadDataFromFile(sqldumpname)
    DropTable(UsersTable)
    ExecuteMultipleStatements(conn, sqldumpQuery)
    CloseDBConnection(conn)

sqldumpLocation = "sqldump.sql"
UsersTable = config.mariadb.__getitem__("users_table")
SelectQuery = "SELECT id, firstName, lastName, email FROM " + UsersTable
file = "Test.txt"


TestAssignment(sqldumpLocation, SelectQuery, file)