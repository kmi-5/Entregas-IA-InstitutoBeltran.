import nltk
from nltk.tokenize import word_tokenize

# Diccionario con los documentos 
documentos = {
    "doc1": "La inteligencia artificial está revolucionando la tecnología",
    "doc2": "El aprendizaje automático es clave en la inteligencia artificial",
    "doc3": "Procesamiento del lenguaje natural y redes neuronales",
    "doc4": "Las redes neuronales son fundamentales en deep learning",
    "doc5": "El futuro de la IA está en el aprendizaje profundo"
}

# Diccionario que guarda las palabras y en qué documentos aparecen
indice = {}

# Tokenización y limpieza de cada documento
for nombre, texto in documentos.items():
    texto = texto.lower()
    tokens = word_tokenize(texto)
    for palabra in tokens:
        if palabra.isalpha(): 
            if palabra not in indice:
                indice[palabra] = {nombre}
            else:
                indice[palabra].add(nombre)

""" 
Explicación de los operadores booleanos:
"and" es "intersección", devuelve si contiene ambas palabras
"or" es "unión", devuelve si contiene una u otra
"not" es "diferencia", devuelve si contiene la primera pero no la segunda
"""

# Bucle de ingreso de consultas 
print("Buscador de palabras (usa AND, OR, NOT). Escribí 'salir' para terminar.")
while True:
    consulta = input("\nIngrese una consulta booleana: ").lower()
    
    if consulta == "salir":
        break

    if " and " in consulta:
        t1, t2 = consulta.split("and")
        t1, t2 = t1.strip(), t2.strip()
        docs = indice.get(t1, set()) & indice.get(t2, set())

    elif " or " in consulta:
        t1, t2 = consulta.split("or")
        t1, t2 = t1.strip(), t2.strip()
        docs = indice.get(t1, set()) | indice.get(t2, set())

    elif " not " in consulta:
        t1, t2 = consulta.split("not")
        t1, t2 = t1.strip(), t2.strip()
        docs = indice.get(t1, set()) - indice.get(t2, set())

    else:
        print("Consulta no reconocida. Usá 'AND', 'OR' o 'NOT'.")
        continue

    # Mostrar resultados
    if docs:
        print("Encontrado en los documentos:", docs)
        for doc in docs:
            print(f"- {doc}: {documentos[doc]}")
    else:
        print("No se encontraron documentos.")

        
