import ply.lex as lex
import sys

# list of tokens
tokens = (
    'BEGIN',
    'READ',
    'WRITE',
    'PROGRAM',
    'END',
    'ID',
    'NUMBER',

    #TOKENS
    'SEMICOLON',
    'COMMA',
    'LPAREN',
    'RPAREN',
    'PUNTO',
    'SIMPLE',
)

# Regular expressions rules for a simple tokens 
t_SEMICOLON = ';'
t_COMMA  = r','
t_LPAREN = r'\('
t_RPAREN  = r'\)'
t_PUNTO = r'\.'
t_SIMPLE = r'\''

def t_WRITE(t):
    r'write'
    return t

def t_BEGIN(t):
    r'begin'
    return t

def t_END(t):
    r'end'
    return t 

def t_READ(t):
    r'read'
    return t

def t_ID(t):
    r'\w+(_\d\w)*'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

""" 
def t_comments(t):
    r'(\*(.|\n)*?\*)'
    t.lexer.lineno += t.value.count('\n')

def t_comments_C99(t):
    r'{(.)*?\n\}'
    t.lexer.lineno += 1
"""
def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
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
		fin = 'hello.pas'
	f = open(fin, 'r')
	data = f.read()
	print (data)
	lexer.input(data)
	test(data, lexer)
	input()

