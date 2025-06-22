% vocabulario base

% determinantes
det(masculino, singular, el).
det(masculino, singular, un).
det(masculino, plural, los).
det(masculino, plural, unos).
det(femenino, singular, la).
det(femenino, singular, una).
det(femenino, plural, las).
det(femenino, plural, unas).

% sustantivos
sust(masculino, singular, empleado).
sust(masculino, plural, empleados).
sust(femenino, singular, empleada).
sust(femenino, plural, empleadas).
sust(masculino, singular, sueldo).
sust(masculino, plural, sueldos).

% verbos
verbo(trabaja, intransitivo, masculino, singular).
verbo(trabaja, intransitivo, femenino, singular).
verbo(trabajan, intransitivo, masculino, plural).
verbo(trabajan, intransitivo, femenino, plural).
verbo(cobra, transitivo, masculino, singular).
verbo(cobra, transitivo, femenino, singular).
verbo(cobran, transitivo, masculino, plural).
verbo(cobran, transitivo, femenino, plural).

% gramatica

% oración principal
o(o(SN, SV)) --> sn(Gen, Num, SN), sv(Gen, Num, SV).

% sintagma nominal
sn(Gen, Num, sn(Det, Sust)) --> det(Gen, Num, Det), sust(Gen, Num, Sust).

% sintagma verbal intransitivo
sv(Gen, Num, sv(V)) --> 
    v(intransitivo, Gen, Num, V),
    % Verificación manual de fin de lista para intransitivos
    { current_input(Input), 
      Input == [] }.

% sintagma verbal transitivo
sv(Gen, Num, sv(V, SN)) --> 
    v(transitivo, Gen, Num, V),
    sn(_, NumObj, SN).

% reglas terminales
det(Gen, Num, det(Palabra)) --> [Palabra], { det(Gen, Num, Palabra) }.
sust(Gen, Num, sust(Palabra)) --> [Palabra], { sust(Gen, Num, Palabra) }.
v(Tipo, Gen, Num, v(Palabra)) --> [Palabra], { verbo(Palabra, Tipo, Gen, Num) }.