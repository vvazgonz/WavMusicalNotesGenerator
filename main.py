import numpy as np
import random
from scipy.io.wavfile import write
import math
from IPython.display import Audio

def calcular_frecuencia(nota_base, semitonos):
    return nota_base * (2 ** (semitonos / 12))

def generar_sonido(frecuencia, duracion=1.0, samplerate=44100):
    t = np.linspace(0, duracion, int(samplerate * duracion), endpoint=False)
    onda = 0.15 * np.sin(2 * np.pi * frecuencia * t)
    return np.int16(onda * 32767)

frecuencia = random.uniform(300, 440)
samplerate = 44100
melodia = []
ultimo  = -1
for j in range(0, 50):
    Index = np.arange(0.5, 5, 0.5)
    inc = random.randint(0, len(Index)-1)
    frecuenciaf = frecuencia *(Index[inc])
    if frecuenciaf == ultimo:
        frecuenciaf = frecuenciaf * 1.2
    if frecuenciaf > 1000:
        frecuenciaf = frecuenciaf /2
    print(f"Frecuencia: {frecuenciaf:.2f} Hz")
    onda = generar_sonido(frecuenciaf, duracion=0.35, samplerate=samplerate)
    melodia.append(onda)
    j = j+1

melodia_total = np.concatenate(melodia)  # Concatenar las ondas
output_filename = "melodia_generada.wav"
write(output_filename, samplerate, melodia_total)  # Pasar el array concatenado
print(f"Archivo guardado como {output_filename}")
Audio("melodia_generada.wav")
