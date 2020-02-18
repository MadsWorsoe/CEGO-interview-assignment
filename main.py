from database import GetDataFromDatabase

def WriteDataToLocalFile(query, filename):
    try:
        data = GetDataFromDatabase(query)
        if data is not None:
            WriteToFileAndDeleteDBData(data, filename)
        else:
            return "There was no data found for this query"
        return "Succesfully inserted data!"
    except:
        raise Exception("Failed to insert data!")
