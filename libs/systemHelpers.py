"""
    Some useful functions used for retrieving system variables and any things alike
"""

import os
import platform



def getSystemVersion() -> str:
    return platform.system()


def clearScreen() -> None:        
    os.system("clear")
    

