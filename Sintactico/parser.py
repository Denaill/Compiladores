from sly import Parser
from paslex import PascalLexer
from astobjects import *



class PasParser(Parser):

    tokens = PascalLexer.tokens

    precedence = (
        ('left', 'OR'),
		('left', 'AND'),
		('left', 'NOT'),
		('left', 'PLUS','MINUS'),
		('left', 'TIMES','DIV'),
        ('right', 'ELSE')
    )

    start = 'program'

    _leafRed = False
    _leafDec = False
    _leafBlue = False

    @_('PROGRAM identifier SEMICOLON block DOT')
    def program(self,p):
        return Program(p.identifier,p.block)

    @_('constant_declaration_part variable_declaration_part procedure_declaration_part function_declaration_part statement_part')
    def block(self,p):
        return Block(p.constant_declaration_part,p.variable_declaration_part,p.procedure_declaration_part,p.function_declaration_part,p.statement_part)

    @_('empty')
    def constant_declaration_part(self,p):
        return ConstantDeclarationPart([])

    @_('CONST list_constant_definition')
    def constant_declaration_part(self,p):
        return ConstantDeclarationPart(p.list_constant_definition)

    @_('constant_definition SEMICOLON')
    def list_constant_definition(self,p):
        return ListConstantDefinition([p.constant_definition])

    @_('constant_definition SEMICOLON list_constant_definition')
    def list_constant_definition(self,p):
        p.list_constant_definition.append(p[0])
        return ListConstantDefinition(p.list_constant_definition)

    @_('identifier EQ INTCONST')
    def constant_definition(self,p):
        return ConstantDefinition(p.identifier,p[2])

    @_('identifier EQ CHARCONST')
    def constant_definition(self,p):
        return ConstantDefinition(p.identifier,p[2])


    @_('empty')
    def variable_declaration_part(self,p):
        return Empty()

    @_('VAR list_variable_declaration')
    def variable_declaration_part(self,p):
        return VariableDeclatarionPart(p.list_variable_declaration)

    @_('var_declaration SEMICOLON')
    def list_variable_declaration(self,p):
        return ListVariableDeclaration([p.var_declaration])

    @_('var_declaration SEMICOLON list_variable_declaration')
    def list_variable_declaration(self,p):
        p.list_variable_declaration.append(p.var_declaration)
        return ListVariableDeclaration(p.list_variable_declaration)

    @_('identifier COLON type')
    def var_declaration(self,p):
        self._leafDec = True
        return OneVarDeclaration(p.identifier,p.type)

    @_('list_identifier COLON type')
    def var_declaration(self,p):
        return MuchVarDeclaration(p.list_identifier,p.type)

    @_('identifier')
    def list_identifier(self,p):
        return ListIdentifier([p.identifier])

    @_('identifier COMA list_identifier')
    def list_identifier(self,p):
        p.list_identifier.append(p.identifier)
        return ListIdentifier(p.list_identifier)

    @_('simple_type')
    def type(self,p):
        return Type(p.simple_type)

    @_('array_type')
    def type(self,p):
        return Type(p.array_type)

    @_('ARRAY LBR index_range RBR OF simple_type')
    def array_type(self,p):
        return ArrayType(p.index_range,p.simple_type)

    @_('INTCONST DOT DOT INTCONST')
    def index_range(self,p):
        return IndexRange(p[0],p[2])

    @_('type_identifier')
    def simple_type(self,p):
        return SimpleType(p.type_identifier)

    @_('identifier')
    def type_identifier(self,p):
        return TypeIdentifier(p.identifier)

    @_('list_procedure_declaration')
    def procedure_declaration_part(self,p):
        return ListProcedureDeclaration(p.list_procedure_declaration)

    @_('empty')
    def list_procedure_declaration(self,p):
        return ListProcedureDeclaration([])

    @_('procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        return ListProcedureDeclaration([p.procedure_declaration])

    @_('list_procedure_declaration procedure_declaration SEMICOLON')
    def list_procedure_declaration(self,p):
        p.list_procedure_declaration.append(p.procedure_declaration)
        return ListProcedureDeclaration(p.list_procedure_declaration)

    @_('PROCEDURE ID SEMICOLON block')
    def procedure_declaration(self,p):
        return ProcedureDeclaration(p[1],p.block)

    @_('list_function_declaration')
    def function_declaration_part(self,p):
        return FunctionDeclarationPart(p.list_function_declaration)

    @_('empty')
    def list_function_declaration(self,p):
        return ListFunctionDeclaration([])

    @_('function_declaration SEMICOLON')
    def list_function_declaration(self,p):
        return ListFunctionDeclaration([p.function_declaration])

    @_('list_function_declaration function_declaration SEMICOLON')
    def list_function_declaration(self,p):
        p.list_function_declaration.append(p.function_declaration)
        return ListFunctionDeclaration(p.list_function_declaration)

    @_('FUNCTION identifier formal_parameter COLON type_identifier SEMICOLON block')
    def function_declaration(self,p):
        return FunctionDeclaration(p.identifier,p.formal_parameter,p.type_identifier,p.block)

    @_('LPAR list_formal_parameter RPAR')
    def formal_parameter(self,p):
        return FormalParameter(p.list_formal_parameter)

    @_('formal_parameter_section')
    def list_formal_parameter(self,p):
        return ListFormalParameter([p.formal_parameter_section])

    @_('list_formal_parameter SEMICOLON formal_parameter_section')
    def list_formal_parameter(self,p):
        p.list_formal_parameter.append(p.formal_parameter_section)
        return ListFormalParameter(p.list_formal_parameter)

    @_('parameter_group')
    def formal_parameter_section(self,p):
        return FormalParameterSection(p.parameter_group)

    @_('VAR parameter_group')
    def formal_parameter_section(self,p):
        return FormalParameterSection(p.parameter_group)

    @_('FUNCTION parameter_group')
    def formal_parameter_section(self,p):
        return FormalParameterSection(p.parameter_group)

    @_('PROCEDURE parameter_group')
    def formal_parameter_section(self,p):
        return FormalParameterSection(p.parameter_group)

    @_('list_identifier COLON type_identifier')
    def parameter_group(self,p):
        return ParameterGroup(p.list_identifier,p.type_identifier)


    @_('compound_statement')
    def statement_part(self,p):
        return StatementPart(p.compound_statement)

    @_('BEGIN statement list_statement END')
    def compound_statement(self,p):
        return CompoundStatement(p.statement,p.list_statement)

    @_('SEMICOLON statement list_statement')
    def list_statement(self,p):
        p.list_statement.append(p.statement)
        return ListStatement(p.list_statement)

    @_('empty')
    def list_statement(self,p):
        return ListStatement([])

    @_('simple_statement')
    def statement(self,p):
        return Statement(p.simple_statement)

    @_('structured_statement')
    def statement(self,p):
        return Statement(p.structured_statement)

    @_('assignament_statement_entire')
    def simple_statement(self,p):
        return SimpleStatement(p.assignament_statement_entire)

    @_('assignament_statement_array')
    def simple_statement(self,p):
        return SimpleStatement(p.assignament_statement_array)

    @_('procedure_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.procedure_statement)

    @_('read_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.read_statement)

    @_('write_statement')
    def simple_statement(self,p):
        return SimpleStatement(p.write_statement)

    @_('identifier ASSIGN expression')
    def assignament_statement_entire(self,p):
        self._leafBlue = True
        return AssignamentStatementEntire(p.identifier,p.expression)

    @_('indexed_variable ASSIGN expression')
    def assignament_statement_array(self,p):
        return AssignamentStatementArray(p.indexed_variable,p.expression)

    @_('procedure_identifier LPAR parameter_list RPAR')
    def procedure_statement(self,p):
        return ProcedureStatement(p.procedure_identifier,p.parameter_list)

    @_('procedure_identifier')
    def procedure_statement(self,p):
        return ProcedureStatement(p.procedure_identifier,[])

    @_('actual_parameter')
    def parameter_list(self,p):
        return ParameterList([p.actual_parameter])

    @_('parameter_list COMA actual_parameter')
    def parameter_list(self,p):
        p.parameter_list.append(p.actual_parameter)
        return ParameterList(p.parameter_list)

    @_('expression')
    def actual_parameter(self,p):
        return ActualParameter([p.expression])

    @_('actual_parameter COLON expression')
    def actual_parameter(self,p):
        p.actual_parameter.append(p.expression)
        return ActualParameter(p.actual_parameter)

    @_('identifier')
    def procedure_identifier(self,p):
        return ProcedureIdentifier(p.identifier)

    @_('READ LPAR list_input_variable RPAR')
    def read_statement(self,p):
        return ReadStatement(p.list_input_variable)

    @_('input_variable')
    def list_input_variable(self,p):
        return ListInputVariable([p.input_variable])

    @_('list_input_variable COMA input_variable')
    def list_input_variable(self,p):
        p.list_input_variable.append(p.input_variable)
        return ListInputVariable(p.list_input_variable)

    @_('variable')
    def input_variable(self,p):
        return InputVariable(p.variable)

    @_('WRITE LPAR list_output_value RPAR')
    def write_statement(self,p):
        return WriteStatement(p.list_output_value)

    @_('output_value')
    def list_output_value(self,p):
        return ListOutputValue([p.output_value])

    @_('list_output_value COMA output_value')
    def list_output_value(self,p):
        p.list_output_value.append(p.output_value)
        return ListOutputValue(p.list_output_value)

    @_('expression')
    def output_value(self,p):
        return OutputValue(p.expression)

    @_('compound_statement')
    def structured_statement(self,p):
        return StructuredStatement(p.compound_statement)

    @_('if_statement')
    def structured_statement(self,p):
        return StructuredStatement(p.if_statement)

    @_('while_statement')
    def structured_statement(self,p):
        return StructuredStatement(p.while_statement)

    @_('IF expression THEN statement')
    def if_statement(self,p):
        return IfStatement(p.expression,p.statement,None)

    @_('IF expression THEN statement ELSE statement')
    def if_statement(self,p):
        return IfStatement(p.expression,p.statement0,p.statement1)

    @_('WHILE expression DO statement')
    def while_statement(self,p):
        return WhileStatement(p.expression,p.statement)

    @_('simple_expression')
    def expression(self,p):
        return Expression(p.simple_expression)

    @_('simple_expression relational_operator simple_expression')
    def expression(self,p):
        return BinaryOp(p.relational_operator,p.simple_expression0,p.simple_expression1)

    @_('sign term list_adding_term')
    def simple_expression(self,p):
        return SimpleExpression(p.sign,p.term,p.list_adding_term)

    @_('empty')
    def list_adding_term(self,p):
        return ListAddingTerm([],None)

    @_('list_adding_term adding_operator term')
    def list_adding_term(self,p):
        #p.list_adding_term.append(p.term)
        #return ListAddingTerm(p.list_adding_term,p.adding_operator)
        return BinaryOp(p.adding_operator,p.list_adding_term,p.term)

    @_('factor list_mult_factor')
    def term(self,p):
        return Term(p.factor,p.list_mult_factor)

    @_('empty')
    def list_mult_factor(self,p):
        return ListMultFactor([],None)

    @_('list_mult_factor multiplying_operator factor')
    def list_mult_factor(self,p):
        #p.list_mult_factor.append(p.factor)
        #return ListMultFactor(p.list_mult_factor,p.multiplying_operator)
        return BinaryOp(p.multiplying_operator,p.list_mult_factor,p.factor)

    @_('variable')
    def factor(self,p):
        return Factor(p[0])

    @_('INTCONST')
    def factor(self,p):
        return Factor(p[0],_leaf = True)

    @_('CHARCONST')
    def factor(self,p):
        return Factor(p[0],_leaf = True)

    @_('LPAR expression RPAR')
    def factor(self,p):
        return FactorPar(p[1],p[0],p[2])

    @_('NOT factor')
    def factor(self,p):
        return Factor(p[1])

    @_('procedure_statement')
    def factor(self,p):
        return Factor(p.procedure_statement)

    @_('EQ')
    def relational_operator(self,p):
        return RelationalOperator(p[0],_leaf = True)

    @_('NE')
    def relational_operator(self,p):
        return RelationalOperator(p[0],_leaf = True)

    @_('LT')
    def relational_operator(self,p):
        return RelationalOperator(p[0], _leaf = True)

    @_('LE')
    def relational_operator(self,p):
        return RelationalOperator(p[0], _leaf = True)

    @_('GE')
    def relational_operator(self,p):
        return RelationalOperator(p[0], _leaf = True)

    @_('GT')
    def relational_operator(self,p):
        return RelationalOperator(p[0], _leaf = True)

    @_('PLUS')
    def sign(self,p):
        return Sign(p[0], _leaf = True)

    @_('MINUS')
    def sign(self,p):
        return Sign(p[0], _leaf = True)

    @_('empty')
    def sign(self,p):
        return Sign(None)

    @_('PLUS')
    def adding_operator(self,p):
        return AddingOperator(p[0],_leaf = True)

    @_('MINUS')
    def adding_operator(self,p):
        return AddingOperator(p[0],_leaf = True)

    @_('OR')
    def adding_operator(self,p):
        return AddingOperator(p[0],_leaf = True)

    @_('TIMES')
    def multiplying_operator(self,p):
        return MultiplyingOperator(p[0],_leaf = True)

    @_('DIV')
    def multiplying_operator(self,p):
        return MultiplyingOperator(p[0],_leaf = True)

    @_('AND')
    def multiplying_operator(self,p):
        return MultiplyingOperator(p[0],_leaf = True)

    @_('entire_variable')
    def variable(self,p):
        return Variable(p.entire_variable)

    @_('indexed_variable')
    def variable(self,p):
        return Variable(p.indexed_variable)

    @_('array_variable LBR expression RBR')
    def indexed_variable(self,p):
        return IndexedVariable(p.array_variable,p.expression)

    @_('entire_variable')
    def array_variable(self,p):
        return ArrayVariable(p.entire_variable)

    @_('variable_identifier')
    def entire_variable(self,p):
        self._leafRed = True
        return EntireVariable(p.variable_identifier)

    @_('ID')
    def variable_identifier(self,p):
        line = p.lineno
        index = p.index
        if(self._leafRed):
            self._leafRed = False
            return VarID(p[0],_leafRed = True,_leaf = False,_leafBlue = False,_leafDec = False)
        if(self._leafDec):
            self._leafDec = False
            return VarID(p[0],_leafDec = True,_leaf = False,_leafBlue = False,_leafRed = False)
        if(self._leafBlue):
            self._leafBlue = False
            return VarID(p[0],_leafBlue = True,_leaf = False,_leafRed = False,_leafDec = False)
        return VarID(p[0],_leaf = True)

    @_('ID')
    def identifier(self,p):
        line = p.lineno
        index = p.index
        return Id(p[0],_leaf = True)

    @_('')
    def empty(self,p):
        return Empty()

if __name__ == '__main__':
    lexer = PascalLexer()
    parser = PasParser()
    toopen = open('tests/test1.pas')
    code = toopen.read()
    result = parser.parse(lexer.tokenize(code))
    if result:
        print("Parser succesfully")
