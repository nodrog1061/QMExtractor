"""
if you get this error:
OSError: [WinError 193] %1 is not a valid Win32 application

you need to move the dll files in the main.py directory to system32 folder as director comes with system 32 dll files
"""

import qmclient as qm
import mvsupport as mv
import funcs as funcs


funcs.connectToDb()

# calls = qm.Open("CALLS")
callsDict = qm.Open("DICT CALLS")

# Rec = qm.Trans("DICT CALLS", "-1", "LOC", "X")
# Data = qm.EvalConv(callsDict, "UNITS", Rec, "00001")
# print(Rec)
# print(qm.DynArrayToList(Rec))

# qm.Select(calls, 1)

# while True:
#   Id = qm.ReadNext(1)
#   if Id == "": break
#   Rec, Err = qm.Read(calls, Id)

# qm.Select(calls, 1)
# List = qm.ReadList(1)
# print(List)

# callsDict = qm.Open("DICT CALLS")
# print(qm.Indices(calls, ""))
DataRec, Err = qm.Read(callsDict, "CLASS")
# print(DataRec)
# print(qm.GetVar("@DICTRECS"))
# DataValue = qm.EvalConv(callsDict, ["ON.SCENE","LOCATION"], DataRec, "")
# print(DataValue)

# while True:
#   Key = qm.SelectRight(calls, "CALLS", 1)
      

# # print(qm.Select(calls, 0))

# Rec, Err = qm.Read(calls, "8")
# print(Rec)
# print(qm.Error())
# index = 0
data = qm.DynArrayToList(DataRec)
print(data)
# print(len(data))

# # # while data != "" or data != "2":
# # #     index =+ 1
# # #     data = qm.Extract(Rec, index, 0, 0)
# # #     print(data)

# for i in range(1, 50):
#     data = qm.Extract(Rec, i, 0, 0)
#     print(data)

# calls = qm.OpenSeq("CALLS", "00001", 0x0010)
# print(qm.Error())
# Rec, Err = qm.ReadSeq(calls)
# print(Rec)


# print(qm.DynArrayToList(qm.Trans("CALLS", "00001", "-1", "0x0010")))


qm.Close(calls)
qm.Close(callsDict)