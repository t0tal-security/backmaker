#!/usr/bin/python3
from libs.handleAscii import AsciiObject
import libs.systemHelpers as sH


def printLogo() -> None:
	try:
		file_Logo = AsciiObject("visualss/logo.txt")
	except ValueError as VE:
		print(VE)
	except FileNotFoundError as FNFE:
		print(f"Can not display logo: {FNFE}")
	else:
		file_Logo.printFileContent()


def printDefaultChoice() -> list:
	print("\nMake a choice of what to backup:")
	print("\n[1] File\n[2] Directory\n[3] List\n\n[0] Exit\n")

	return [1, 2, 3]


def getMenuChoice(F_go_back: bool=False) -> int:
	try:
		choice = int(input("[ backmaker ] > "))
		if choice == 0:
			print("\nTerminating!\n")
			exit()
	except KeyboardInterrupt as KI:
			print("\n\nTerminating!\n")
			exit()
	except ValueError as VE:
		print("Please provide integer number\n")
		return getMenuChoice()
	
	return choice


def backupFile() -> None:
	paths = []
	try:
		try:
			file_Path = AsciiObject(input("\nProvide absolute file path: "))
			paths.append(file_Path)
		except ValueError:
			print(f"Specify the absolute path to the file you want to backup!")
			exit()
		
		try:
			backup_Path = AsciiObject(input("Provide absolute backup path: "))
			paths.append(backup_Path)
		except ValueError:
			print(f"Specify the absolute path to the path where you want to backup your file!")
			exit()

	except KeyboardInterrupt as KI:
		print("\nTerminating!\n")
		exit()
			


def main() -> None:
	sH.clearScreen()
	printLogo()
	printDefaultChoice()

	choice = getMenuChoice()

	

if __name__ == "__main__":
	main()

