"""
    Some useful functions used for retrieving system variables and any things alike
"""

import os
import platform



def getSystemVersion() -> str:
    return platform.system()



def clearScreen() -> None:
    os_Version = getSystemVersion()

    if os_Version == "Linux":
        os.system("clear")
        return None

    if os_Version == "Windows":
        os.system("cls")
        return None
    
    print("[Error] Unable to clear the screen")

