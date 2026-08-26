program conversion_du_temps;
var
  temps, jour, heure, minute, seconde, reste: longint;

BEGIN
  write('Entrer le temps (en secondes) : ');
  readln(temps);

  // Calcul des jours, heures, minutes et secondes
  jour := temps div 86400;
  reste := temps mod 86400;

  heure := reste div 3600;
  reste := reste mod 3600;

  minute := reste div 60;
  seconde := reste mod 60;

  writeln('Le temps saisi est le suivant : ');

  // Affichage avec accord au pluriel
  if jour > 0 then
  begin
    if jour > 1 then writeln(jour, ' jours')
    else writeln(jour, ' jour');
  end;

  if heure > 1 then writeln(heure, ' heures')
  else writeln(heure, ' heure');

  if minute > 1 then writeln(minute, ' minutes')
  else writeln(minute, ' minute');

  if seconde > 1 then writeln(seconde, ' secondes')
  else writeln(seconde, ' seconde');
END.