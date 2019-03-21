#!/usr/bin/python3

# --------------------- LEX ---------------------------

# TOKENS
reserved_words = {
    # reserved words code
    "max": "MAX",
    "min": "MIN",
    "program": "PROGRAM",
    "script": "SCRIPT",
    # Data types
    "False": "FALSE",
    "True": "TRUE",
    "bool": "BOOL",
    "double": "DOUBLE",
    "else": "ELSE",
    "if": "IF",
    "int": "INT",
    "loop": "LOOP",
    "str": "STR",
    # Functions
    "def": "DEF",
    "eval": "EVAL",
    "spit": "SPIT",
    # Special Functions
    "avg": "AVG",
    "find_max": "FIND_MAX",
    "find_min": "FIND_MIN",
    "median_1Dslice": "MEDIAN",
    "mode_1Dslice": "MODE",
    "multiply_1Dslice": "MULTIPLY_1DSLICE",
    "pow": "POW",
    "randoms": "RANDOMS",
    "sort_slice": "SORT_SLICE",
    "suck_csv": "SUCK_CSV",
    "zeros": "ZEROS",
    # reserved words html
    "class": "CLASS",
    "div": "DIV",
    "embed": "EMBED",
    "h1": "H1",
    "h2": "H2",
    "p": "P",
    "table": "TABLE",
    "th": "TH",
    "tr": "TR",
}

tokens = list(reserved_words.values()) + [
    "ASSOCIATIVE",
    "CBRACE",
    "CBRACK",
    "CEVALSCRIPT",
    "COLON",
    "COMMA",
    "CPAREN",
    "CTED",
    "CTEI",
    "CTESTR",
    "EQ",
    "ID",
    "OBRACE",
    "OBRACK",
    "OEVALSCRIPT",
    "OP",
    "OPAREN",
    "REL",
    "SIGN",
]

t_SIGN = r"\+|-"
t_OP = r"\*|/"
t_ASSOCIATIVE = r"or|and"
t_EQ = r"="
t_COMMA = r","
t_COLON = r":"
t_OPAREN = r"\("
t_CPAREN = r"\)"
t_OBRACE = r"\{"
t_CBRACE = r"\}"
t_OBRACK = r"\["
t_CBRACK = r"\]"


def t_OEVALSCRIPT(t):
    r"<\^"
    return t


def t_REL(t):
    r"is|not|>=|<=|>|<"
    return t


def t_CEVALSCRIPT(t):
    r"\^>"
    return t


def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"
    t.type = reserved_words.get(t.value, "ID")
    return t


def t_CTED(t):
    r"(-?[0-9]+[.])[0-9]+"
    return t


def t_CTEI(t):
    r"-?[0-9]+"
    return t


def t_CTESTR(t):
    r"\"[^\"]*\""
    return t


# Ignored
t_ignore = " \t"


def t_newline(t):
    r"\n+"
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Discarded tokens
# Reference: https://www.dabeaz.com/ply/ply.html#ply_nn8
def t_COMMENT(t):
    r"\#.*"
    pass
    # No return value. Token discarded


# Build the lexer
import ply.lex as lex

lexer = lex.lex()
