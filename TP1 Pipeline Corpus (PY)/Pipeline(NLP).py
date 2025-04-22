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
def quitarStopwords_eng(texto):
    ingles = stopwords.words("english")
    palabras_extra = ["lematizar", "quitarStopwords_eng", "words_tokenize"]
    texto_limpio = [
        w.lower() for w in texto if w.lower() not in ingles
        and w.lower() not in palabras_extra
        and w not in string.punctuation
        and w not in ["'s", '|', '--', "''", "``"] 
        and w.isalpha() # no símbolos o números del corpus.
    ]
    return texto_limpio

# Lematizacion
def lematizar(texto):
    texto_lema = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in texto]
    return texto_lema

# Inicio Lematizador
lemmatizer = WordNetLemmatizer()
corpus = PlaintextCorpusReader(".", 'CorpusLenguajes.txt') 
texto_tokenizado = word_tokenize(corpus.raw()) 
frecuencia=FreqDist(quitarStopwords_eng(texto_tokenizado))
# Grafico de frecuencia 
frecuencia.plot(6, show = True) 
  
corpus = [
    lematizar(quitarStopwords_eng(word_tokenize("Python is an interpreted and high-level language, while CPlus is a compiled and low-level language .-"))),
    lematizar(quitarStopwords_eng(word_tokenize("JavaScript runs in web browsers, while Python is used in various applications, including data science and artificial intelligence."))),
    lematizar(quitarStopwords_eng(word_tokenize("JavaScript is dynamically and weakly typed, while Rust is statically typed and ensures greater data security .-"))),
    lematizar(quitarStopwords_eng(word_tokenize("Python and JavaScript are interpreted languages, while Java, CPlus, and Rust require compilation before execution."))),
    lematizar(quitarStopwords_eng(word_tokenize("JavaScript is widely used in web development, while Go is ideal for servers and cloud applications."))),
    lematizar(quitarStopwords_eng(word_tokenize("Python is slower than CPlus and Rust due to its interpreted nature."))),
    lematizar(quitarStopwords_eng(word_tokenize("JavaScript has a strong ecosystem with Node.js for backend development, while Python is widely used in data science .-"))),
    lematizar(quitarStopwords_eng(word_tokenize("JavaScript does not require compilation, while CPlus and Rust require code compilation before execution .-"))),
    lematizar(quitarStopwords_eng(word_tokenize("Python and JavaScript have large communities and an extensive number of available libraries."))),
    lematizar(quitarStopwords_eng(word_tokenize("Python is ideal for beginners, while Rust and CPlus are more suitable for experienced programmers.")))
]

print("\nCorpus tokenizado:\n")
print(corpus) # corpus tokenizado y lematizado
print("\n", "-" * 80, "\n") 

# TF-IDF
vectorizer = TfidfVectorizer()
# Aplica TF-IDF al corpus
corpus = [" ".join(sentence) for sentence in corpus]
X = vectorizer.fit_transform(corpus)
print("\nMatriz TF-IDF:\n")
print(X.toarray())
print("\nVocabulario:")
vocabulario = vectorizer.get_feature_names_out()
print(vocabulario)

# Matriz a tabla (con pandas) para mejor visualización 
"""tabla_tfidf = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(tabla_tfidf)
print("\n", "-" * 80, "\n")"""

# Corpus segmentado oraciones enumeradas
print("Oraciones:")
for corpus_oracion, sentence in enumerate(corpus):
    print(corpus_oracion + 1,":", sentence)
    frequencia = FreqDist(word_tokenize(sentence))
    for palabra, frecuencia in frequencia.most_common(1):  # La palabra más repetida
        print("Palabra más repetida:", f"{palabra}, aparece {frecuencia} veces.""\n")
print("\n", "-" * 80, "\n")
