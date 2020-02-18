from database import DeleteElementFromDB

def IsDataInFile(data, filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                if data in line:
                    return True
        return False
    except:
        raise Exception("Data was not correctly written to file, aborting!")

def WriteToFileAndDeleteDBData(data, filename):
    try:
        i = 0
        #CreateFile(filename)
        with open(filename, "w+") as file:
            for element in data:
                line = WriteElementToFile(file, element)
                DataExists = IsDataInFile(line, filename)
                if DataExists is True:
                    DeleteElementFromDB(element)
                    i += 1
                else:
                    raise Exception("Data was not inserted properly!")
        return i
    except:
        raise Exception("Failed to write data to file!")

def ReadDataFromFile(filename):
    try:
        str = ""
        with open(filename, "r") as file:
            for line in file.read().splitlines():
                str += line
            temp = file.read().splitlines()
        return str
    except:
        raise Exception("Unable to read from sqldump file")

def CreateFile(filename):
    try:
        with open(filename) as FileExists:
            FileExists.close()
            print "File: " + filename + " already exist"
    except:
        print "File: " + filename + " does not exist"
        with open(filename, "w") as CreateFile:
            CreateFile.close()
            print "File: " + filename + " Created"

def WriteElementToFile(writer, element):
    try:
        line = ", ".join(map(str, element))
        writer.write(line)
        writer.write("\n")
        writer.flush()
        print "Wrote ID: " + element[0] + " to file"
        return line
    except:
        raise Exception("Failed to write element to file")