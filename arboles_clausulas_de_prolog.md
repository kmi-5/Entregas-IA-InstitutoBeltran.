***Árbol de análisis sintáctico***

Los árboles de `análisis gramatical` son fundamentales en el procesamiento del lenguaje natural (PLN) porque permiten implementar gramáticas formales computacionalmente, validando oraciones o generándolas de forma estructurada. 
En este ejemplo, se utilizo `gramáticas de cláusulas definidas`, ya que proporcionan a los lenguajes de programación lógicos como Prolog una forma conveniente y efectiva de expresar gramáticas, resultando especialmente útiles en el `procesamiento de lenguajes naturales` y de lenguajes formales.

1. **Estructuración del lenguaje**
    Representan visualmente la jerarquía gramatical de una oración, mostrando cómo se relacionan las palabras entre sí (sujeto-verbo-objeto, modificadores, etc.).

2. **Extracción de significado**: 
    Facilitan tareas como:
   - Identificación de relaciones semánticas (quién hace qué a quién)
   - Reconocimiento de entidades nombradas
   - Análisis de sentimientos (qué modifica a qué)

3. **Aplicaciones prácticas**
   - Traducción automática (para reordenar correctamente los elementos entre idiomas)
   - Búsqueda semántica (entender consultas complejas)
   - Generación de lenguaje natural (producir oraciones bien formadas)
   - Sistemas de diálogo (entender la estructura de las preguntas/respuestas)

4. **Intermediario para representaciones más abstractas**: 
    Son el paso previo para crear representaciones lógicas del significado (como fórmulas de predicados).

*Sabiendo que la gramática se compone del conjunto de concordancias, palabras, reglas Y oraciones. Podemos entender las definiciones de los términos utilizados.*

o = oracion (raiz del arbol)
sn = sintagma nominal
sv = sintagma verbal
det = determinante
sp = sintagma proposicional
num = numero
    sg = singular
    pl = plural
n = nucleo (verbo)
vt = verbo transitivo
vi =  verbo intransitivo
md = modificador directo

*Algunos ejemplos de estos arboles pueden ser.*

1. Los aztecas hablan náhuatl

Oración
├── Sintagma Nominal
│   ├── Determinante: los
│   └── Nombre/Nucleo: aztecas
└── Sintagma Verbal
    ├── Verbo: hablan
    └── Complemento: náhuatl


2. Los reyes católicos conquistaron Granada

├── Sintagma Nominal
│   ├── Determinante: los
│   └── Nombre/Nucleo: reyes católicos
└── Sintagma Verbal
    ├── Verbo: conquistaron
    └── Complemento (Nombre propio): Granada


3. Los sacerdotes evangelizaban a los indígenas

Oración
├── Sintagma Nominal
│   ├── Determinante: los
│   └── Nombre/Nucleo: sacerdotes
└── Sintagma Verbal
    ├── Verbo: evangelizaban
    └── Complemento
        ├── Preposición: a
        └── Sintagma Nominal
            ├── Determinante: los
            └── Nombre/Nucleo: indígenas

4. El catalán es una lengua romance

Oración
├── Sintagma Nominal
│   ├── Determinante: el
│   └── Nombre/Nucleo: catalán
└── Sintagma Verbal
    ├── Verbo: es
    └── Sintagma Nominal
        ├── Determinante: una
        ├── Nombre/Nucleo: lengua
        └── Modificador directo: romance


5. La dominación islámica disminuyó progresivamente

Oración
├── Sintagma Nominal
│   ├── Determinante: la
│   └── Nombre/Nucleo: dominación islámica
└── Sintagma Verbal
    ├── Verbo: disminuyó
    └── Adverbio: progresivamente


6. Los mayas resistieron la colonización española

Oración
├── Sintagma Nominal
│   ├── Determinante: los
│   └── Nombre/Nucleo: mayas
└── Sintagma Verbal
    ├── Verbo: resistieron
    └── Sintagma Nominal
        ├── Determinante: la
        ├── Nombre/Nucleo: colonización
        └── Modificador directo: española


7. Las lenguas minoritarias de España han entrado en una nueva etapa

Oración
├── Sintagma Nominal
│   ├── Determinante: las
│   ├── Nombre/Nucleo: lenguas
│   ├── Modificador directo: minoritarias
│   └── Complemento
│       ├── Preposición: de
│       └── Nombre/Nucleo: España
└── Sintagma Verbal
    ├── Verbo auxiliar: han
    ├── Participio: entrado
    └── Complemento
        ├── Preposición: en
        └── Sintagma Nominal
            ├── Determinante: una
            ├── Modificador directo: nueva
            └── Nombre/Nucleo: etapa


8. Los niños monolingües de desarrollo normal pasan por varias etapas

Oración
├── Sintagma Nominal
│   ├── Determinante: los
│   ├── Nombre/Nucleo: niños
│   ├── Modificador directo: monolingües
│   └── Complemento
│       ├── Preposición: de
│       └── Sintagma Nominal
│           ├── Nombre/Nucleo: desarrollo
│           └── Modificador directo: normal
└── Sintagma Verbal
    ├── Verbo: pasan
    └── Complemento
        ├── Preposición: por
        └── Sintagma Nominal
            ├── Determinante: varias
            └── Nombre/Nucleo: etapas


9. El español es lengua oficial en diecinueve países de Latinoamérica

Oración
├── Sintagma Nominal
│   ├── Determinante: el
│   └── Nombre/Nucleo: español
└── Sintagma Verbal
    ├── Verbo: es
    └── Sintagma Nominal
        ├── Nombre/Nucleo: lengua
        └── Modificador directo: oficial
        └── Complemento
            ├── Preposición: en
            └── Sintagma Nominal
                ├── Determinante: diecinueve
                ├── Nombre/Nucleo: países
                └── Complemento
                    ├── Preposición: de
                    └── Nombre/Nucleo: Latinoamérica


10. El terreno de Paraguay representaba desafíos de envergadura para los españoles

Oración
├── Sintagma Nominal
│   ├── Determinante: el
│   ├── Nombre/Nucleo: terreno
│   └── Complemento
│       ├── Preposición: de
│       └── Nombre/Nucleo: Paraguay
└── Sintagma Verbal
    ├── Verbo: representaba
    └── Sintagma Nominal
        ├── Nombre/Nucleo: desafíos
        ├── Complemento
        │   ├── Preposición: de
        │   └── Nombre/Nucleo: envergadura
        └── Complemento
            ├── Preposición: para
            └── Sintagma Nominal
                ├── Determinante: los
                └── Nombre/Nucleo: españoles