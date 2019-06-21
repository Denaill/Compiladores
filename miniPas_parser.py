import ply.yacc as yacc
from minic_lexer import tokens
import minic_lexer
import sys
# falta la asignacion 
VERBOSE = 1

def p_program (p):
    'program : PROGRAM ID SEMICOLON block'
    pass
def p_block (p):
    'block : variable_declaration_part procedure_declaration_part statement_part'
    pass
def p_variable_declaration_part (p):
    '''variable_declaration_part : empty
                                 | VAR variable_declaration SEMICOLON variable_declaration_part 
                                 | CONST const_declaration SEMICOLON variable_declaration_part'''
    pass
def p_variable_declaration (p):
    'variable_declaration : ID  variable_declaration2 COLON type'
    pass
def p_variable_declaration1 (p):
    '''variable_declaration2 :  COMMA ID variable_declaration2  
                             | empty '''
    pass
def p_const_declaration(p):
    '''const_declaration : ID EQUAL NUMBER
                         | ID EQUAL STRING'''
    pass
def p_type (p):
    'type : simple_type'
    pass
def p_type2 (p):
    'type : array_type'
    pass
def p_array_type (p):
    'array_type : ARRAY LBRACKET index_range RBRACKET OF simple_type'
    pass
def p_index_range (p):
    'index_range : NUMBER DOT DOT NUMBER '
    pass
def p_simple_type (p):
    'simple_type : type_identifier'
    pass
# dudas en este identificador
def p_type_identifier (p):
    '''type_identifier : INTEGER
                       | CHAR
                       | BOOLEAN'''
    pass

#procedure 
def p_procedure_declaration_part (p):
    'procedure_declaration_part : empty'
    pass
def p_procedure_declaration_part2 (p):
    '''procedure_declaration_part : procedure_declaration
                                  | function_declaration'''
    pass
def p_procedure_declaration (p):
    'procedure_declaration : PROCEDURE ID SEMICOLON block'
    pass
def p_function_declaration (p):
    'function_declaration : FUNCTION ID LPAREN variable_declaration RPAREN COLON type SEMICOLON variable_declaration_part'
    pass
# call functions
def p_call_function (p):
    'call_function : ID LPAREN args RPAREN SEMICOLON'
    pass
def p_args (p):
    '''args : args args2
            | empty'''
def p_args2 (p):
    '''args2 : empty 
            | COMMA args
            | NUMBER COMMA args
            | STRING  args
            | ID
            | NUMBER
            | STRING'''
    pass
            
# statement part 
## problema aqui. no reconoce mas de una statement 
def p_statement_part (p):
    'statement_part : compound_statement '
    pass
# revisar 
""" def p_compound_statement (p):
    'compound_statement : empty'
    pass """
def p_compound_statement (p):
    'compound_statement : BEGIN statement  END DOT compound_statement2'
    pass
def p_compound_statement2 (p):
    '''compound_statement2 : empty
                            | compound_statement '''
    pass
def p_statement (p):
    'statement : simple_statement'
    pass
def p_statement4(p):
    'statement : statement  simple_statement'
    pass
def p_statement5(p):
    'statement : statement structured_statement'
    pass
def p_statement2 (p):
    'statement : structured_statement'
    pass
def p_statement3 (p):
    'statement3 : SEMICOLON statement'  
    pass

""" def p_statement3es (p):
    'statement3 : structured_statement'
    pass """

def p_statement3e (p):
    'statement3 : empty'
    pass
## call functions

    
# statement 
def p_simple_statement (p):
    'simple_statement : assignment_statement'
    pass
def p_simple_statemen1 (p):
    'simple_statement : procedure_statement'
    pass
def p_simple_statemen2 (p):
    'simple_statement : read_statement'
    pass
def p_simple_statemen3 (p):
    'simple_statement : write_statement'
    pass
def p_simple_statemen4 (p):
    'simple_statement : call_function'
    pass
def p_assignment_statement (p):
    'assignment_statement : variable COLON EQUAL expression SEMICOLON'
    pass


def p_procedure_statement(p):
    'procedure_statement : procedure_identifier'
    pass
def p_procedure_identifier (p):
    'procedure_identifier : ID'
def p_read_statement (p):
    'read_statement : READ LPAREN input_variable input_variable2 RPAREN SEMICOLON'
    pass
def p_input_variable (p):
    'input_variable : variable'
    pass
def p_input_variable2 (p):
    '''input_variable2 : empty
                    | COMMA variable'''
    pass
def p_write_statement(p):
    'write_statement : WRITE LPAREN output_value  output_value2 RPAREN SEMICOLON'
    pass
def p_output_value (p):
    '''output_value : expression
                    | STRING'''
    pass
def p_output_value2 (p):
    '''output_value2 : empty
                     | COMMA expression'''
    pass

#structured statement
def p_structured_statement(p):
    'structured_statement : compound_statement'
    pass
def p_structured_statement2(p):
    'structured_statement : if_statement'
    pass
def p_structured_statement3(p):
    'structured_statement : while_statement'
    pass

def p_if_statement (p):
    'if_statement : IF LPAREN expression RPAREN THEN statement'
    pass
def p_if_statement2 (p):
    'if_statement : IF LPAREN expression RPAREN THEN statement ELSE statement'
    pass
def p_while_statement(p):
    'while_statement : WHILE expression DO statement'
    pass
def p_while_statement2(p):
    'while_statement : WHILE expression DO BEGIN statement END SEMICOLON'
    pass
#expression 
def p_expression (p):
    'expression : simple_expression'
    pass
def p_expression2 (p):
    'expression : simple_expression relational_operator simple_expression'
    pass
def p_simple_expression (p):
    'simple_expression : sign term   simple_expression2' # ojo aqui, recordad el e (corregido)
    pass
# la siguiente parte de la expresion opcional
def p_simple_expression2 (p):
    '''simple_expression2 : adding_operator term
                          | empty'''
    pass

def p_term (p):
    'term : factor term2' # ojo aqui, recordad el e (corregido)
    pass
def p_term2 (p):
    '''term2 : multiplying_operator factor
             | empty'''

def p_factor (p):
    'factor : variable'
    pass

def p_factor2 (p):
    'factor : NUMBER'''
    pass
def p_factor3 (p):
    'factor : LPAREN expression RPAREN'
    pass
def p_factor4 (p):
    'factor : NOT factor'
    pass

def p_relational_operator (p):
    '''relational_operator : EQUAL 
                           | DISTINT
                           | LESS
                           | GREATER
                           | GREATER EQUAL
                           | LESS EQUAL'''
    pass
def p_sign (p):
    '''sign : PLUS
            | MINUS
            | empty'''
    pass
def p_adding_operator(p):
    '''adding_operator : PLUS
                       | MINUS
                       | OR'''
    pass
def p_multiplying_operator (p):
    '''multiplying_operator : TIMES 
                            | DIV
                            | AND'''

#Variable 
def p_variable (p):
    'variable : entire_variable'
    pass
def p_variable2 (p):
    'variable : indexed_variable'
    pass
def p_indexed_variable (p):
    'indexed_variable : array_variable LBRACKET expression RBRACKET'
    pass
def p_array_variable (p):
    'array_variable : entire_variable'
    pass
def p_entire_variable (p):
    'entire_variable : variable_identifier'
    pass
def p_variable_identifier (p):
    'variable_identifier : ID'
    pass



def p_empty(p):
    'empty :'
    pass

""" def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error') """
		
def p_error(p):
    print "syntax error", p
    print "line -> "+str(p.lineno)
parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Sintactico/tests/fibonacciMAL.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input()

