program  nbpremier;
var  a:integer;
begin
	write('entrez a : ');
	readln(a);
	if ((a<>2) and (a<>3)) then
	begin
        if ((a mod 2=0) or (a mod 3=0) or (a mod 5=0) or (a mod 9=0) or (a mod 10=0)) then
        begin
            writeln('le nombre est pas un nombre premier');
        end
            else
            begin
            	writeln('le nombre est  un nombre premier');
            end;
    end
            else
              begin
              	writeln('le nombre est un nombre premier');
            end;
end.