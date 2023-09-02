"""
if you get this error:
OSError: [WinError 193] %1 is not a valid Win32 application

you need to move the dll files in the main.py directory to system32 folder as director comes with system 32 dll files
"""

import qmclient as qm
import funcs as funcs


import json 

def getDictData(filename):
    dictData = getAllRecordsHelper("DICT " + filename)
    # print(dictData)

    trimmed_data = {}

    # Iterate through each key-value pair in the original data
    for key, value in dictData.items():
        # Check if the value is a list and has at least four items
        if isinstance(value, list) and len(value) >= 4 and str(value[1]).isnumeric():
            # Add the 4th item to the trimmed_data dictionary
            index = int(value[1])
            if index != 0 : trimmed_data[key] = {"name": value[3], "index": index - 1}
    return trimmed_data

"""
This function returns all records in a file using the DICT file to get the names of the fields
*THIS FUNCTION IS PRIVATE*
"""

def getAllRecordsHelper(fileName, dict = None):
    funcs.connectToDb()
    file = qm.Open(fileName)
    if dict is not None: DictFile = qm.Open("DICT " + fileName)

    dataOut = {}

    qm.Select(file, 1)
    while True:
        Id = qm.ReadNext(1)
        if Id == "": break
        Rec, Err = qm.Read(file, Id)

        if dict is not None:
            childItem = {}
            for key, value in dict.items():
                evalItem = qm.EvalConv(DictFile, key, Rec, "")
                evalItem = qm.DynArrayToList(evalItem)
                if evalItem == []:
                    childItem[value["name"]] = None
                else:
                    childItem[value["name"]] = evalItem
            dataOut[Id] = childItem
        else:
            dataOut[Id] = qm.DynArrayToList(Rec)


    qm.Close(file)
    if dict is not None: qm.Close(DictFile)
    return dataOut

"""
This function returns a all records in a file
 * @param filename: the name of the file to get the record from
"""

def getAllRecords(filename):
    filename = filename.upper()
    trimmed_data = getDictData(filename)

    return getAllRecordsHelper(filename, trimmed_data)

"""
This function returns a single record in a file using the DICT file to get the names of the fields
*THIS FUNCTION IS PRIVATE*
"""

def getARecordHelper(fileName, Id, dict):
    funcs.connectToDb()
    file = qm.Open(fileName)
    DictFile = qm.Open("DICT " + fileName)

    dataOut = {}

    Rec, Err = qm.Read(file, Id)

    childItem = {}
    for key, value in dict.items():
        evalItem = qm.EvalConv(DictFile, key, Rec, "")
        evalItem = qm.DynArrayToList(evalItem)
        if evalItem == []:
            childItem[value["name"]] = None
        else:
            childItem[value["name"]] = evalItem
    dataOut[Id] = childItem


    qm.Close(file)
    qm.Close(DictFile)
    return dataOut

"""
This function returns a single record in a file 
 * @param filename: the name of the file to get the record from
 * @param Id: the id of the record to get
"""

def getARecord(filename, Id):
    filename = filename.upper()
    trimmed_data = getDictData(filename)

    return getARecordHelper(filename, Id, trimmed_data)



# print(json.dumps(getARecord("CALLS", "00002"), indent=4, sort_keys=True))