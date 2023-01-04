from . import handleAscii


class DisplayMenu:
    def __init__(self, 
                M_menu_message:            str,
                M_menu_options:            dict,
                M_option_count_from:       int=1,
                M_message_tab_indents:     int=0, 
                M_menu_option_indents:     int=0,
                M_after_message_new_line:  bool=False,
                M_after_new_lines:         int=1,
                M_before_message_new_line: bool=True,
                M_before_new_lines:        int=1
                ) -> None:
        
        user_Input                =        handleAscii.AsciiObject()

        self.menu_Message         =        user_Input.sanitizeUserInput(M_menu_message)
        
        if self.menu_Message      == None:
            self.menu_Message     = ""
        self.message_Tab_Indents  = "\t" * user_Input.sanitizeUserInput(M_message_tab_indents)      
        

        self.menu_Options         =        user_Input.sanitizeUserInput(M_menu_options)
        self.menu_Option_Indents  = "\t" * user_Input.sanitizeUserInput(M_menu_option_indents)
        self.menu_Option_Keys     =        user_Input.sanitizeUserInput(self.menu_Options.keys())
        self.menu_Option_Values   =        user_Input.sanitizeUserInput(self.menu_Options.values())


        self.option_Count_From    =        user_Input.sanitizeUserInput(M_option_count_from)


        self.start_With_New_Line  =        user_Input.sanitizeUserInput(M_before_message_new_line)
        self.before_New_Lines     =        user_Input.sanitizeUserInput(M_before_new_lines)
        before_Message_New_Line   = "\n" * self.before_New_Lines if self.start_With_New_Line == True else ""

        self.end_With_New_Line    =        user_Input.sanitizeUserInput(M_after_message_new_line)
        self.after_New_Lines      =        user_Input.sanitizeUserInput(M_after_new_lines)
        after_Message_New_Line    = "\n" * self.after_New_Lines if self.end_With_New_Line == True else ""


        print(f"{before_Message_New_Line}{self.message_Tab_Indents}{self.menu_Message}{after_Message_New_Line}")


    def getOptionIndex(self) -> list:       # of tuples ( index, option_text(key) )
        option_Text  = self.menu_Option_Keys
        option_Index = []
        

        for index, option in enumerate(option_Text, start=self.option_Count_From):
            option_Index.append((index, option))
        
        return option_Index


    def displayOptions(self) -> None:
        no_Of_Indents = self.menu_Option_Indents

        for index, option in self.getOptionIndex():
            print(f"{no_Of_Indents}[{index}] {option}")
        

    def receiveMenuOptions(self) -> None:
        pass


if __name__ == "__main__":
    pass

#wartosc danego klucza