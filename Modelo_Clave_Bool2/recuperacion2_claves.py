import nltk
from nltk.tokenize import word_tokenize

# Diccionario con los documentos
documentos = {
    "doc1": "Los egipcios construyeron las pirámides y desarrollaron una escritura jeroglífica.",
    "doc2": "La civilización romana fue una de las más influyentes en la historia occidental.",
    "doc3": "Los mayas eran expertos astrónomos y tenían un avanzado sistema de escritura.",
    "doc4": "La antigua Grecia sentó las bases de la democracia y la filosofía moderna.",
    "doc5": "Los sumerios inventaron la escritura cuneiforme y fundaron las primeras ciudades."
}

# Función para tokenizar y limpiar los documentos
def tokenizar_y_limpiarlos(texto):
    texto = texto.lower()
    tokens = word_tokenize(texto)
    return [palabra for palabra in tokens if palabra.isalpha()]

# Indice invertido
indice = {}
for nombre_doc, contenido in documentos.items():
    palabras = tokenizar_y_limpiarlos(contenido)
    for palabra in palabras:
        if palabra not in indice:
            indice[palabra] = {nombre_doc}
        else:
            indice[palabra].add(nombre_doc)

# Bucle de consultas
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
