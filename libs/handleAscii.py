"""
    My own interpretation of handling ASCII file object's content

    self.file_Path by being sanitized in __init__ is always sanitized
"""

import os
import subprocess


class AsciiObject:
    def __init__(self, M_file_path: str="") -> None:
        # Log message "Initialization of '<file>' file object"

        self.file_Path = self.sanitizeUserInput(M_file_path)


        if self.file_Path == "":
            raise ValueError("Provide path to the object")

        if self.doesExistPath() == False:
            raise FileNotFoundError(f"'{self.getAbsolutePath()}' does not exist")
        

            
    def __str__(self) -> str:
        return self.file_Path


    def sanitizeUserInput(self, M_user_input: str) -> str:
        to_Sanitize_User_Input = str(M_user_input)
        
        if to_Sanitize_User_Input == "" or to_Sanitize_User_Input == str(None):
            return ""        

        # Sanitizing user input ( to_Sanitize_User_Input )
        
        sanitized_User_Input = to_Sanitize_User_Input
                
        return sanitized_User_Input


    def isAbsolutePath(self) -> bool:
       return os.path.isabs(self.file_Path)


    def getAbsolutePath(self) -> str:
        return os.path.abspath(str(self.file_Path)) 


    def doesExistPath(self) -> bool:
        return os.path.exists(self.getAbsolutePath())


    def getFileName(self) -> str:
        pass


    def getHashSum(self, M_hash_type: str="") -> str:
        hash_Type = self.sanitizeUserInput(M_hash_type).upper()
        hash_Types = ["MD5", "SHA1", "SHA256", "SHA512"]

        if hash_Type == "" or hash_Type not in hash_Types:
            raise ValueError("Provide correct hash type")
        
        script_Absolute_Path = AsciiObject(f"libs/shell/getHash{hash_Type}.sh").getAbsolutePath()
        
        hash_Sum = subprocess.check_output(["/usr/bin/bash", script_Absolute_Path, self.file_Path]).decode("utf-8")

        return {hash_Type: hash_Sum}


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
    
    AO.sanitizeUserInput(None)
    
