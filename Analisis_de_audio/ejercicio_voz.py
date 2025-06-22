#%%
import soundfile as sf
import numpy as np
import librosa.display 
from scipy.io import wavfile
from IPython.display import Audio 
import matplotlib.pyplot as plt

# Archivo de audio con su ruta correspondiente
audio, sr = sf.read(r"C:\Users\camic\Downloads\ffmpeg\ffmpeg-2025-06-17-git-ee1f79b0fa-essentials_build\bin\marita.wav")

# Información del audio
print(audio)
print("Largo array:", len(audio))
print("Frecuencia de muestreo:", sr)
print("Duracion:", len(audio) / sr)

# Grafico de la forma de onda
plt.plot(audio)
plt.title("Forma de onda")
plt.xlabel("Muestras")
plt.ylabel("Amplitud") 

# Reproducir audio ('Audio' con minuscula es incorrecto y no correrá)
Audio(audio, rate=sr)


# Modificaciones del audio en diferentes formatos
"""Para reproducir el audio a diferentes velocidades, se ajusta la frecuencia de muestreo
Audio(audio, rate=sr * 2)  # Más rápido
Audio(audio, rate=sr * 0.5)  # Más lento

Para bajar calidad del audio
#print("audio con profundidad de 8 bits: ")
Audio(audio_8bit, rate=sr)"""
