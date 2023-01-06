#!/usr/bin/python3
from libs.handleAscii import AsciiObject
import libs.systemHelpers as sH


def printLogo() -> None:
	try:
		file_Logo = AsciiObject("visuals/logo.txt")
	except ValueError as VE:
		print(VE)
	else:
		file_Logo.printFileContent()


def printDefaultChoice() -> None:
	print("\nMake a choice of what to backup:")
	print("\n[1] File\n[2] Directory\n[3] List\n\n[0] Exit\n")


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



def main() -> None:
	sH.clearScreen()
	printLogo()
	printDefaultChoice()

	choice = getMenuChoice()

	if choice == 1:
		try:
			file_Path 	= AsciiObject(input("\nProvide file path: "))
			backup_Path = AsciiObject(input("Provide backup path: "))
		except ValueError as VE:
			print(f"\nE: {VE}")
		except KeyboardInterrupt as KI:
			print("\nTerminating!\n")
			exit()
	elif choice == 2:
		pass
	elif choice == 3:
		pass
	elif choice == 0:
		print("\nTerminating!\n")
		exit()



if __name__ == "__main__":
	main()

