program test;
const constante = 1;
var c : char;
x,y,z : integer;
begin
  x := -1 * 4 + (3 - 5);
  y := 5 div 3 div 5 - 3 * (3*5 - 2) div 2;
  z := 3;
  c := "holiwi";
  read(x,y,z);
  write(x,y,x - y);
  read(y);
  if -x <> y * 500 then
    write(x)
  else
    write(y);
  read(z);
  if not "holi" = (y or 7 = 5) then
  begin
    write("hola");
    write("chao")
  end
  else
  begin
    read(z);
    y := x + 10
  end;
  read(x)
end.
