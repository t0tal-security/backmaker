#!/usr/bin/python3
from libs.handleAscii import AsciiObject
import libs.systemHelpers as sH


def printLogo() -> None:
	try:
		file_Logo = AsciiObject("visuals/logo.txt")
	except ValueError as VE:
		print(f"Can not display logo: {VE}")
	except FileNotFoundError as FNFE:
		print(f"Can not display logo: {FNFE}")
	else:
		file_Logo.printFileContent()


def printDefaultChoices() -> list:
	print("Make a choice of what to backup:")
	print("\n[1] File\n[2] Directory\n[3] List\n\n[0] Exit\n")

	return [1, 2, 3]


def getMenuChoice() -> int:
	try:
		choice = int(input("\n[ backmaker ] > "))
	except ValueError as VE:
		print("Please provide integer number\n")
		return getMenuChoice()


	if choice == 0:
			print("\nTerminating!\n")
			exit()

	return choice


def selectMenuChoice() -> None:
	function_Of_Choice = {1: backupFile, 2: backupFolderContents, 3:backupList}

	choices = printDefaultChoices()
	choice = getMenuChoice()

	if choice in choices:
		function_Of_Choice[choice]()


def backupFile(F_file_path: str="", F_backup_path: str="") -> None:
	sH.clearScreen()
	printLogo()

	def assignPaths():
		if F_file_path == "" or F_backup_path == "":
			try:
				file_Path, backup_Path = AsciiObject(input("Absolute path of file: ")), AsciiObject(input("Absolute path to backup dir: "))
			except ValueError:
				print("Provide path!")
				exit()
			except FileNotFoundError:
				print("File can not be found")
				exit()

		
		return file_Path, backup_Path



	file_Path, backup_Path = assignPaths()
	origin_File_Hash = file_Path.getHashSum("SHA256")
	print(origin_File_Hash)
	
	

def backupFolderContents() -> None:
	sH.clearScreen()
	printLogo()
	print("backupFolderContents")


def backupList() -> None:
	sH.clearScreen()
	printLogo()
	print("backupList")



def main() -> None:
	sH.clearScreen()
	printLogo()
	
	try:
		selectMenuChoice()
	except KeyboardInterrupt as KI:
		print("\nTerminating!\n")
		exit()
	
	

if __name__ == "__main__":
	os_Version = sH.getSystemVersion()

	if os_Version != "Linux":
		print("Are you running linux?")
		exit()


	main()

