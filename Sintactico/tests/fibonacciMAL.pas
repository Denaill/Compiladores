program fibonacci;
var a,b,c,max:integer;
begin
 write('Serie de Fibonacci');
 write('Teclea el numero tope de la serie');
 write('wdwd');
 read(max);
 a:=1;
 b:=1;
 write(a);
 write(b);
 while (a+b)<max do
  c:=(a+b);
  write(c);
  a:=b;
  b:=c;
  
end.