# mpascal/checker.py
'''

*** No inicie este proyecto hasta que no haya completado el parser. ***

Visión general
--------------
En este proyecto necesitas realizar verificaciones semánticas
en tu programa.  Este problema es multifacético y complicado.
Para hacerlo un poco menos complicado, necesitas tomarlo lento
y en partes pequeñas.  La idea básica de lo que debe hacer es
la siguiente:

1.	Nombres y símbolos:

    Todos los identificadores deben definirse antes de ser
    utilizados. Esto incluye variables, constantes y nombres
    tipográficos. Por ejemplo, este tipo de código genera
    un error:

       a = 3; // Error. 'a' no definido.
       var a int;

2.	Tipos de literales y constantes.

    Todos los símbolos literales se escriben implícitamente
    y se les debe asignar un tipo "int", "float" o "char".
    Este tipo se utiliza para establecer el tipo de constantes.
    Por ejemplo:

       const a = 42; // Escribe "int"
       const b = 4.2; // Escribe "float"
       const c = 'a'; // Escribe "char"

3.	Comprobación del tipo de operador

    Los operadores binarios solo operan en operandos de un
    tipo compatible.  De lo contrario, obtendrá un error de
    tipo. Por ejemplo:

        var a int = 2;
        var b float = 3.14;

        var c int = a + 3; // OKAY
        var d int = a + b; // Error. int + float
        var e int = b + 4.5; // Error. int = float

    Además, debe asegurarse de que solo sea compatible
    Los operadores están permitidos. Por ejemplo:

        var a char = 'a'; // OKAY
        var b char = 'a' + 'b'; // Error (op + no soportada)

4.	Asignación.

    Los lados izquierdo y derecho de una operación de
    asignación deben estar declarado como el mismo tipo.

        var a int;
        a = 4 + 5; // OKAY
        a = 4.5; // Error. int = float

    Los valores solo se pueden asignar a declaraciones de
    variables, no a las constantes.

        var a int;
        const b = 42;

        a = 37; // OKAY
        b = 37; // Error. b es const

Estrategia de implementacion:
-----------------------------
Se va a usar la clase NodeVisitor definida en ast.py
para recorrer el árbol de parse. Se van a definir
varios métodos para diferentes tipos de nodos AST.
Por ejemplo, si tiene un nodo BinOp, escribirás un
método como este:

      def visit_BinOp (self, node):
          ...

Para comenzar, haga que cada método simplemente
imprima un mensaje:

      def visit_BinOp (self, node):
          imprimir ('visit_BinOp:', nodo)
          self.visit (node.left)
          self.visit (node.right)

Esto al menos te dirá que el método se está disparando.
Prueba ejemplos de código simple y asegúrese de que todos
sus métodos en realidad están corriendo cuando recorres
el árbol de análisis.

Pruebas
-------
Construya archicos que contengan diferentes elementos que
necesita para comprobar Las instrucciones específicas se
dan en cada archivo de prueba.

Pensamientos generales y consejos.
----------------------------------
Lo principal en lo que debe estar pensando con la verificación
es el programa exactitud. ¿Esta declaración u operación que
estás mirando? en el arbol de parse tiene sentido? Si no,
algún tipo de error necesita ser generado. Use sus propias
experiencias como programador como guía (piense sobre lo que
causaría un error en tu lenguaje de programación favorito).

Un desafío será la gestión de muchos detalles complicados.
Tienes que rastrear símbolos, tipos y diferentes tipos de
capacidades. No siempre está claro cómo organizar mejor
todo eso. Entonces, espera un poco al principio.
'''

from collections import ChainMap
from errors import error
from astobjects import *
from typesys import *
import sys
from parser import *

