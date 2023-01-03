from . import handleAscii


class DisplayMenu:
    def __init__(self, 
                M_menu_message: str,
                M_menu_options: dict,
                M_option_count_from: int=1,
                M_message_tab_indents: int=0, 
                M_menu_option_indents: int=0,
                M_message_new_line: bool=False
                ) -> None:
        
        user_Input            =        handleAscii.AsciiObject()

        self.menu_Message        =        user_Input.sanitizeUserInput(M_menu_message)
        self.message_Tab_Indents = "\t" * user_Input.sanitizeUserInput(M_message_tab_indents)      
        self.menu_Options        =        user_Input.sanitizeUserInput(M_menu_options)
        self.option_Count_From   =        user_Input.sanitizeUserInput(M_option_count_from)
        self.menu_Option_Indents = "\t" * user_Input.sanitizeUserInput(M_menu_option_indents)
        self.end_With_Newline    =        user_Input.sanitizeUserInput(M_message_new_line)


        if self.end_With_Newline == False:
            new_line = ""
        
        if self.end_With_Newline == True:
            new_line = "\n"


        print(f"{self.message_Tab_Indents}{self.menu_Message}{new_line}")
        

    def getMenuKeys(self) -> str:        # <class 'dict_keys'>
        return self.menu_Options.keys()
    

    def getKeyIndex(self) -> int:
        menu_Keys  = self.getMenuKeys()
        keys_Index = []

        for index, key in enumerate(menu_Keys):
            keys_Index.append((index, key))


    def displayOptions(self) -> None:
        menu_Keys     = self.getMenuKeys()
        no_Of_Indents = self.menu_Option_Indents 
        
        for index, key in enumerate(menu_Keys, start=self.option_Count_From):     
            print(f"{no_Of_Indents}[{index}] {key}")


    def receiveMenuOptions(self) -> None:
        pass