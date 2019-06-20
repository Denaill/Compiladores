import ply.yacc as yacc
from minic_lexer import tokens
import minic_lexer
import sys

VERBOSE = 1

def p_program (p):
    'program : PROGRAM ID SEMICOLON block'
    pass
def p_block (p):
    'block : variable_declaration_part procedure_declaration_part statement_part'
    pass
def p_variable_declaration_part (p):
    '''variable_declaration_part : empty
    | VAR variable_declaration SEMICOLON'''
    pass
def p_variable_declaration (p):
    'variable_declaration : ID COLON type'
    pass
def p_variable_declaration1 (p):
    'variable_declaration2 : ID COMMA variable_declaration2 COLON type '
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
    'type_identifier : ID'
    pass

#procedure 
def p_procedure_declaration_part (p):
    'procedure_declaration_part : empty'
    pass
def p_procedure_declaration_part2 (p):
    'procedure_declaration_part : procedure_declaration'
    pass
def p_procedure_declaration (p):
    'procedure_declaration : PROCEDURE ID SEMICOLON block '
    pass

# statement part 

def p_statement_part (p):
    'statement_part : compound_statement'
    pass
def p_compound_statement (p):
    'compound_statement : empty'
    pass
def p_compound_statement2 (p):
    'compound_statement : BEGIN statement SEMICOLON STATEMENT END'
    pass
def p_statement (p):
    'statement : simple_statement'
    pass
def p_statement2 (p):
    'statement : structured_statement'
    pass

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
def p_assignment_statement (p):
    'assignment_statement : variable'
    pass

def p_assignment_statement2 (p):
    'assignment_statement : expresion'
    pass
def p_procedure_statement(p):
    'procedure_statement : procedure_identifier'
    pass
def p_read_statement (p):
    'read_statement : READ LPAREN input_variable COMMA input_variable2 RPAREN'
    pass
def p_input_variable (p):
    'input_variable : variable'
    pass
def p_input_variable2 (p):
    '''input_variable2 : empty
                    | variable'''
    pass
def p_write_statement(p):
    'write_statement : WRITE LPAREN output_value comma output_variable2 RPAREN'
    pass
def p_output_value (p):
    'output_value : expression'
    pass
def p_output_value2 (p):
    '''output_value2 : empty
                     | expression'''
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
    'if_statement : IF expression THEN statement'
    pass
def p_if_statement2 (p):
    'if_statement : IF expression THEN statement ELSE statement'
    pass
def p_while_statement(p):
    'while_statement : WHILE expression  DO statement'
    pass
#expression 
def p_expression (p):
    'expression : simple_expression'
    pass
def p_expression2 (p):
    'expression : simple_expression relational_operator simple_expression'
    pass
def P_simple_expression (p):
    'simple_expression : sign term  adding_operator term' # ojo aqui, recordad el e
    pass
def p_term (p):
    'term : factor multiplying_operator factor' # ojo aqui, recordad el e
    pass



def p_empty(p):
    'empty : '
    pass
def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			print ("ERROR SINTACTICO EN LA LINEA: " + str(cminus_lexer.lexer.lineno))
	else:
		raise Exception('syntax', 'error')
		

parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'Sintactico/fibo.pas'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Amiguito, tengo el placer de informa que Tu parser reconocio correctamente todo")
	#input()

