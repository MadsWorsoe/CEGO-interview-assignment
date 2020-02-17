def WriteDataToLocalFile(query, filename):
    try:
        data = GetDataFromDatabase(query)
        WriteToFileAndDeleteDBData(data, filename)
        return "Succesfully inserted data!"
    except:
        return "Failed to insert data: " + error
