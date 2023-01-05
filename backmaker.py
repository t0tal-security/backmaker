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


def printChoice() -> None:
	print("Make a choice of what to backup:")
	print("\n[1] File\n[2] Directory\n[3] List\n\n[0] Exit\n")


def getChoice() -> int:
	try:
		choice = int(input("[ backmaker ] > "))
		if choice == 0:
			print("\nTerminating!\n")
			exit()
	except KeyboardInterrupt as KI:
			print("\nTerminating!\n")
			exit()
	except ValueError as VE:
		print("Please provide integer number\n")
		return getChoice()
	
	return choice



def main() -> None:
	sH.clearScreen()
	printLogo()
	printChoice()

	choice = getChoice()

	if choice > 3:
		print(">3")



if __name__ == "__main__":
	main()

