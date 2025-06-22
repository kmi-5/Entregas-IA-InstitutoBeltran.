**Conclusión del Código**

Este código está diseñado para realizar un preprocesamiento y análisis básico de texto utilizando técnicas de procesamiento de lenguaje natural (NLP) y análisis estadístico. Siendo útil para tareas como análisis de texto, minería de datos, clasificación, o construcción de modelos de lenguaje, con el objetivo de extraer información relevante del corpus del texto original. 

**¿Qué se logra con el código?**

* Se obtiene un texto limpio y normalizado (tokenizado y lematizado), eliminando ruido como signos de puntuación y palabras irrelevantes.
* Se visualizan las palabras más frecuentes del texto, ayudando a entender cuáles son los términos clave.
* Se construye una matriz TF-IDF que pondera la importancia de cada término dentro del corpus, facilitando análisis posteriores.
* Se identifican secuencias frecuentes de palabras (n-gramas) que permiten detectar frases o combinaciones recurrentes en el texto.

**Cómo funciona cada bloque:**

1. **Importación y configuración de librerías**
   Se importan herramientas de NLTK para procesamiento de texto (tokenización, lematización, stopwords, POS tagging) y de scikit-learn para vectorización (TF-IDF, conteo n-gramas).

2. **Función `get_wordnet_pos(word)`**
   Convierte la etiqueta gramatical (POS tag) de una palabra al formato requerido para una lematización más precisa según el tipo de palabra (sustantivo, verbo, adjetivo, adverbio).

3. **Función `quitarStopwords_esp(texto)`**
   Elimina del texto las stopwords en español, signos de puntuación, palabras específicas definidas y cualquier símbolo o número, dejando solo palabras relevantes y limpias.

4. **Función `lematizar(texto)`**
   Aplica la lematización a cada palabra del texto, es decir, reduce cada término a su forma base o raíz para evitar variantes morfológicas.

5. **Carga y tokenización del corpus**
   Se lee el archivo de texto, se tokeniza en palabras individuales y luego se limpia y lematiza usando las funciones anteriores.

6. **Frecuencia de palabras**
   Se calcula y se visualiza la frecuencia de las palabras más comunes en el texto limpio, identificando aquellas que son claves en el corpus.

7. **Vectorización TF-IDF**
   Se transforma el texto limpio a una matriz numérica que grafica la importancia de cada palabra en el texto, a raiz de su frecuencia con su relevancia en general.

8. **Extracción de n-gramas**
   Se obtienen y muestran las secuencias de 2 y 3 palabras (n-gramas) más recurrente que permiten detectar combinaciones de palabras y frases mas pesadas en el texto.
   En este codigo se obtuvieron n-gramas como:
   "abilite trabajo", "abilite trabajo digno", "xalidad vua", "xalidad vua local"