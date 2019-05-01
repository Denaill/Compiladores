[33mcommit 18ef970729eafc81a5774c957bca61b7d6c92abb[m
Author: Daniel Patiño Rojas <denail@Daniel>
Date:   Fri Apr 26 08:49:58 2019 -0500

    first

[1mdiff --git a/evaluacion.c b/evaluacion.c[m
[1mnew file mode 100644[m
[1mindex 0000000..b84fa7a[m
[1m--- /dev/null[m
[1m+++ b/evaluacion.c[m
[36m@@ -0,0 +1,59 @@[m
[32m+[m[32m#include stdio.h[m[41m[m
[32m+[m[32m#define aktura 67.8[m[41m[m
[32m+[m[41m[m
[32m+[m[32mint evaluar (int a, int b, float c){[m[41m[m
[32m+[m[32m  int p,q,*q, r=100, **u[m[41m[m
[32m+[m[32m  float r;[m[41m  [m
[32m+[m[32m  char *z;[m[41m [m
[32m+[m[32m  boolean val=true;[m[41m[m
[32m+[m[32m//este es un comentario[m[41m[m
[32m+[m[41m [m
[32m+[m[32mq=&p;[m[41m[m
[32m+[m[32m  if (a>0)[m[41m[m
[32m+[m[32m        p=a+1;[m[41m[m
[32m+[m[32m    else[m[41m[m
[32m+[m[32m          q=b;    ;[m[41m[m
[32m+[m[32m           if (b>0){[m[41m[m
[32m+[m[32m          p=1;[m[41m [m
[32m+[m[32m                while(p<=100){[m[41m[m
[32m+[m[32m                 q=q+1;[m[41m[m
[32m+[m[32m                 r--;[m[41m[m
[32m+[m[32m                 }[m[41m[m
[32m+[m[32m          }[m[41m[m
[32m+[m[32m          else{[m[41m[m
[32m+[m[32m                for(p=0;p<100; p++){[m[41m[m
[32m+[m[32m                  c=c+1;[m[41m[m
[32m+[m[32m                 }[m[41m [m
[32m+[m[32m   /* soy un comentario de varias lineas[m[41m[m
[32m+[m[32m    y no me creo mucho*/[m[41m[m
[32m+[m[32m              }[m[41m[m
[32m+[m[32m  a=b;[m[41m[m
[32m+[m[41m    [m
[32m+[m[32m  switch(a)[m[41m[m
[32m+[m[32m  {[m[41m[m
[32m+[m[32m     case 1: a=b;[m[41m[m
[32m+[m[32m             break;[m[41m[m
[32m+[m[32m     case 2: a=c;[m[41m[m
[32m+[m[32m             break;[m[41m[m
[32m+[m[32m     case 3: c=a+b;[m[41m[m
[32m+[m[32m             break;[m[41m[m
[32m+[m[32m     default: a=0;[m[41m[m
[32m+[m[32m              break;[m[41m      [m
[32m+[m[41m           [m
[32m+[m[32m           }[m[41m[m
[32m+[m[41m      [m
[32m+[m[32mreturn (a+1);[m[41m              [m
[32m+[m[32m}[m[41m[m
[32m+[m[41m[m
[32m+[m[32mint fibonaci(int i)[m[41m[m
[32m+[m[32m{[m[41m[m
[32m+[m[32m   if(i == 0)[m[41m[m
[32m+[m[32m   {[m[41m[m
[32m+[m[32m      return 0;[m[41m[m
[32m+[m[32m   }[m[41m[m
[32m+[m[32m   if(i == 1)[m[41m[m
[32m+[m[32m   {[m[41m[m
[32m+[m[32m      return 1;[m[41m[m
[32m+[m[32m   }[m[41m[m
[32m+[m[32m   return fibonaci(i-1) + fibonaci(i-2);[m[41m[m
[32m+[m[32m}[m[41m[m
[1mdiff --git a/hello.pas b/hello.pas[m
[1mnew file mode 100644[m
[1mindex 0000000..ba4edc5[m
[1m--- /dev/null[m
[1m+++ b/hello.pas[m
[36m@@ -0,0 +1,5 @@[m
[32m+[m[32mprogram Hello;[m
[32m+[m[32mbegin[m
[32m+[m[32m  write ('Hello, world.');[m
[32m+[m[32m  read;[m
[32m+[m[32mend.[m
\ No newline at end of file[m
[1mdiff --git a/minic_lexer.py b/minic_lexer.py[m
[1mnew file mode 100644[m
[1mindex 0000000..b48006f[m
[1m--- /dev/null[m
[1m+++ b/minic_lexer.py[m
[36m@@ -0,0 +1,97 @@[m
[32m+[m[32mimport ply.lex as lex[m[41m[m
[32m+[m[32mimport sys[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# list of tokens[m[41m[m
[32m+[m[32mtokens = ([m[41m[m
[32m+[m[32m    'BEGIN',[m[41m[m
[32m+[m[32m    'READ',[m[41m[m
[32m+[m[32m    'WRITE',[m[41m[m
[32m+[m[32m    'PROGRAM',[m[41m[m
[32m+[m[32m    'END',[m[41m[m
[32m+[m[32m    'ID',[m[41m[m
[32m+[m[32m    'NUMBER',[m[41m[m
[32m+[m[41m[m
[32m+[m[32m    #TOKENS[m[41m[m
[32m+[m[32m    'SEMICOLON',[m[41m[m
[32m+[m[32m    'COMMA',[m[41m[m
[32m+[m[32m    'LPAREN',[m[41m[m
[32m+[m[32m    'RPAREN',[m[41m[m
[32m+[m[32m    'PUNTO',[m[41m[m
[32m+[m[32m    'SIMPLE',[m[41m[m
[32m+[m[32m)[m[41m[m
[32m+[m[41m[m
[32m+[m[32m# Regular expressions rules for a simple tokens[m[41m [m
[32m+[m[32mt_SEMICOLON = ';'[m[41m[m
[32m+[m[32mt_COMMA  = r','[m[41m[m
[32m+[m[32mt_LPAREN = r'\('[m[41m[m
[32m+[m[32mt_RPAREN  = r'\)'[m[41m[m
[32m+[m[32mt_PUNTO = r'\.'[m[41m[m
[32m+[m[32mt_SIMPLE = r'\''[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_WRITE(t):[m[41m[m
[32m+[m[32m    r'write'[m[41m[m
[32m+[m[32m    return t[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_BEGIN(t):[m[41m[m
[32m+[m[32m    r'begin'[m[41m[m
[32m+[m[32m    return t[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_END(t):[m[41m[m
[32m+[m[32m    r'end'[m[41m[m
[32m+[m[32m    return t[m[41m [m
[32m+[m[41m[m
[32m+[m[32mdef t_READ(t):[m[41m[m
[32m+[m[32m    r'read'[m[41m[m
[32m+[m[32m    return t[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_ID(t):[m[41m[m
[32m+[m[32m    r'\w+(_\d\w)*'[m[41m[m
[32m+[m[32m    return t[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_NUMBER(t):[m[41m[m
[32m+[m[32m    r'\d+(\.\d+)?'[m[41m[m
[32m+[m[32m    t.value = float(t.value)[m[41m[m
[32m+[m[32m    return t[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_newline(t):[m[41m[m
[32m+[m[32m    r'\n+'[m[41m[m
[32m+[m[32m    t.lexer.lineno += len(t.value)[m[41m[m
[32m+[m[41m[m
[32m+[m[32mt_ignore = ' \t'[m[41m[m
[32m+[m[41m[m
[32m+[m[32m"""[m[41m [m
[32m+[m[32mdef t_comments(t):[m[41m[m
[32m+[m[32m    r'(\*(.|\n)*?\*)'[m[41m[m
[32m+[m[32m    t.lexer.lineno += t.value.count('\n')[m[41m[m
[32m+[m[41m[m
[32m+[m[32mdef t_comments_C99(t):[m[41m[m
[32m+[m[32m    r'{(.)*?\n\}'[m[41m[m
[32m+[m[32m    t.lexer.lineno += 1[m[41m[m
[32m+[m[32m"""[m[41m[m
[32m+[m[32mdef t_error(t):[m[41m[m
[32m+[m[32m    print ("Lexical error: " + str(t.value[0]))[m[41m[m
[32m+[m[32m    t.lexer.skip(1)[m[41m[m
[32m+[m[41m    [m
[32m+[m[32mdef test(data, lexer):[m[41m[m
[32m+[m	[32mlexer.input(data)[m[41m[m
[32m+[m	[32mwhile True:[m[41m[m
[32m+[m		[32mtok = lexer.token()[m[41m[m
[32m+[m		[32mif not tok:[m[41m[m
[32m+[m			[32mbreak[m[41m[m
[32m+[m		[32mprint (tok)[m[41m[m
[32m+[m[41m[m
[32m+[m[32mlexer = lex.lex()[m[41m[m
[32m+[m[41m[m
[32m+[m[41m [m
[32m+[m[32mif __name__ == '__main__':[m[41m[m
[32m+[m	[32mif (len(sys.argv) > 1):[m[41m[m
[32m+[m		[32mfin = sys.argv[1][m[41m[m
[32m+[m	[32melse:[m[41m[m
[32m+[m		[32mfin = 'hello.pas'[m[41m[m
[32m+[m	[32mf = open(fin, 'r')[m[41m[m
[32m+[m	[32mdata = f.read()[m[41m[m
[32m+[m	[32mprint (data)[m[41m[m
[32m+[m	[32mlexer.input(data)[m[41m[m
[32m+[m	[32mtest(data, lexer)[m[41m[m
[32m+[m	[32minput()[m[41m[m
[32m+[m[41m[m
