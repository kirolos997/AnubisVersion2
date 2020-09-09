"""
Introduction: this file includes all reserved words used in CSharp language and used in CSharpFormat.py file.
3 sections :reservedKeywordsCSharp, reservedOperatorsCSharp, reservedBracesCSharp
########################################################################################################################

Reserved identifiers that have special meanings to the compiler in C#.
They cannot be used as identifiers in your program unless they include @ as a prefix.
Link Microsoft doc: https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/
"""
reservedKeywordsCSharp = [
    'abstract', 'as', 'base', 'bool', 'break', 'byte',
    'case', 'catch', 'char', 'checked', 'class', 'const',
    'continue', 'decimal', 'default', 'delegate',
    'do', 'double', 'else', 'enum',
    'event', 'explicit', 'extern', 'false',
    'finally', 'fixed', 'float', 'for',
    'foreach', 'goto', 'if', 'implicit',
    'in', 'int', 'interface', 'internal',
    'is', 'lock', 'long', 'namespace',
    'new', 'null', 'object', 'operator',
    'out', 'override', 'params', 'private',
    'protected', 'public', 'readonly', 'ref',
    'return', 'sbyte', 'sealed', 'short',
    'sizeof', 'stackalloc', 'static', 'string',
    'struct', 'switch', 'this', 'throw',
    'true', 'try', 'typeof', 'uint',
    'ulong', 'unchecked', 'unsafe', 'ushort',
    'using', 'virtual', 'void', 'volatile',
    'while', 'add', 'alias', 'ascending',
    'async', 'await', 'by', 'descending', 'dynamic',
    'equals', 'from', 'get', 'global',
    'group', 'into', 'join', 'let', 'nameof', 'notnull',
    'on', 'orderby', 'partial', 'remove', 'select',
    'set', 'unmanaged', 'value', 'var', 'when', 'where', 'yield'
]

""" 
########################################################################################################################
 Operators that have special meanings to the compiler in C#.
 Documentation link: https://www.programiz.com/csharp-programming/operators
 ########################################################################################################################
 """
reservedOperatorsCSharp = [
    # Assignment Operators
    '=',
    # Arithmetic Operators
    '\+', '-', '\*', '/', '\%',
    # Relational Operators
    '==', '!=', '<', '<=', '>', '>=',
    # Logical Operators
    'true', 'false',
    # Bitwise Operators
    '\^', '\|', '\&', '\~', '>>', '<<',
    # Compound Assignment Operators
    '\+=', '\-=', '\*=', '\%=', '\&=', '\|=', '^=', '<<=', '>>=', '=>',
    # Unary operation
    '++', "--", '!',
]

""" 
########################################################################################################################
Reserved braces used in programing and special meanings to the compiler in C#.
Documentation link: https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/
########################################################################################################################
"""
reservedBracesCSharp = [
    '\{', '\}', '\(', '\)', '\[', '\]',
]