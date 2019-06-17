# PascalCompilador
Realización de un compilador del lenguaje Pascal utilizando la librería de Python SLY.

Para ejecutar es necesario seguir el siguiente formato

```
python3 pascal.py [opcion] archivo [archivo]* <---- Para la ejecución en terminal unix

python pascal.py [opcion] archivo [archivo]* <---- Para ejecución en algún entorno de Python 3.6
```

Opciones:
La presente entrega contiene el analizador léxico, el analizador sintáctico y el analizador semántico. A continuación, detallaré lo ocurrido con cada una de estas etapas:

## Analizador léxico

Funciona, en teoría, para cualquier programa escrito en Pascal. Se ejecuta de la siguiente forma:

```
python3 pascal.py -l archivo [archivo]*
python3 pascal.py --lex archivo [archivo]*
```
Las anteriores opciones son para ver el resultado del análisis léxico.
Con la ejecución de ese comando y teniendo los correspondientes archivos de código en Pascal, el programa pascal.py mostrará todos los tokens de los códigos ingresados como parámetro a la ejecución.
<br><br>

## Analizador sintáctico

Funciona para programas escritos en Pascal con las siguientes condiciones:

- La definición y el llamado de **procedimientos** sigue estrictamente la gramática entregada al principio del semestre (ver archivo *Mini Pascal.pdf* en el presente repositorio). Por lo tanto, el analizador sintáctico soporta definiciones y llamados de procedimientos **sin argumentos**.

- A pesar de no estar definido en la gramática entregada a principio de semestre, el presente analizador sintáctico soporta la definición y llamado de **funciones con argumentos**, tal como lo define la gramática completa del lenguaje Pascal (no Mini Pascal). Las funciones también soportan valores de retorno

- También, a pesar de no estar definido en la gramática entregada en clase, este analizador sintáctico soporta programas con definición de constantes.

Para ejecutar este analizador sintáctico es necesario seguir el siguiente comando:

```
python3 pascal.py -p archivo [archivo]* (en terminales Unix)

python pascal.py -p archivo [archivo]* (en algún entorno de Python 3.6 o superior)
```
Al ejecutar el comando presentado anteriormente, el analizador creará el árbol de sintaxis abstracto (ast) del programa de prueba. Esto se hace en memoria (a través de un objeto de clase AST con todas sus ramificaciones en él) y su resultado se puede ver en una imagen contenida en la subcarpeta astimage en formato png con el mismo nombre del archivo de Pascal. Esta imagen se crea inmediatamente se ejecuta el analizador sintáctico con este comando.

**NOTA:** Para que la imagen pueda ser creada correctamente, es necesario tener instalado el módulo graphviz para Python en la máquina.

## Analizador semántico

Este analizador semántico realiza chequeos de variables y tipos de datos para programas escritos en Pascal con las siguientes consideraciones:

- Este analizador semántico **NO SOPORTA** definición y llamados de funciones y/o procedimientos.
- Exceptuando la consideración hecha anteriormente, el presente analizador semántico es capaz de chequear y reportar los errores más comunes de declaración de variables y chequeo de datos (redefinición de variables, uso de variables no definidas, tipo de dato desconocido, inconsistencias en tipos de datos a la hora de hacer asignaciones, error al asignar valores a una constante).

Para ejecutar el analizador semántico se debe escribir el siguiente comando:

```
python3 pascal.py -s archivo [archivo]* (terminales UNIX)

python pascal.py -s archivo [archivo]* (entornos de Python 3.6 o superior)
```

Al ejecutar el comando anterior, se ejecutará también el analizador sintáctico, creando la respectiva imagen del ast en la carpeta *astimage*. Además, se mostrará el reporte de chequeo, específicando qué errores se presentaron (si los hubo) y cuántos errores **semánticos** hubo en total.

**NOTA:** A diferencia del análisis sintáctico, en este análisis semántico el seguimiento de número de línea para los errores no funciona.

# Archivos de prueba

En la subcarpeta *tests* del presente repositorio se encuentran algunos archivos de prueba hechos por mí. Algunas aclaraciones:

- **fibonacci.pas:** Implementación de los números de fibonacci **con funciones**. Ya que tiene definición y manejo de funciones, este archivo solo puede ser probado en el análisis léxico (opción -l) y el análisis sintáctico (opción -p). Este archivo está bien escrito, sin ningún error sintáctico, por lo que el analizador no presenta errores.
- **fibonacciMAL.pas:** Es el mismo programa escrito en *fibonacci.pas* pero con varios errores de sintaxis. Es necesario tener en cuenta que el presente analizador sintáctico se detiene al detectar el primer error, por lo que no los reporta todos.
- **test1.pas:** Se trata de un programa inventado **sin funciones ni procedimientos**. Por ese motivo, puede ser ejecutado a través del analizador semántico (-s).
- **test2.pas:** Es el mismo programa anterior con errores. Tiene los errores semánticos más comunes. En el caso del analizador semántic, el compilador reporta todos los errores y cuenta cuántos son.
