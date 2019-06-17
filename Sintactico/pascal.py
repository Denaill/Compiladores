from paslex import *
from parser import *
from astobjects import *
from pascheckers import *
from errors import *
import sys
import os

if __name__ == '__main__':
    file = "tests/charconst.pas"
    lexer = PascalLexer()
    if len(sys.argv) > 1:
        files = sys.argv[2:len(sys.argv)]
        if sys.argv[1] == "-l" or sys.argv[1] == "--lex":
            for f in files:
                if os.path.isfile(f):
                    printLex(f,lexer)
                else:
                    print("ERROR: The file %r does not exist" % f)
                print("-------------------------------------\n")

        elif sys.argv[1] == "-p":
            for f in files:
                if os.path.isfile(f):
                    lexer = PascalLexer()
                    parser = PasParser()
                    toopen = open(f)
                    code = toopen.read()
                    result = parser.parse(lexer.tokenize(code))
                    fSplit = f.split('/')
                    fPas = fSplit[-1]
                    fPasSplit = fPas.split('.')
                    nameFile = fPasSplit[0]
                    pathJPG = "astimage/" + nameFile + ".png"
                    if result:
                        print("\n\nParser succesfully. AST file's path:")
                        print(pathJPG)
                        result.graphprint(pathJPG)
                else:
                    print("ERROR: The file %r does not exist" % f)

        elif sys.argv[1] == "-s":
            for f in files:
                if os.path.isfile(f):
                    lexer = PascalLexer()
                    parser = PasParser()
                    toopen = open(f)
                    code = toopen.read()
                    result = parser.parse(lexer.tokenize(code))
                    fSplit = f.split('/')
                    fPas = fSplit[-1]
                    fPasSplit = fPas.split('.')
                    nameFile = fPasSplit[0]
                    pathJPG = "astimage/" + nameFile + ".png"
                    if result:
                        print("\n\nParser succesfully. AST file's path:")
                        print(pathJPG)
                        result.graphprint(pathJPG)

                    checker = CheckProgramVisitor()
                    checker.visit(result)
                    print(f"Program succesfully checked with '{errors_reported()}' errors")

                else:
                    print("ERROR: The file %r does not exist" % f)
