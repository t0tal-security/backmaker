# backmaker.py
Tool for automatic files backup

## This is newbie project
Don't hesitate about giving me any advices about the code. As I am trying my best, that is unlikely for mistakes to actually not happen.

And I know that some functions may be considered as reengineering a wheel. As described in the code, some of the system actions around the files, texts etc. are done with my vision of way of doing so.


# What is the tool going to do?
Ask you for input. Choose backup of singular files or list of files. In specified format, lists should have file paths to copy and destination paths to backup to.

It will proceed with the some actions related to backup as of checking if the path exists, make a recursive call for checking whether it is a directory or not. Get file's hash sum. Copy file to destination and get hash sum of copied file. Compare both hashes and based on that inform whether the copy action was successful or not.
Take hash sums with the help of bash scripts

For lists there are going to be functionalities checking if the files were modified or not ( based on hash sum ) and it will be decided not to backup such file ( to avoid potential file corruption ).  

Everything will be managed inside of proper functions or methods.
