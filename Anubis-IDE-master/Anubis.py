"""
Introduction: this file includes the main project functionalities including reading, opening, compiling & running
(Not yet implemented), saving both python code and CSharp.
This is considered as Version 2 from original repos on https://github.com/a1h2med/Anubis-IDE that includes many new
features.
This project is part of their graduation project and it intends to make a fully functioned IDE from scratch
########################################################################################################################
"""
"""
########################################################################################################################
   The imports needed for the project including:
    1-PYQT5,I/O library
    2-Python_Coloring including the format used for python code
    3-CSharpFormat including the format used for CSharp code
    4-FastExecution including the template in which the user enters his code
########################################################################################################################
"""
import sys
import glob
import os
import serial
import Python_Coloring
import CSharpFormat
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import FastExecution
from io import StringIO

"""
########################################################################################################################
 Global variables section
########################################################################################################################
"""
# Making text editor as A global variable (to solve the issue of being local to (self) in widget class)
text = QTextEdit
text2 = QTextEdit

# This includes the path for the file the user opens/selects
filePathForSelectedFile = ''
# This include the list of parameters passed by the user in Fast Execution Mode
parametersList=[]
# A boolean for fast Execution Button mode( if flag%2==0 then open window for user to enter his code,
# otherwise it executes it if user press again)
flag=1

"""
########################################################################################################################
 Global function section used in various places
########################################################################################################################
"""
""" 
Lists serial port names
:raises EnvironmentError: On unsupported or unknown platforms
:returns: A list of the serial ports available on the system
 """

def serialPorts():

    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

""" 
defining a new Slot (takes string)
Actually I could connect the (mainwindow) class directly to the (widget class) but I've made this function in between 
for futuer use.
All what it do is to take the (input string) and establish a connection with the widget class, send the string to it.
 """

@pyqtSlot(str)
def reading(s):
    newSignalConnection = Signal()
    newSignalConnection.reading.connect(Widget.Saving)
    newSignalConnection.reading.emit(s)

# same as reading Function
@pyqtSlot(str)
def Openning(s):
    newSignalConnection = Signal()
    newSignalConnection.reading.connect(Widget.Open)
    newSignalConnection.reading.emit(s)

""" 
This new added feature check the file extension based on user event and set the suitable format for the language 
used by the file.
Also it prints on the screen the type of file the user chooses
"""

def automaticFileExtensionSetter(fileName):

    global filePathForSelectedFile

    # First case for C# file: set format and print a message on the editor
    if fileName and fileName.lower().endswith(('.cs')):
        CSharpFormat.CSharpHighlighter(text)
        text2.clear()
        text2.append('C# file has been selected')

    # second case for Python file: set format and print a message on the editor
    if fileName and fileName.lower().endswith(('.py')):
        Python_Coloring.PythonHighlighter(text)
        text2.clear()
        text2.append('Python file has been selected')

    # Open file and display it in the editor tab
    if fileName:
        filePathForSelectedFile = fileName
        file = open(fileName, 'r')
        with file:
            data = file.read()
            text.setText(data)

"""
Main section for the fast execution mode .
the fast execution calls your function here and specify the parameters
"""

def main():
    global parametersList
    FastExecution.testedFunction(parametersList)

"""
########################################################################################################################
Signal class that initializing a Signal which will take (string) as an input
########################################################################################################################
"""
class Signal(QObject):

    reading = pyqtSignal(str)
    # init Function for the Signal class
    def __init__(self):
        QObject.__init__(self)

"""
########################################################################################################################
TextWidget class which is made to connect the QTab with the necessary layouts.
Class which is made to implement some usage from the Python_coloring.py file to color the code written in
the editor tab of the program in the widget class. Function used (itUI).
########################################################################################################################
"""

class TextWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.itUI()
    def itUI(self):
        global text
        text = QTextEdit()
        hbox = QHBoxLayout()
        hbox.addWidget(text)
        self.setLayout(hbox)

