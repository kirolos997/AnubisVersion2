"""
Introduction: this file includes regular expression for Csharp language and used in CSharpFormat.py file.
########################################################################################################################
"""
import ReservedCSharpIdentifiers
import CSharpStyleAndColors

# Using reserved keywords, operators, braces defined in ReservedCSharpIdentifiers.py file
stylesCSharp = CSharpStyleAndColors.stylesCSharp
reservedKeywords = ReservedCSharpIdentifiers.reservedKeywordsCSharp
reservedOperators = ReservedCSharpIdentifiers.reservedOperatorsCSharp
reservedBraces = ReservedCSharpIdentifiers.reservedBracesCSharp


regexRules = []
# Keyword, operator, and brace regexRules
regexRules += [(r'\b%s\b' % word, 0, stylesCSharp['keywords'])
               for word in reservedKeywords]

regexRules += [(r'%s' % operator, 0, stylesCSharp['operator'])
               for operator in reservedOperators]

regexRules += [(r'%s' % brace, 0, stylesCSharp['brace'])
               for brace in reservedBraces]

# All other regexRules
regexRules += [

    # Double-quoted string, possibly containing escape sequences
    (r'"[^"\\]*(\\.[^"\\]*)*"', 0, stylesCSharp['stringQuotes']),

    # Single-quoted string, possibly containing escape sequences
    (r"'[^'\\]*(\\.[^'\\]*)*'", 0, stylesCSharp['stringQuotes']),

    # 'class' followed by an identifier
    (r'\bclass\b\s*(\w+)', 1, stylesCSharp['className']),

    # 'namespace' followed by an identifier
    (r'\bnamespace\b\s*(\w+)', 1, stylesCSharp['className']),

    # a word followed by a dot followed by another word
    (r'\w*\.\w*', 0, stylesCSharp['functionalities']),

    # From '//' until a newline
    (r'//[^\n]*', 0, stylesCSharp['comment']),

    # MultiLine comment
    (r'/\*(?:(?!\*/).)*\*/', 0, stylesCSharp['comment']),

    # Numeric literals
    (r'\b[+-]?[0-9]+[lL]?\b', 0, stylesCSharp['numbers']),
    (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, stylesCSharp['numbers']),
    (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, stylesCSharp['numbers']),
]
