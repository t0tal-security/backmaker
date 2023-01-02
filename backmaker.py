#!/usr/bin/python3
from libs.handleAscii import AsciiFile
import libs.systemHelpers as sH



def main() -> None:
	sH.clearScreen()

	file_Logo = AsciiFile("visuals/logo.txt")
	file_Logo.printFileContent()


if __name__ == "__main__":
	main()

