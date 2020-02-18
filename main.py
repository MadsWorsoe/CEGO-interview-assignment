from database import GetDataFromDatabase
from writer import WriteToFileAndDeleteDBData

def WriteDataToLocalFile(query, filename):
    try:
        data = GetDataFromDatabase(query)
        if data is not None:
            lines = WriteToFileAndDeleteDBData(data, filename)
            print "Found " + str(len(data)) + " entries in the database"
            print "Wrote " + str(lines) + " entries to " + filename
            print str(len(data) - lines) + " entries were not inserted"
        else:
            return "There was no data found for this query"
        return "Succesfully inserted data!"
    except:
        raise Exception("Failed to insert data!")
