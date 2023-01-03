#!/usr/bin/python3
from libs.handleAscii import AsciiObject
from libs.displayMenu import DisplayMenu
import libs.systemHelpers as sH



def main() -> None:
	sH.clearScreen()

	file_Logo = AsciiObject("visuals/logo.txt")
	file_Logo.printFileContent()
	

	backup_Options = DisplayMenu("Pick a backup type: ",
		{
			"": ""
		}
				
	)

	backup_Options.displayOptions()



if __name__ == "__main__":
	main()

