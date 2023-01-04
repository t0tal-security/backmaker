#!/usr/bin/python3
from libs.handleAscii import AsciiObject
from libs.displayMenu import DisplayMenu
import libs.systemHelpers as sH


def temp_file_path():
	print("wfile_path")

def temp_directory_path():
	print("wdirectory_path")

def temp_list_path():
	print("wlist_path")


def main() -> None:
	sH.clearScreen()

	file_Logo = AsciiObject("visuals/logo.txt")
	file_Logo.printFileContent()
	

	backup_Options = DisplayMenu("Pick a backup type: ",
		{
			"kFile": temp_file_path(),
			"kDirectory": temp_directory_path(),
			"kList":	temp_list_path()
		}				
	)

	backup_Options.displayOptions()


if __name__ == "__main__":
	main()

