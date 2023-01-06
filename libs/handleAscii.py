"""
    My own interpretation of handling ASCII file object's content
"""

import os


class AsciiObject:
    def __init__(self, M_file_path: str="") -> None:
        # Log message "Initialization of '<file>' file object"
        
        if M_file_path == "":
            raise ValueError("Provide path to the object")


        self.file_Path = self.sanitizeUserInput(M_file_path)
        
    
    def __str__(self) -> str:
        return self.file_Path


    # Self-used


    def sanitizeUserInput(self, M_user_input: str) -> str:
        sanitized_User_Input = M_user_input        

        # Sanitizing user's input code
        
        return sanitized_User_Input


    def doesExistPath(self) -> bool:
        return os.path.exists(self.getAbsolutePath())


    def isAbsolutePath(self) -> bool:
       return os.path.isabs(self.file_Path)


    def getAbsolutePath(self) -> str:      
        return os.path.abspath(self.file_Path)


    def getHashSum(self) -> str:
        # MD5, SHA1, SHA256, SHA512
        pass


    # User-used        


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
    pass #AO = AsciiObject("")
    