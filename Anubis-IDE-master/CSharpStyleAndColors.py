"""
Introduction: this file includes styles used to color & format c# file and used in CSharpFormat.py file.
2 sections :format, stylesCSharp
########################################################################################################################
   A function that returns a QTextCharFormat with the given attributes passed.
########################################################################################################################
"""
from PyQt5.QtGui import QColor, QTextCharFormat, QFont


def format (color, style=''):

    # define 2 variables, one Constructs a color that is a copy of color.
    # The other focuses on the style which can be bold, italic or normal
    syntaxColor = QColor()
    syntaxFormat= QTextCharFormat()

    # check if a color is being passed and assign it as a foreground
    if type(color) is not str:
        syntaxColor.setRgb(color[0], color[1], color[2])
    else:
        syntaxColor.setNamedColor(color)
    syntaxFormat.setForeground(syntaxColor)

    # check if a style is being passed
    if 'bold' in style:
        syntaxFormat.setFontWeight(QFont.Bold)
    if 'italic' in style:
        syntaxFormat.setFontItalic(True)

    # return the format based on the given implementation and passed style
    return syntaxFormat
"""
###################################################################################################
    This section includes the style used by CSharp for formating the file.
    The chosen colors are based on the ones used in VSCode editor
###################################################################################################
"""
stylesCSharp = {
        # Reserved keywords coloring in C#
       'keywords': format('dodgerBlue'),

        # Operators coloring in C#
       'operator': format('red'),

        # Braces coloring in C#
       'brace': format('darkGray'),

        # Numbers coloring in C#
       'numbers': format('brown'),

        # Strings including: variablesName, functions  coloring in C#
       'string': format('black', 'italic'),

        # comment coloring in C#
       'comment': format('darkGreen', 'italic'),

        # className coloring in C#
       'className': format('mediumTurquoise', 'bold'),

        # String included in quotes coloring in C#
       'stringQuotes': format('orange'),

        # Functionalities built in like console. or imports inside in quotes coloring in C#
       'functionalities': format('darkMagenta','italic'),

   }
