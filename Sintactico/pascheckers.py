from errors import error
from astobjects import *
from typesys import *
from parser import *
import sys

class CheckProgramVisitor(NodeVisitor):

    def __init__(self):
        self.symbols = {}
        self.temp_symbols = {}
        self.expected_ret_type = None
        self.current_ret_type = None
        self.functions = {}
        self.keywords = [t.name for t in DType.__subclasses__()]

    def visit_OneVarDeclaration(self,node):
        if node.identifier.value in self.keywords:
            error(node.lineno, f"Nombre '{node.identifier.value}' no es un nombre legal para declaración de variable")
            return

        if node.identifier.value not in self.symbols:
            self.visit(node.type)
            node.type = node.type.type.type_identifier.identifier.value
            if node.type in self.keywords:
                self.symbols[node.identifier.value] = node.type
            else:
                error(node.lineno, f"Tipo desconocido '{node.type}'")
        else:
            error(node.lineno, f"'{node.identifier.value}' ya se ha definido")

    def visit_MuchVarDeclaration(self,node):
        listId = self.return_ListIdentifier(node.list_identifier)
        for id in listId:
            if id.value in self.keywords:
                error(node.lineno, f"Nombre '{id.value}' no es un nombre legal para declaración de variable")
                return

            if id.value not in self.symbols:
                self.visit(node.type)
                type = node.type.type.type_identifier.identifier.value
                if type in self.keywords:
                    self.symbols[id.value] = type
                else:
                    error(node.lineno, f"Tipo desconocido '{type}'")
            else:
                error(node.lineno, f"'{node.identifier.value}' ya se ha definido")


    def return_ListIdentifier(self,node):
        if not isinstance(node.identifier, list):
            return self.return_ListIdentifier(node.identifier)
        if isinstance(node.identifier, list):
            return node.identifier


    def visit_ConstantDefinition(self,node):
        node.type = None
        if node.id.value not in self.symbols:
            #validación de tipo:
            if(type(node.constant) == int):
                node.type = 'integer'
            if(type(node.constant) == str):
                node.type = 'char'
            self.symbols["constante " + node.id.value] = node.type
        else:
            error(node.lineno, f"'{node.id.value}' ya se ha definido")


    def visit_AssignamentStatementEntire(self,node):
        self.visit(node.expression)
        cons = "constante " + node.identifier.value
        if node.identifier.value in self.symbols or cons in self.symbols:
            if cons in self.symbols:
                error(node.lineno, f"No se puede escribir a constante '{node.identifier.value}'")

            if node.identifier.value in self.symbols:
                typeVar = self.symbols[node.identifier.value]
                typeExp = node.expression.type
                if typeVar != typeExp:
                    error(node.lineno,f"No se puede asignar el tipo '{node.expression.type}' a variable '{node.identifier.value}' de tipo '{typeVar}'")



    def visit_Variable(self,node):
        node.type = None
        if isinstance(node.var,EntireVariable):
            node.name = node.var.var.value
            if node.name not in self.symbols:
                error(node.lineno, f"Nombre '{node.name}' no esta definido")
            else:
                node.type = self.symbols[node.name]

    def visit_Factor(self,node):
        #node.type = None
        if type(node.value) == int:
            node.type = 'integer'
        if type(node.value) == str:
            node.type = 'char'
        if type(node.value) == Variable:
            self.visit(node.value)
            node.type = node.value.type
        if type(node.value) == Factor:
            self.visit(node.value)
            node.type = node.value.type

    def visit_FactorPar(self,node):
        self.visit(node.factor)
        node.type = node.factor.type

    def visit_Expression(self,node):
        self.visit(node.simple)
        node.type = node.simple.type

    def visit_SimpleExpression(self,node):
        self.visit(node.term)
        self.visit(node.list)
        node.type = None
        if isinstance(node.list,ListAddingTerm):
            node.list.type = node.term.type
        if node.term.type == node.list.type:
            node.type = node.term.type
        else:
            error(node.lineno, f"Error: Tipos de datos incompatibles en expresión")

    def visit_Term(self,node):
        node.type = None
        self.visit(node.factor)
        self.visit(node.list_mult_factor)
        if node.list_mult_factor == None:
            node.type = node.factor.type
        elif isinstance(node.list_mult_factor,ListMultFactor):
            node.type = node.factor.type
        elif node.factor.type == node.list_mult_factor.type:
            node.type = node.factor.type
        else:
            error(node.lineno, f"Error: Tipos de datos incompatibles en expresión")



    def visit_BinaryOp(self,node):
        self.visit(node.left)
        self.visit(node.right)
        node.type = None
        #print(node.op.value,node.left)
        if isinstance(node.left, ListMultFactor):
            node.left.type = node.right.type
        if isinstance(node.left, ListAddingTerm):
            node.left.type = node.right.type
        if node.right.type == node.left.type:
            node.type = node.right.type
            #print(node.type)
