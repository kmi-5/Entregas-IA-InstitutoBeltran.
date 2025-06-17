**Conclusión general del código**

Utilizando Python, el siguiente código implementa un **pipeline de procesamiento de lenguaje natural (NLP)** trabajando con herramientas de NLTK y scikit-learn, con el objetivo de transformar textos crudos en datos cuantificables y analizables. Con procesos para limpiar, lematizar, vectorizar y analizar textos relacionados a distintos lenguajes de programación. 

**Explicación de cada parte**

1. **Importación de librerías**
   Se importan módulos de NLTK para el procesamiento lingüístico (tokenización, lematización, stopwords, etc.), así como `TfidfVectorizer` de scikit-learn para convertir el texto en vectores numéricos, y `pandas` para visualización opcional de tablas.

2. **Función `get_wordnet_pos`**
   Convierte etiquetas gramaticales (POS tags) a las compatibles con el lematizador WordNet, mejorando la precisión de la lematización.

3. **Función `quitarStopwords_eng`**
   Limpia el texto eliminando:

   * Palabras vacías ("stopwords") en inglés.
   * Palabras irrelevantes manualmente agregadas.
   * Símbolos y signos de puntuación.
   * Palabras no alfabéticas.
     Resultado: una lista de palabras relevantes para el análisis.

4. **Función `lematizar`**
   Aplica lematización usando `WordNetLemmatizer`, devolviendo las formas base (lemmas) de las palabras según su categoría gramatical.

5. **Procesamiento de corpus real (`CorpusLenguajes.txt`)**

   * Se lee un archivo corpus de texto.
   * Se tokeniza y limpia el texto.
   * Se calcula la frecuencia de las palabras más comunes (sin stopwords) y se grafica.
	En este corpus las palabras frecuentes que se imprimen son: PYTHON con 7, JAVASCRIPT con 7, CPLUS con 5, RUST con 5, INTERPRETED con 3, USED con 3.
	- Siendo INTERPRETED y USED las menos utilizadas de dicha jerarquia.


6. **Procesamiento de oraciones predefinidas**
   Se aplican los mismos pasos (tokenización, limpieza y lematización) a 10 oraciones comparando lenguajes como Python, JavaScript, C++, Rust y Go.

7. **Vectorización con TF-IDF**

   * Se convierte el corpus preprocesado en una **matriz numérica** donde cada fila representa una oración y cada columna una palabra relevante.
   * Se imprime la matriz y el vocabulario extraído.
	En este corpus: La palabra con mayor peso en el corpus, LANGUAGE con 0.757... Y la de menor peso, JAVASCRIPT con 0.146...

8. **Análisis de oraciones**

   * Se imprime cada oración limpia con su número correspondiente para una lectura mas rápida del corpus.
   * Para cada oración, se identifica la palabra más frecuente (con su cantidad de apariciones).
	En el corpus utilizado: En la primera oración seria PYTHON apareciendo 2 veces, en la tercera TYPED apareciendo 2 veces y en la octava REQUIRE apareciendo 2 veces.