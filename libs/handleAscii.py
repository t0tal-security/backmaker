"""
    My own interpretation of handling ASCII file object's content
"""

import os


class AsciiObject:
    def __init__(self, M_file_path: str="") -> None:
        # Log message "Initialization of '<file>' file object"
        
        self.file_Path = self.sanitizeUserInput(M_file_path)
        
    
    def __str__(self) -> str:
        return self.file_Path


    # Self-used


    def sanitizeUserInput(self, M_user_input: str) -> str:
        sanitized_User_Input = M_user_input        

        # Sanitizing user's input code
        
        return sanitized_User_Input


    def doesExistPath(self) -> bool:
        return os.path.exists(self.file_Path)


    def getAbsolutePath(self) -> str:
        if self.doesExistPath() == False:
            print("(logLib: Error) Path does not exist")
            exit()
        
        return os.path.abspath(self.file_Path)


    # User-used        


    def readFileContent(self) -> str:
        absolute_File_Path = self.getAbsolutePath()
        
        with open(absolute_File_Path, "r") as file_To_Read:
                file_Content = file_To_Read.read()
        
        return file_Content


    def printFileContent(self):
        file_Content = self.readFileContent()
        print(file_Content) 



if __name__ == "__main__":
    pass #    file_Logo = AsciiFile("visuals/logo.txt")