import sys
from antlr4 import *
from lib.LOVELexer import LOVELexer
from lib.LOVEParser import LOVEParser
from ListenerInterp import ListenerInterp

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = LOVELexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LOVEParser(stream)
    tree = parser.prog()
    if parser.getNumberOfSyntaxErrors() > 0:
        print("syntax errors")
    else:
        linterp = ListenerInterp()
        walker = ParseTreeWalker()
        walker.walk(linterp, tree)

if __name__ == '__main__':
    main(sys.argv)