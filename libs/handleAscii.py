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

        if self.doesExistPath() == False:
            raise FileNotFoundError(f"'{self.file_Path}' does not exist")
        
            
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
        hash_Type = self.sanitizeUserInput(M_hash_type).upper()
        
        if hash_Type == "":
            raise ValueError("Provide hash type")

        hash_Types = ["MD5", "SHA1", "SHA256", "SHA512"]

        if hash_Type in hash_Types:
            script_Absolute_Path = AsciiObject(f"libs/shell/getHash{hash_Type}.sh").getAbsolutePath()
        
        try:
            hash_Sum = subprocess.check_output(["/usr/bin/bash", script_Absolute_Path, self.file_Path]).decode("utf-8")
        except UnboundLocalError:
            print("Check provided hash type again!")
        else:
            return hash_Sum


    def readFileContent(self) -> str:
        absolute_File_Path = self.getAbsolutePath()
            
        with open(absolute_File_Path, "r") as file_To_Read:
                file_Content = file_To_Read.read()
        
        return file_Content


    def printFileContent(self) -> None:
        file_Content = self.readFileContent()
        print(file_Content) 



if __name__ == "__main__":
    AO = AsciiObject("visuals/logo.txt")
    
    print(AsciiObject("visuals/logo.txt").getHashSum("sha512"))
    