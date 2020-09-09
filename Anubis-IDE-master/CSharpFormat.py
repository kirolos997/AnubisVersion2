"""
###################################################################################################
    Importing the needed functionalities from PYQT5.
    PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in.
###################################################################################################
"""
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter
import CSharpRegex

"""Syntax highlighter for the Python language."""
class CSharpHighlighter(QSyntaxHighlighter):

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        # Creating Regular expression for CSharp code
        rules = CSharpRegex.regexRules

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)
