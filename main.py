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
from playsound import playsound

text = open('markovid_data.txt')
words = []

for line in text:
    line = line.replace('\r', ' ').replace('\n', ' ')
    #line = line.replace('', ).replace(' ')
    new_words = line.split(' ')
    new_words = [word for word in new_words if word not in ['', ' ']]
    words = words + new_words

print('Corpus size: {0} words.'.format(len(words)))

chain = {}
n_words = len(words)

for i, key in enumerate(words):
    if n_words > (i + 1):
        word = words[i + 1]
        if key not in chain:
            chain[key] = [word]
        else:
            chain[key].append(word)

w1 = random.choice(words)
tweet = w1
while len(tweet) < 350:
    w2 = random.choice(chain[w1])
    tweet += ' ' + w2
    w1 = w2
print('\t', tweet)

output = gTTS(text=tweet, lang=lang)

output.save('./markovid-19.mp3')

#playsound("markovid-19.mp3")
