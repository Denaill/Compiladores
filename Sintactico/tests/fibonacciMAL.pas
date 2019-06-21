program fibonacci;
var a,b,c,max:integer;
const  ho = 0;
const hooo = 'wdwd'; 
begin
 write('Serie de Fibonacci');
 write('Teclea el numero tope de la serie');
 write('wdwd');
 read(max);
 a:=1;  (*un comentario aqui *)
 b:=1; 
 write(a);
 write(b);
         while (a+b)<max do
                c:=(a+b);
                 write(c);
                 a:=b;
                 b:=c;
 if (a >= b) then 
        a := a+b;
else 
        b := a+b;
        fib(a);
   (* por aqui otro *)
end.