"""
########################################################################################################################
Widget class the main application window implementation that appears, opening and saving functionality for a file. 
Functions used (initUI, saving, openMenuButton, onClickedFromLeftTab).
########################################################################################################################
"""
class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # This widget is responsible of making Tab in IDE which makes the Text editor looks nice
        tab = QTabWidget()
        tx = TextWidget()
        tab.addTab(tx, "Tab"+"1")

        # second editor in which the error messeges and succeeded connections will be shown
        global text2
        text2 = QTextEdit()
        text2.setReadOnly(True)

        # defining a Treeview variable to use it in showing the directory included files
        self.treeview = QTreeView()

        # making a variable (path) and setting it to the root path (surely I can set it to whatever the root I want,
        # not the default)
        #path = QDir.rootPath()
        path = QDir.currentPath()

        # making a Filesystem variable, setting its root path and applying somefilters (which I need) on it
        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(QDir.rootPath())

        # NoDotAndDotDot => Do not list the special entries "." and "..".
        # AllDirs =>List all directories; i.e. don't apply the filters to directory names.
        # Files => List files.
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)
        self.treeview.setModel(self.dirModel)
        self.treeview.setRootIndex(self.dirModel.index(path))
        self.treeview.clicked.connect(self.onClickedFromLeftTab)

        Left_hbox = QHBoxLayout()
        Right_hbox = QHBoxLayout()

        # after defining variables of type QVBox and QHBox
        # I will Assign treevies variable to the left one and the first text editor in which the code will be written
        # to the right one
        Left_hbox.addWidget(self.treeview)
        Right_hbox.addWidget(tab)

        # defining another variable of type Qwidget to set its layout as an QHBoxLayout
        # I will do the same with the right one
        Left_hbox_Layout = QWidget()
        Left_hbox_Layout.setLayout(Left_hbox)

        Right_hbox_Layout = QWidget()
        Right_hbox_Layout.setLayout(Right_hbox)

        # I defined a splitter to seperate the two variables (left, right) and make it more easily to change the space
        # between them
        H_splitter = QSplitter(Qt.Horizontal)
        H_splitter.addWidget(Left_hbox_Layout)
        H_splitter.addWidget(Right_hbox_Layout)
        H_splitter.setStretchFactor(1, 1)

        # I defined a new splitter to seperate between the upper and lower sides of the window
        V_splitter = QSplitter(Qt.Vertical)
        V_splitter.addWidget(H_splitter)
        V_splitter.addWidget(text2)

        Final_Layout = QHBoxLayout(self)
        Final_Layout.addWidget(V_splitter)

        self.setLayout(Final_Layout)

    # defining a new Slot (takes string) to saveMenuButton the text inside the first text editor
    @pyqtSlot(str)
    def Saving(s):
        name = os.path.basename(filePathForSelectedFile)
        if name != '':
            with open(name, 'w') as file:
                TEXT = text.toPlainText()
                file.write(TEXT)
                file.flush()
                os.fsync(file.fileno())
                file.close()

    # defining a new Slot (takes string) to set the string to the text editor
    @pyqtSlot(str)
    def Open(s):
        global text
        text.setText(s)

    # Function gets called when the user click on a file from the left hand tab.
    # It focus on the file extension in order to select which format to use for displaying the code(PYTHON/CSHARP).
    def onClickedFromLeftTab(self, index):
        filePath = self.sender().model().filePath(index)
        filePath = tuple([filePath])
        automaticFileExtensionSetter(filePath[0])


