# Anubis Version 2
- This is a modified version for Anubis repository founded in the following link :https://github.com/a1h2med/Anubis-IDE
- This was a project for CSE426 Software Maintenance and Evolution course in **Ain Shams Faculty of Engineering** provided by *Prof: Ayman Bahaa*

# Concept and benefits: 
This is a part of graduation project introduced by a team of Ain shams university written in Python language for creating an open-source editor that enable the user to write, edit, compile and run micro python codes (micro python is a code that runs on small embedded development boards mainly microcontrollers). Being open-source code is an advantage for allowing different developers to use this code, make some evolutions and maintain besides the provided functionality by this team


# New added features in this version:
-	A fast executed for python code: in this feature, the editor user will enter a code for a single function that would be automatically wrapped inside a program that has a main function that will call the function. The user would be asked to provide a list of parameters to be passed from the main function to the called function.
<img width="607" alt="Screen Shot 2020-09-09 at 11 49 47 PM" src="https://user-images.githubusercontent.com/47366286/92658613-2df38780-f2f7-11ea-8c16-f114412960b5.png">

-	Support for C# format: the editor automatically recognizes which format to use based on the file extension selected/opened and display it.
<img width="683" alt="Screen Shot 2020-09-09 at 11 52 32 PM" src="https://user-images.githubusercontent.com/47366286/92658883-9478a580-f2f7-11ea-9fa0-b5f01900a80d.png">
-	Fixing Issues: all old issues including variables name, functions names, bad comments and bad resturcturing in last version are fixed in this new version and we will big into these details later in the report file including with the repo (comment, restructure, naming,…)
-	Save As and Save: fixing issues in save button and introduce new feature as saveAs to support different ways (format) to save a file.

# Repository files:
-	Anubis.py: the file in which the main core project code exists.
- Python_coloring.py: the file in which the developer used to define his style, colorings, fonts, formats and syntax highlighter for the python language.
- Requirements.txt: the needed dependencies and libraries for the environment to work correctly.
- CSharpFormat.py: The file in which the first new added feature of supporting the C# format is being implemented
- CSharpRegex.py: The file in which the regular expression for the language C# have been implemented to support the language and used in CSharpFormat.py 
- ReservedCSharpIdentifiers.py: The file in which the reserved keywords, operators, braces used by C# language
- FastExecution.py: The Template in which the user will enter his code for being wrapped and tested and it includes the second new added feature 

# Report
- The repo includes a fully detailed reports showing:**Class Diagrram**, **Sequence Diagrram**, **Use Case**, **SRS**, **Screenshots for the running program with outputs**, **Fixed issues**, **Full descreption about each function and class in the program** and **Some evaluation metrics(Line of code)**,

## Requirements 
- Python3
- Pyserial (**Important for detecting ports section**)
- PYQT5

## Install Requirements 
(It's recommended to create virtual env before installing the requirements)
- pip3 install -r requirements.txt
### **NOTE**
If python3 is the default use this: 
- pip install -r requirements.txt 

## Run
- Clone the repo .
- Be sure you exist in the repo folder after cloning .
