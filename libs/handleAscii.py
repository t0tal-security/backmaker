"""
    My own interpretation of handling ASCII file object's content

    self.file_Path by being sanitized in __init__ is always sanitized
"""

import os
import subprocess


class AsciiObject:
    def __init__(self, M_file_path: str="") -> None:
        # Log message "Initialization of '<file>' file object"
        
        if M_file_path == "":
            raise ValueError("Provide path to the object")


        self.file_Path = self.sanitizeUserInput(M_file_path)
        
    
    def __str__(self) -> str:
        return self.file_Path



    def sanitizeUserInput(self, M_user_input: str) -> str:
        sanitized_User_Input = M_user_input        

        # Sanitizing user's input code
        
        return sanitized_User_Input


    def isAbsolutePath(self) -> bool:
       return os.path.isabs(self.file_Path)


    def getAbsolutePath(self) -> str:      
        return os.path.abspath(self.file_Path) 


    def doesExistPath(self) -> bool:
        return os.path.exists(self.getAbsolutePath())


    def getHashSum(self, M_hash_type: str="") -> str:
        # MD5, SHA1, SHA256, SHA512
        hash_Type = self.sanitizeUserInput(M_hash_type)
        
        if hash_Type == "":
            raise ValueError("Provide hash type")

        def getHashMD5():
            script_Absolute_Path = AsciiObject("libs/shell/getHashMD5.sh").getAbsolutePath()

            hash_Sum = subprocess.check_output(["/usr/bin/bash", script_Absolute_Path, self.file_Path]).decode("utf-8")
            return hash_Sum

        def getHashSHA1():
            script_Absolute_Path = AsciiObject("libs/shell/getHashSHA1.sh").getAbsolutePath()

            hash_Sum = subprocess.check_output(["/usr/bin/bash", script_Absolute_Path, self.file_Path]).decode("utf-8")
            return hash_Sum

        def getHashSHA256():
            script_Absolute_Path = AsciiObject("libs/shell/getHashSHA256.sh").getAbsolutePath()

            hash_Sum = subprocess.check_output(["/usr/bin/bash", script_Absolute_Path, self.file_Path]).decode("utf-8")
            return hash_Sum

        def getHashSHA512():
            script_Absolute_Path = AsciiObject("libs/shell/getHashSHA512.sh").getAbsolutePath()

            hash_Sum = subprocess.check_output(["/usr/bin/bash", script_Absolute_Path, self.file_Path]).decode("utf-8")
            return hash_Sum

        hash_Types = {
            "MD5":    getHashMD5,
            "SHA1":   getHashSHA1,
            "SHA256": getHashSHA256,
            "SHA512": getHashSHA512
        }

        if hash_Type in hash_Types.keys():
            hash_Value = hash_Types.get(hash_Type)()
        
        return hash_Value


    def readFileContent(self) -> str:
        absolute_File_Path = self.getAbsolutePath()

        if self.doesExistPath() == False:
            raise FileNotFoundError(f"Provided non-existent file '{absolute_File_Path}' to read")
            
        with open(absolute_File_Path, "r") as file_To_Read:
                file_Content = file_To_Read.read()
        
        return file_Content


    def printFileContent(self):
        try:
            file_Content = self.readFileContent()
        except FileNotFoundError as FNFE:
            print(FNFE)
            exit()
        else:
            print(file_Content) 



if __name__ == "__main__":
    AO = AsciiObject("visuals/logso.txt")
    #print(AO.getAbsolutePath())
    #AO.printFileContent()
    #try:
    print(AO.getHashSum("SHA512"))
    #except ValueError as VE:
        #print(VE)
    