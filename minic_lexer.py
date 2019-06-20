import ply.lex as lex
import sys

# list of tokens
tokens = (
    #RESERVED WORDS
    'AND','ARRAY','BEGIN','CASE','CONST','DIV','DO',
    'DOWNTO','ELSE','END','FILE','FOR','FUNCTION','GOTO','IF',
    'IN','LABEL','MOD','NIL','NOT','OF','OR','PACKED',
    'PROCEDURE','PROGRAM','RECORD','REPEAT','SET','THEN',
    'TO','TYPE','UNTIL','VAR','WHILE','WITH',

    #REQUIRED IDENTIFIERS
    'INTEGER','REAL','CHAR','BOOLEAN','ABS','ARCTAN',
    'CHR','COS','DISPOSE','EOF','EOLN','EXP','FALSE','GET',
    'INPUT','LN','MAXINT','NEW','ODD','ORD','OUTPUT','PACK',
    'PAGE','PRED','PUT','READ','READLN','RESET','REWRITE',
    'ROUND','SIN','SQR','SQRT','SUCC','TEXT','TRUE','TRUNC',
    'UNPACK','WRITE','WRITELN','STRING',

    #REGULAR EXPRESSIONS RULES FOR A SIMPLE TOKENS
    'PLUS','MINUS','TIMES','DIVIDE','EQUAL','DISTINT',
    'LESS','GREATER','SEMICOLON','COMMA','LPAREN','RPAREN',
    'LBRACKET','RBRACKET','COLON','AMPERSANT',
    'HASHTAG','DOT','SIMPLE', 'COMMENT', 'OPENCOMMENT','CLOSECOMMENT',
    'OPENCOMMENT2','CLOSECOMMENT2',

    #IDENTIFIER AND NUMBER
    'ID','NUMBER'
)

# Regular expressions rules for a simple tokens 
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_EQUAL  = r'='
t_DISTINT = r'!'
t_LESS   = r'<'
t_GREATER = r'>'
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON   = r':'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_SIMPLE = r'\''
t_STRING = r'\'[a-zA-Z_][a-zA-Z_0-9 ]*\''
t_COMMENT = r'\//'
t_OPENCOMMENT = r'\(\*'
t_CLOSECOMMENT = r'\*\)'
t_OPENCOMMENT2   = r'{'
t_CLOSECOMMENT2   = r'}'


def t_ABS(t):
    r'abs'
    return t

def t_AND(t):
    r'and'
    return t

def t_ARCTAN(t):
    r'arctan'
    return t

def t_ARRAY(t):
    r'array'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_CHR(t):
    r'chr'
    return t

def t_CONST(t):
    r'const'
    return t

def t_COS(t):
    r'cos'
    return t

def t_DISPOSE(t):
    r'dispose'
    return t

def t_DIV(t):
    r'div'
    return t

def t_DO(t):
    r'do'
    return t

def t_DOWNTO(t):
    r'downto'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_END(t):
    r'end'
    return t 

def t_EOF(t):
    r'eof'
    return t

def t_EOLN(t):
    r'eoln'
    return t

def t_EXP(t):
    r'exp'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_FILE(t):
    r'file'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_GET(t):
    r'get'
    return t

def t_GOTO(t):
    r'goto'
    return t

def t_IF(t):
    r'if'
    return t

def t_IN(t):
    r'in'
    return t

def t_INPUT(t):
    r'input'
    return t

def t_INTEGER(t):
    r'integer'
    return t

def t_LABEL(t):
    r'label'
    return t

def t_LN(t):
    r'ln'
    return t

def t_MAXINT(t):
    r'maxint'
    return t

def t_MOD(t):
    r'mod'
    return t

def t_NEW(t):
    r'new'
    return t

def t_NIL(t):
    r'nil'
    return t

def t_NOT(t):
    r'not'
    return t

def t_ODD(t):
    r'odd'
    return t

def t_OF(t):
    r'of'
    return t

def t_OR(t):
    r'or'
    return t

def t_ORD(t):
    r'ord'
    return t

def t_OUTPUT(t):
    r'output'
    return t

def t_PACK(t):
    r'pack'
    return t

def t_PACKED(t):
    r'packed'
    return t

def t_PAGE(t):
    r'page'
    return t

def t_PRED(t):
    r'pred'
    return t

def t_PROCEDURE(t):
    r'procedure'
    return t

def t_PROGRAM(t):
    r'program'
    return t

def t_PUT(t):
    r'put'
    return t

def t_READ(t):
    r'read'
    return t

def t_READLN(t):
    r'readln'
    return t

def t_RECORD(t):
    r'record'
    return t

def t_REPEAT(t):
    r'repeat'
    return t

def t_RESET(t):
    r'reset'
    return t

def t_REAL(t):
    r'real'
    return t

def t_REWRITE(t):
    r'rewrite'
    return t

def t_ROUND(t):
    r'round'
    return t

def t_SET(t):
    r'set'
    return t

def t_SIN(t):
    r'sin'
    return t

def t_SQR(t):
    r'sqr'
    return t

def t_SQRT(t):
    r'sqrt'
    return t

def t_SUCC(t):
    r'succ'
    return t

def t_TEXT(t):
    r'text'
    return t

def t_THEN(t):
    r'then'
    return t

def t_TRUE(t):
    r'true'
    return t

def t_TRUNC(t):
    r'trunc'
    return t

def t_TO(t):
    r'to'
    return t

def t_TYPE(t):
    r'type'
    return t

def t_UNPACK(t):
    r'unpack'
    return t

def t_UNTIL(t):
    r'until'
    return t

def t_VAR(t):
    r'var'
    return t

def t_WHILE(t):
    r'while'
    return t



def t_WITH(t):
    r'with'
    return t

def t_WRITE(t):
    r'write'
    return t

def t_WRITELN(t):
    r'writeln'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_d_0-9]*'
    return t

t_ignore = ' \t'
    
def t_error(t):
   # print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)


    
def test(data, lexer):
	lexer.input(data)
	while True:
		tok = lexer.token()
		if not tok:
			break
		print (tok)

lexer = lex.lex()

 
if __name__ == '__main__':
	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = '/tests/test1.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

