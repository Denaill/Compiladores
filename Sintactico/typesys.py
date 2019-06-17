

ARITHM_BIN_OPS = ["+", "-", "*", "/"]

REL_BIN_OPS = ["<", "<=", ">", ">=", "==", "!="]

BOOL_BIN_OPS = ["&&", "||", "==", "!="]
BOOL_UNARY_OPS = ["!"]

class DType(object):
	'''
	Clase base para nuestro sistema de tipos
	'''
	@classmethod
	def binop_type(cls, op, right_type):
		'''
		Devuelve el tipo al aplicar el operador binario con el
		actual tipo y el tipo del operando derecho, o devuelve
		None si la operación no es válida
		'''
		return None


	@classmethod
	def get_by_name(cls, type_name):
		for type_cls in cls.__subclasses__():
			if type_cls.name == type_name:
				return type_cls

		return None




class IntType(DType):
	name = "integer"

	@classmethod
	def binop_type(cls, op, right_type):
		if issubclass(right_type, IntType):
			if op in ARITHM_BIN_OPS:
				return IntType
			elif op in REL_BIN_OPS:
				return BoolType

		return None


class CharType(DType):
	name = "char"

	@classmethod
	def binop_type(cls, op, right_type):
		if issubclass(right_type, CharType):
			if op in REL_BIN_OPS:
				return BoolType

		return None