class CheckProgramVisitor(NodeVisitor):
	def __init__(self):
		self.symbols = { }

		self.temp_symbols = { }

		self.expected_ret_type = None

		self.current_ret_type = None

		self.functions = { }

		self.keywords = {t.name for t in Type.__subclasses__()}

	def visit_VarDeclaration(self, node):
		#node.type = None
		if node.identifier in self.keywords:
			error(node.lineno, f"Nombre '{node.name}' no es un nombre legal para declaración de variable")
			return
		print(self.symbols)
		if node.identifier not in self.symbols and node.identifier:
			print("holi")
			self.visit(node.type)
			if node.type:
				node.type = node.type.type
				self.symbols[node.identifier] = node
			else:
				error(node.lineno, f"Tipo desconocido '{node.type}'")
		else:
			prev_lineno = self.symbols[node.identifier].lineno
			error(node.lineno, f"Nombre '{node.identifier
			}' ya se ha definido en linea {prev_lineno}")

	def visit_ConstDeclaration(self, node):
		# Para una declaración, deberá verificar que no esté ya definida.
		# Colocarás la declaración en la tabla de símbolos para que
		# puedas consultarla más adelante.
		node.type = None
		if node.name not in self.symbols:
			self.visit(node.value)
			if node.datatype.type:
				if node.value:
					self.visit(node.value)
					if node.value.type:
						node.type = node.datatype.type
						self.symbols[node.name] = node
				else:
					node.type = node.datatype.type
					self.symbols[node.name] = node
			else:
				error(node.lineno, f"Tipo desconocido '{node.datatype.name}'")


		else:
			prev_lineno = self.symbols[node.name].lineno
			error(node.lineno, f"Nombre '{node.name}' ya se ha definido en linea {prev_lineno}")

	def visit_IntegerLiteral(self, node):
		node.type = IntType

	def visit_PrintStatement(self, node):
		self.visit(node.value)

	def visit_IfStatement(self, node):
		self.visit(node.condition)

		cond_type = node.condition.type
		if cond_type:
			if issubclass(node.condition.type, BoolType):
				self.visit(node.true_block)
				self.visit(node.false_block)
			else:
				error(node.lineno, f"'Condicion debe ser de tipo 'bool' pero tiene tipo '{cond_type.name}'")

	def visit_WhileStatement(self, node):
		self.visit(node.condition)

		cond_type = node.condition.type
		if cond_type:
			if issubclass(node.condition.type, BoolType):
				self.visit(node.body)
			else:
				error(node.lineno, f"'Condición debe ser de tipo 'bool' pero tiene tipo '{cond_type.name}'")

	def visit_BinaryOp(self, node):

		self.visit(node.left)
		self.visit(node.right)

		node.type = None
		# Realiza varios controles aquí
		if node.left.type and node.right.type:
			op_type = node.left.type.binop_type(node.op, node.right.type)
			if not op_type:
				left_tname = node.left.type.name
				right_tname = node.right.type.name
				error(node.lineno, f"Operacion binaria '{left_tname} {node.op} {right_tname}' no soportada")

			node.type = op_type


	def visit_AssignamentStatementEntire(self, node):
		self.visit(node.identifier)
		self.visit(node.expression)

		node.type = None
		if node.identifier.type and node.expression.type:
			loc_name = node.identifier.name

			if isinstance(self.symbols[loc_name], ConstDeclaration):
				error(node.lineno, f"No se puede escribir a constante '{loc_name}'")
				return

			if node.location.type == node.value.type:
				pass

			else:
				error(node.lineno,
				f"No se puede asignar el tipo '{node.value.type.name}' a variable '{node.location.name}' de tipo '{node.location.type.name}'")


	def visit_Variable(self, node):
		if node.name not in self.symbols:
			node.type = None
			error(node.lineno, f"Nombre '{node.name}' no esta definido")
		else:
			node.type = self.symbols[node.name].type

	def visit_SimpleType(self, node):
		# Asocie un nombre de tipo como "int" con un objeto de tipo
		node.type = node.type_identifier
		if node.type is None:
			error(node.lineno, f"Tipo invalido '{node.name}'")

	def visit_FuncParameter(self, node):
		self.visit(node.datatype)
		node.type = node.datatype.type

	def visit_ReturnStatement(self, node):
		self.visit(node.value)
		# Propagar el tipo de valor de retorno como una propiedad
		# especial ret_type, solo para revisarse en la verificación
		# de la declaración de la función
		if self.expected_ret_type:
			self.current_ret_type = node.value.type
			if node.value.type and node.value.type != self.expected_ret_type:
				error(node.lineno, f"Funcion retorna '{self.expected_ret_type.name}' pero el valor de la declaración de retorno es de tipo '{node.value.type.name}'")
		else:
			error(node.lineno, "Instrucción return debe de estar dentro de una funcion")

	def visit_FuncDeclaration(self, node):
		if node.name in self.functions:
			prev_def = self.functions[node.name].lineno
			error(node.lineno, f"Funcion '{node.name}' esta definida en la linea {prev_def}")

		self.visit(node.params)

		param_types_ok = all((param.type is not None for param in node.params))
		param_names = [param.name for param in node.params]
		param_names_ok = len(param_names) == len(set(param_names))
		if not param_names_ok:
			error(node.lineno, "Nombre de parametros duplicados en definicion de funcion")

		self.visit(node.datatype)
		ret_type_ok = node.datatype.type is not None

		# Antes de visitar la función, cuerpo, debemos cambiar la tabla
		# de símbolos a una nueva.
		if self.temp_symbols:
			error(node.lineno, f"Declaración de función anidada ilegal '{node.name}'")
		else:
			self.temp_symbols = self.symbols
			self.symbols = ChainMap(
				{param.name: param for param in node.params},
				self.temp_symbols
			)
			# Establecer el valor de retorno esperado para observar
			self.expected_ret_type = node.datatype.type

			self.visit(node.body)

			if not self.current_ret_type:
				error(node.lineno, f"Funcion '{node.name}' no tiene instrucción return")
			elif self.current_ret_type == self.expected_ret_type:
				# Debemos agregar la declaración de función como
				# disponible para futuras llamadas.
				self.functions[node.name] = node

			self.symbols = self.temp_symbols
			self.temp_symbols = { }
			self.expected_ret_type = None
			self.current_ret_type = None

	def visit_FuncCall(self, node):
		if node.name not in self.functions:
			error(node.lineno, f"Function '{node.name}' no esta declarada")
		else:
			# Debemos verificar que la lista de argumentos coincida con
			# la definición de parámetros de la función
			self.visit(node.arguments)

			arg_types = tuple([arg.type.name for arg in node.arguments])
			func = self.functions[node.name]
			expected_types = tuple([param.type.name for param in func.params])
			if arg_types != expected_types:
				error(node.lineno, f"Function '{node.name}' espera {expected_types}, pero fue llamada con {arg_types}")

			# El tipo de llamada a la función es el tipo de retorno de la función.
			node.type = func.datatype.type

# ----------------------------------------------------------------------
#                       NO MODIFICAR NADA ABAJO
# ----------------------------------------------------------------------

def check_program(ast):
	checker = CheckProgramVisitor()
	checker.visit(ast)

def main():


	if len(sys.argv) < 2:
		sys.stderr.write('Uso: python -m mpascal.checker filename\n')
		raise SystemExit(1)
	parse = PasParser()
	lexer = PascalLexer()
	parser = PasParser()
	toopen = open(sys.argv[1])
	code = toopen.read()
	ast = parser.parse(lexer.tokenize(code))
	check_program(ast)
	if '--show-types' in sys.argv:
		for depth, node in flatten(ast):
			print('%s: %s%s type: %s' % (getattr(node, 'lineno', None), ' '*(4*depth), node,
			getattr(node, 'type', None)))

if __name__ == '__main__':
	main()

