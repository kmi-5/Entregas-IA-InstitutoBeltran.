import nltk 
from nltk.corpus import stopwords
import string
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
from nltk import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# (POS part of speech) para lematizar
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {
    "J": wordnet.ADJ,
    "N": wordnet.NOUN,
    "V": wordnet.VERB,
    "R": wordnet.ADV 
    }
    return tag_dict.get(tag, wordnet.NOUN)

# Stopwords
def quitarStopwords_esp(texto):
    español = stopwords.words("spanish")
    texto_limpio = [
        w.lower() for w in texto if w.lower() not in español
        and w.lower() 
        and w not in string.punctuation
        and w not in ["'s", '|', '--', "''", "``"] 
        and w.isalpha()  # Solo palabras, sin números ni símbolos
    ]
    return texto_limpio

# Lematizacion
def lematizar(texto):
    texto_lema = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]
    return texto_lema

# Inicio Lematizador
lemmatizer = WordNetLemmatizer()

# Corpus original
corpus = PlaintextCorpusReader("C:/VSCode/Entregas_Beltran/Modelos_N_gramas", r'CorpusEducacion\.txt')
texto_tokenizado = word_tokenize(corpus.raw('CorpusEducacion.txt'))
texto_limpio = lematizar(quitarStopwords_esp(texto_tokenizado))
# El corpus ya esta tokenizado y vectorizado
corpus = [" ".join(texto_limpio)]
# Frecuencia de palabras sobre texto limpio (sin stopwords ni símbolos)
frecuencia = FreqDist(texto_limpio)
frecuencia.plot(6, show=True)

print("\nTexto tokenizado y lematizado:\n")
print(texto_limpio)
print("\n", "-" * 80, "\n")

# TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)  # como lista de strings
print("\nMatriz TF-IDF:\n")
print(X.toarray())
print("\nVocabulario del TF-IDF:\n")
vocabulario = vectorizer.get_feature_names_out()
print(vocabulario)
print("\n", "-" * 80, "\n") 

# Imprime los n-gramas más comunes que aparecen al menos 2 veces
vectorizer = CountVectorizer(ngram_range=(2, 3))
X = vectorizer.fit_transform(corpus)
print("\nSecuencias de palabras (n-gramas más frecuentes):\n")
ngramas = vectorizer.get_feature_names_out()
print(ngramas)
