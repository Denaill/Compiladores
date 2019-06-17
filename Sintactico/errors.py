import sys

_subscribers = []
_num_errors = 0

def error(lineno, message, filename=None):

	#Reporta un error del compilador a todos los suscriptores.

	global _num_errors
	if filename==None:
		errmsg = "{}: {}".format(lineno, message)
	else:
		errmsg = "{} : {} : {}".format(filename,lineno,message)
	print(errmsg)
	_num_errors += 1

def errors_reported():
	'''
	Devuelve el numero de errores reportados.
	'''
	return _num_errors

def clear_errors():
	'''
	Limpia el numero total de errores reportados.
	'''
	global _num_errors
	_num_errors = 0
