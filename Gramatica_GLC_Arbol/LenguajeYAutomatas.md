# Gramática libre de contexto G 

R -> XRX | S
S -> aT b | bT a
T -> XT X | X | ε
X -> a | b

- El simbolo inicial de la gramatica es la "R", siendo sus variables "R", "S", "T", "X" y sus terminales "a" y "b".

**3 Cadenas que pueden pertenecer a esta gramatica. A partir desde su inicial para derivar.**

R   ->  xRx  
    ->  aSb
    ->  a(xRx)b *aplicando recursion*
    ->  a(aSb)b
    ->  aa(sTb)bb
    ->  aaa(ε)bbb
    ->  aaabbb

R   ->  xRx  
    ->  aSb
    ->  a(bTa)b 
    ->  ab(X)ab
    ->  ab(ε)ab
    ->  abab

R   ->  S 
    ->  bTa
    ->  b(xTx)a
    ->  bb(T)aa
    ->  bb(ε)aa
    ->  bbbaaa

**La derivación mós corta seria la siguiente.**

R   ->  S 
    ->  aTb
    ->  a(ε)b
    ->  ab

- En conclusión, el lenguaje que se genera es un lenguaje libre de contexto de cualquier longitud (par o impar).
- Logrando formar cadenas de palíndromos, permitiendo leerse de igual manera de izquierda a derecha y viceversa, con el alfabeto a y b. Usando reglas de produccion y recursión.


**Aunque es posible que existan algunas cadenas no posibles a generar con estas reglas o cadenas no palindromicas dentro de a;b.**

- Cadenas no posibles.

T   ->  T           *NO se puede llegar a T aplicando una o mas reglas.*
T   ->  aba         *Es imposible llegar a dicha cadena con una sola regla.*
XXX   ->  aba       *XXX al nos ser un inicial, no es posible derivar.*
X   ->  * aba       *Por mas que se puedan aplicar más pasos, no se puede generar dicha cadena.*
S   ->  * ε         *Desde S no es posible llegar a derivar quedando unicamente ε.*

- Cadenas no palindromicas o no dentro del alfabeto a;b.

T   ->  xTx
    ->  a(ε)a
    ->  aba
        
T   ->  xTx
    ->  a(ε)a
    ->  XX

T   ->  * XXX 
T   ->  xTx
    ->  xxx

**También es posible realizar un árbol de derivación a partir de cadenas, en este caso "aababa".**

*Su cadena seria esta.*                             

R   ->  xRx  
    ->  aRa
    ->  a(xRx)a 
    ->  aa(S)ba
    ->  aa(bTa)ba
    ->  aab(ε)aba
    ->  aababa

*Imagen del árbol.*
https://github.com/kmi-5/Entregas-Inst.Beltr-n-/blob/main/arbol%20derivacion.jpeg?raw=true


