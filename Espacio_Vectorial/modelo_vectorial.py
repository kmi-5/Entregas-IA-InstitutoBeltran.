"""
Este codigo utiliza el modelo de espacio vectorial con TF-IDF para representar documentos 
como vectores numéricos, es un modelo fundamental en recuperación de información y PLN.
El mismo calcula la similitud entre ellos usando la metrica de coseno, que nos indica lo similares que son. 
Finalmente, la matriz de similitud se visualiza con un mapa de calor para que podamos identificar 
rapidamente que documentos se parecen más entre si.
"""

from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.metrics.pairwise import cosine_similarity       
import matplotlib.pyplot as plt                              
import seaborn as sns                                        

# Lista de documentos
documents = [
    "El veloz zorro marrón salta sobre el perro perezoso.",
    "Un perro marrón persiguió al zorro.",
    "El perro es perezoso."
]

# vectorizador TF-IDF
vectorizer = TfidfVectorizer()

# Transformamos los documentos en una matriz numérica (TF-IDF)
tfidf_matrix = vectorizer.fit_transform(documents)

# Calculamos la similitud del coseno entre todos los documentos
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Graficamos la matriz de similitud usando seaborn
plt.figure(figsize=(8, 6))  # Tamaño de la figura
sns.heatmap(
    cosine_sim, 
    annot=True,  # muestra los valores dentro de cada celda
    cmap="pink",  # paleta de colores
    xticklabels=[f"Doc {i+1}" for i in range(len(documents))],  # etiquetas del eje X
    yticklabels=[f"Doc {i+1}" for i in range(len(documents))]   # etiquetas del eje Y
)
plt.title("Matriz de similitud del coseno entre documentos")  # titutlo del gráfico
plt.show()  # muestra la gráfica