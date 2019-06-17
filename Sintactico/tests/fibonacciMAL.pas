(* fib.pas -  Compute fibonacci numbers *)

program fibonacci

const LAST = 30;                                        (* A constant declaration *)
var n : integer;                                  { Variable declaration }
(* A function declaration *)

function fib(n  int) : int ;
begin
        if n <= 1 then                                  (* Conditionals *)
                fib := 1;
        fib := fib(n-1) + fib(n-2)
end;
begin
n = 0;
        while n < LAST do                       { Looping (while) }
        begin
                write(fibonacci(n));    { Printing }
                n := n + 1                              { Assignment }
        end
end.
