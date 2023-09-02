"""
if you get this error:
OSError: [WinError 193] %1 is not a valid Win32 application

you need to move the dll files in the main.py directory to system32 folder as director comes with system 32 dll files
"""

import qmclient as qm
import mvsupport as mv


def connectToDb():
    if not qm.ConnectLocal("SJD"):
        print("Failed to connect - ", qm.Error())
        return False
    else:
        print("Connected")
        return True