"""
########################################################################################################################
UI class holds the main functionality of the project as for example creating
signal connection, creating the menu items, shortcuts, creating a widget (main window for the application) instance, run 
the program, saveMenuButton and openMenuButton files buttons. Functions used (InitUI, RunMenuButton, PortClickedMenuButton, saveMenuButton, openMenuButton)
########################################################################################################################
"""
class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.intUI()

    def intUI(self):
        self.portFlag = 1
        self.newSignalConnection = Signal()

        self.Open_Signal = Signal()

        # connecting (self.Open_Signal) with Opening function
        self.Open_Signal.reading.connect(Openning)

        # connecting (self.newSignalConnection) with reading function
        self.newSignalConnection.reading.connect(reading)

        # creating menu items
        menu = self.menuBar()

        # I have three menu items
        fileMenu = menu.addMenu('File')
        Port = menu.addMenu('Port')
        Run = menu.addMenu('Run')
        fastExecutionMode = menu.addMenu('Fast Execution Mode')

        # As any PC or laptop have many ports, so I need to list them to the User
        # so I made (Port_Action) to add the Ports got from (serialPorts()) function
        # copyrights of serialPorts() function goes back to a guy from stackoverflow(whome I can't remember his name), so thank you (unknown)
        Port_Action = QMenu('port', self)

        res = serialPorts()

        for i in range(len(res)):
            s = res[i]
            Port_Action.addAction(s, self.PortClickedMenuButton)

        # adding the menu which I made to the original (Port menu)
        Port.addMenu(Port_Action)

        # Making and adding RunMenuButton Actions
        FastExecutionAction = QAction("Change Mode", self)
        FastExecutionAction.triggered.connect(self.fastExecutionAlgorithm)
        fastExecutionMode.addAction(FastExecutionAction)

        RunAction = QAction("RunMenuButton", self)
        RunAction.triggered.connect(self.RunMenuButton)
        Run.addAction(RunAction)

        # Making and adding File Features
        Save_Action = QAction("Save", self)
        Save_Action.triggered.connect(self.saveMenuButton)
        Save_Action.setShortcut("Ctrl+S")

        Save_As_Action = QAction("Save As", self)
        Save_As_Action.triggered.connect(self.saveAsMenuButton)
        Save_As_Action.setShortcut("Ctrl+x")

        Close_Action = QAction("Close", self)
        Close_Action.setShortcut("Alt+c")
        Close_Action.triggered.connect(self.close)

        Open_Action = QAction("Open", self)
        Open_Action.setShortcut("Ctrl+O")
        Open_Action.triggered.connect(self.openMenuButton)

        fileMenu.addAction(Save_As_Action)
        fileMenu.addAction(Save_Action)
        fileMenu.addAction(Close_Action)
        fileMenu.addAction(Open_Action)

        # Seting the window Geometry
        self.setGeometry(200, 150, 600, 500)
        self.setWindowTitle('Anubis IDE')
        self.setWindowIcon(QtGui.QIcon('Anubis.png'))

        widget = Widget()

        self.setCentralWidget(widget)
        self.show()

    ###########################        Start Of the Functions          ##################
    def RunMenuButton(self):
        if self.portFlag == 0:
        #
        ##### Compiler Part which is still missied
        #
            text2.append("Sorry, there is no attached compiler.")

        else:
            text2.append("Please Select Your Port Number First")

    # This function is made to get which port was selected by the user
    @QtCore.pyqtSlot()
    def PortClickedMenuButton(self):
        action = self.sender()
        self.portNo = action.text()
        self.portFlag = 0

    # This function to saveMenuButton the code into a file
    def saveMenuButton(self):
        self.newSignalConnection.reading.emit("name")

    # New added functionality for saveAs files to support both python and CSharp
    def saveAsMenuButton(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        if name[0] !='' and name[0] !='FastExecution.py':
            with open(name[0], 'w') as file:
                TEXTData = text.toPlainText()
                file.write(TEXTData)
                file.close()

    # This function to openMenuButton a file and exhibits it to the user in a text editor
    def openMenuButton(self):
        fileName = QFileDialog.getOpenFileName(self,'Open File','/home')
        automaticFileExtensionSetter(fileName[0])


    """
    New added feature to the system, it include the fast execution mode.
    A fast executed for python code: in this feature the editor user will enter a code for a single function that would
    be automatically wrapped inside a program that has a main function that will call the the function.
    The user would be asked to also to provide a list of parameters to be passed from the main to the called function
    """
    def fastExecutionAlgorithm(self):
        global flag
        flag=flag+1

        # first of all it opens a new window with the location to place the user code for testing
        if flag % 2 == 0 :
            text2.clear()
            text2.append("Fast Execution mode Applied")
            automaticFileExtensionSetter('FastExecution.py')
            text2.clear()

        # the user execute the function he wrote, the program will ass the user to specify the list of parameters.
        # the output for the execution will be printed on the editor GUI
        else :
            text, okPressed = QInputDialog.getText(self, "Parameters", "Place Your Parametes (use , to seperate them)", QLineEdit.Normal, "")
            if okPressed and text != '':
                text2.clear()
                global parametersList
                parametersList = text.split(",")
                codeOut = StringIO()
                codeErr = StringIO()
                sys.stdout = codeOut
                sys.stderr = codeErr

                # this line will execute the needed code the user made
                eval(compile('main()', '', 'eval'))
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
                text2.append(codeOut.getvalue())
                text2.append(codeErr.getvalue())
                codeOut.close()
                codeErr.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    # ex = Widget()
    sys.exit(app.exec_())
