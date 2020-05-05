'''
                             Markovid-19
            Generador automático de contenidos sobre las 
          últimas noticias y reflexiones en torno al Covid-19 

      Para correr el código presiona el ícono run o ctrl+enter(Windows, Linux) y cmd+enter(Mac).

      Espera a que se instalen las librerias requeridas, no te preocupes todo esto ocurre en un servidor web, nada se instalará en tu computadora.

      Una vez que se instalaron las librerias requeridas, podrás
      leer en la ventana del lado derecho lo que ha generado el algoritmo, y del lado izquierdo estará el archivo "markovid-19.mp3" el cual podrás reproducir al darle click.  
'''

# Aqui puedes variar la pronunciación del español otras opciones son es-us o es-es
lang = "es"

import os
import random
from gtts import gTTS
import os

texto = open('markovid_data.txt')
palabras = []

for lineas in texto:
    lineas = lineas.replace('\r', ' ').replace('\n', ' ')
    nuevas_palabras = lineas.split(' ')
    nuevas_palabras = [palabra for palabra in nuevas_palabras if palabra not in ['', ' ']]
    palabras = palabras + nuevas_palabras

cadena = {}
n_palabras = len(palabras)

for i, key in enumerate(palabras):
    if n_palabras > (i + 1):
        palabra = palabras[i + 1]
        if key not in cadena:
            cadena[key] = [palabra]
        else:
            cadena[key].append(palabra)

w1 = random.choice(palabras)
tweet = w1
while len(tweet) < 350:
    w2 = random.choice(cadena[w1])
    tweet += ' ' + w2
    w1 = w2

print('Hay un Corpus de: ', str(n_palabras), ' palabras.', 'y un total de: ', str(len(cadena)), ' palabras diferentes.')

print('\n', 'Markovid-19 de primer orden')
print('\n', tweet)

salida = gTTS(text=tweet, lang=lang)
salida.save('./markovid-19_primer_orden.wav')

#### Markovid-19 de segundo orden ####

cadena = {}  
n_words = len(palabras)  
for i, key1 in enumerate(palabras):  
    if n_words > i + 3:
        key2 = palabras[i + 1]
        key3 = palabras[i + 2]
        palabra = palabras[i + 3]
        if (key1, key2, key3) not in cadena:
            cadena[(key1, key2, key3)] = [palabra]
        else:
            cadena[(key1, key2, key3)].append(palabra)            
r = random.randint(0, len(palabras) - 1) 
key = (palabras[r], palabras[r + 1], palabras[r + 2])
tweet = key[0] + ' ' + key[1] + ' ' +  key[2]
while len(tweet) < 300:  
    w = random.choice(cadena[key])
    tweet += (" " + w)
    key = (key[1], key[2], w)

print('\n', 'Markovid-19 de tercer orden')
print('\n', tweet)

salida = gTTS(text=tweet, lang=lang)
salida.save('./markovid-19_tercer_orden.wav')