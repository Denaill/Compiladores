from sly import Lexer

class PascalLexer(Lexer):

    keywords = { 'program', 'var', 'array', 'of', 'procedure', 'begin', 'end',
                'write', 'read', 'if', 'then', 'else', 'while', 'do', 'not',
                'or', 'div', 'and','const','function'}
    tokens = { ID, INTCONST, CHARCONST, *{kw.upper() for kw in keywords},
                PLUS, MINUS, TIMES, EQ, NE, LT, GT, LE, GE, LPAR, RPAR, LBR,
                RBR, ASSIGN, DOT, COMA, SEMICOLON, COLON }

    #ignore = r' \t({([\n]|[.])*?})*'
    ignore = r' '

    ignore_comment = r'\(\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*?\*+\)|{[^{]*}'
    #ignore_comment = r'{[^}]*}'



    CHARCONST = r'\'[^\']*\'|"[^"]*"'
    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    LE = r'<='
    GE = r'>='
    EQ = r'='
    NE = r'<>'
    LT = r'<'
    GT = r'>'
    LPAR = r'\('
    RPAR = r'\)'
    LBR = r'\['
    RBR = r'\]'
    ASSIGN = r':='
    DOT = r'\.'
    COMA = r','
    SEMICOLON = r';'
    COLON = r':'

    @_(r'[a-zA-z][a-zA-Z0-9]*')
    def ID(self,t):
        if t.value.lower() in self.keywords:
            t.type = t.value.upper()
        return t

    @_(r'[0-9]+')
    def INTCONST(self,t):
        t.value = int(t.value)
        return t

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self,t):
        print("Line %d: Illegal character '%s'" % (self.lineno,t.value[0]))
        self.index += 1


def printLex(file,lexer):
    toopen = open(file)
    code = toopen.read()
    print("\t\t\tPROGRAM: %r\n\n" % (file))
    print("LEXER RESULTS:")
    for tok in lexer.tokenize(code):
        print('type=%r, value=%r' % (tok.type, tok.value))
