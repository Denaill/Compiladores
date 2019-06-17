from sly import Parser
import pydot

class AST(object):
    _fields = []
    def __init__(self,*args,**kwargs):
        self.return_type = None
        self.lineno = -1
        self.gen_location= None
        self.hasReturn = None
        #
        ####
        assert len(args) == len(self._fields)
        for name,value in zip(self._fields,args):
            setattr(self,name,value)
        if(len(kwargs)!=0):
            for name,value in kwargs.items():
                setattr(self,name,value)
        else:
            setattr(self,"_leaf",False)
            setattr(self,"_leafDec",False)
            setattr(self,"_leafRed",False)
            setattr(self,"_leafBlue",False)



        #setattr(self,"_leaf",False)

    def pprint(self):
        for depth, node in flatten(self):
            print("%s%s" % (" "*(4*depth),node))

    def graphprint(self,name):
        dotty=DotVisitor()
        dotty.visit(self)
        dotty.graph.write_png(name)
        '''dot = DotVisitor()
        print(dot)'''

def validate_fields(**fields):
    def validator(cls):
        old_init = cls.__init__
        def __init__(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            for field,expected_type in fields.items():
                assert isinstance(getattr(self, field), expected_type)
        cls.__init__ = __init__
        return cls
    return validator



class Program(AST):
    _fields = ['identifier','blocks']

class Block(AST):
    _fields = ['constant_declaration_part','variable_declaration_part','procedure_declaration_part', 'function_declaration_part','statement_part']

class ConstantDeclarationPart(AST):
    _fields = ['list_constant_definition']

class ListConstantDefinition(AST):
    _fields = ['constants']
    def append(self,e):
        self.constants.append(e)

class ConstantDefinition(AST):
    _fields = ['id','constant']

class VariableDeclatarionPart(AST):
    _fields = ['list_variable_declaration']

#@validate_fields(variables = list)
class ListVariableDeclaration(AST):
    _fields = ['variables']
    def append(self,e):
        self.variables.append(e)

class OneVarDeclaration(AST):
    _fields = ['identifier','type']

class MuchVarDeclaration(AST):
    _fields = ['list_identifier','type']

class ListIdentifier(AST):
    _fields = ['identifier']
    def append(self,e):
        self.identifier.append(e)

class Type(AST):
    _fields = ['type']

class ArrayType(AST):
    _fields = ['index_range','simple_type']

class IndexRange(AST):
    _fields = ['n1','n2']

class SimpleType(AST):
    _fields = ['type_identifier']

class TypeIdentifier(AST):
    _fields = ['identifier']

class ListProcedureDeclaration(AST):
    _fields = ['list_procedure_declaration']
    def append(self,e):
        self.list_procedure_declaration.append(e)

class ProcedureDeclaration(AST):
    _fields = ['identifier','block']

class FunctionDeclarationPart(AST):
    _fields = ['list_function_declaration']

class ListFunctionDeclaration(AST):
    _fields = ['list_function_declaration']
    def append(self,e):
        self.list_function_declaration.append(e)

class FunctionDeclaration(AST):
    _fields = ['identifier','formal_parameter','type_identifier','block']

class FormalParameter(AST):
    _fields = ['list_formal_parameter']

class ListFormalParameter(AST):
    _fields = ['list_formal_parameter']
    def append(self,e):
        self.list_formal_parameter.append(e)

class FormalParameterSection(AST):
    _fields = ['parameter_group']

class ParameterGroup(AST):
    _fields = ['list_identifier','type_identifier']

class StatementPart(AST):
    _fields = ['compound_statement']

class CompoundStatement(AST):
    _fields = ['statement','list_statement']

class ListStatement(AST):
    _fields = ['list_statement']
    def append(self,e):
        self.list_statement.append(e)

class Statement(AST):
    _fields = ['statement']

class SimpleStatement(AST):
    _fields = ['statement']

class AssignamentStatementArray(AST):
    _fields = ['variable','expression']

class AssignamentStatementEntire(AST):
    _fields = ['identifier','expression']

class ProcedureStatement(AST):
    _fields = ['procedure_identifier','parameter_list']

class ParameterList(AST):
    _fields = ['actual_parameter']
    def append(self,e):
        self.actual_parameter.append(e)

class ActualParameter(AST):
    _fields = ['actual_parameter']

class ProcedureIdentifier(AST):
    _fields = ['identifier']
    def append(self,e):
        self.actual_parameter.append(e)

class ReadStatement(AST):
    _fields = ['list_input_variable']

class ListInputVariable(AST):
    _fields = ['list_input_variable']
    def append(self,e):
        self.list_input_variable.append(e)

class InputVariable(AST):
    _fields = ['variable']

class WriteStatement(AST):
    _fields = ['list']

class ListOutputValue(AST):
    _fields = ['list_output_value']
    def append(self,e):
        self.list_output_value.append(e)

class OutputValue(AST):
    _fields = ['expression']

class StructuredStatement(AST):
    _fields = ['statement']

class IfStatement(AST):
    _fields = ['expression','statement1','statement2']

class WhileStatement(AST):
    _fields = ['expression','statement']

class Expression(AST):
    _fields = ['simple']

class SimpleExpression(AST):
    _fields = ['sign','term','list']

class ListAddingTerm(AST):
    _fields = ['list','op']
    def append(self,term):
        self.list.append(term)

class Term(AST):
    _fields = ['factor','list_mult_factor']

class ListMultFactor(AST):
    _fields = ['list_mult_factor','op']
    def append(self,factor):
        self.list_mult_factor.append(factor)

class Factor(AST):
    _fields = ['value']

class FactorVariable(AST):
    _fields = ['element']

class FactorPar(AST):
    _fields = ['factor','lpar','rpar']

class RelationalOperator(AST):
    _fields = ['value']

class Sign(AST):
    _fields = ['value']

class AddingOperator(AST):
    _fields = ['value']

class MultiplyingOperator(AST):
    _fields = ['value']

class Variable(AST):
    _fields = ['var']

class IndexedVariable(AST):
    _fields = ['var','exp']

class ArrayVariable(AST):
    _fields = ['var']

class EntireVariable(AST):
    _fields = ['var']

class VarID(AST):
    _fields = ['value']

class Id(AST):
    _fields = ['value']

class Empty(AST):
    _fields = []

class BinaryOp(AST):
    _fields = ['op','left','right']

class UnaryOp(AST):
    _fields = ['op','value']





class NodeVisitor(object):
    def visit(self,node):
        if node:
            method = 'visit_' + node.__class__.__name__
            visitor = getattr(self, method, self.generic_visit)
            return visitor(node)
        else:
            return None

    def generic_visit(self,node):
        for field in getattr(node,"_fields"):
            value = getattr(node,field,None)
            if isinstance(value, list):
                for item in value:
                    if isinstance(item,AST):
                        self.visit(item)
            elif isinstance(value, AST):
                self.visit(value)

# NO MODIFICAR
class NodeTransformer(NodeVisitor):
    def generic_visit(self,node):
        for field in getattr(node,"_fields"):
            value = getattr(node,field,None)
            if isinstance(value,list):
                newvalues = []
                for item in value:
                    if isinstance(item,AST):
                        newnode = self.visit(item)
                        if newnode is not None:
                            newvalues.append(newnode)
                    else:
                        newvalues.append(n)
                value[:] = newvalues
            elif isinstance(value,AST):
                newnode = self.visit(value)
                if newnode is None:
                    delattr(node,field)
                else:
                    setattr(node,field,newnode)
        return node

# NO MODIFICAR
def flatten(top):
    class Flattener(NodeVisitor):
        def __init__(self):
            self.depth = 0
            self.nodes = []
        def generic_visit(self,node):
            self.nodes.append((self.depth,node))
            self.depth += 1
            NodeVisitor.generic_visit(self,node)
            self.depth -= 1

    d = Flattener()
    d.visit(top)
    return d.nodes



class DotVisitor():
    graph = None
    def __init__(self):
        self.graph = pydot.Dot('AST', graph_type='digraph')
        self.id=0
    def ID(self):
        self.id+=1
        return self.id
        #return "n%d" %self.id

    def visit (self, node):
        if node:
            if(node._leaf):
                newname = self.visit_leaf(node)
            elif(node._leafRed):
                newname = self.visit_leafRed(node)
            elif(node._leafBlue):
                newname = self.visit_leafBlue(node)
            elif(node._leafDec):
                newname = self.visit_leafDec(node)
            else:
                method = 'visit_' + node.__class__.__name__
                visitor = getattr(self, method, self.visit_non_leaf)
                newname= visitor(node)

        self.graph.add_node(newname)
        return newname


    def visit_color(self,node,node_name,node_id,color):
        string= "N%d %s ( %s )" % (self.ID(), node_name, node_id)
        name=pydot.Node(string,shape='box3d', style="filled", fillcolor=color)
        for i in xrange (1,len(node._fields)):
            if (not isinstance(getattr(node,node._fields[i]) , list) ):
                newname=self.visit(getattr(node,node._fields[i]))
                self.graph.add_edge(pydot.Edge(name, newname))
            else:
                for foo in getattr(node,node._fields[i]):
                    if isinstance(foo,AST):
                        newname = self.visit(foo)
                        self.graph.add_edge(pydot.Edge(name, newname))
        return name



    def visit_non_leaf(self,node):
        string= "N%d %s" % (self.ID(), node.__class__.__name__)
        name=pydot.Node(string,shape='box3d', style="filled", fillcolor="#ffffff")
        for field in getattr(node,"_fields"):
            value = getattr(node,field,None)
            if isinstance(value,list):
                for item in value:
                    if isinstance(item,AST):
                        newname = self.visit(item)
                        self.graph.add_edge(pydot.Edge(name, newname))


            elif isinstance(value,AST):
                newname = self.visit(value)
                self.graph.add_edge(pydot.Edge(name, newname))
        return name




    def visit_leafBlue(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#0000ff")

    def visit_leafDec(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#9ACD32")

    def visit_leafRed(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#fd0000")

    def visit_leaf(self, node):
        string = "L%d %s ( %s )" % (self.ID(), node.__class__.__name__, node.value)
        return pydot.Node(string, shape='box3d',style="filled", fillcolor="#ffffff")

'''
class DotVisitor(NodeVisitor):


        def __init__(self):
                self.dot =pgv.Dot('AST',graph_type='digraph')
                self.dot.set_node_defaults(shape='box')
                self.st = []
                self.id =0

        def __repr__(self):
                return self.dot.to_string()

        def name(self):
                self.id+=1
                return 'n%02d' % self.id

        def generic_visit(self,node):
                #siempre va a pasar poraca cada vez queeste en un nodo
                id = self.name()
                label = node.__class__.__name__
                NodeVisitor.generic_visit(self,node)
                for field in getattr(node,'_fields'):
                        value=getattr(node,field,None)
                        if isinstance (value,list):
                                for item in value:
                                        self.dot.add_edge(pgv.Edge(id,self.st.pop()))
                        elif isinstance(value,AST):
                                self.dot.add_edge(pgv.Edge(id), self.st.pop())
                        elif value:
                                label += '\\n' + '({}={})'.format(field,value)

                self.dot.add_node(pgv.Node(id,label=label))
                self.st.append(id)'''
