'''
                             Markovid-19
            Generador automático de contenidos sobre las 
          últimas noticias y reflexiones en torno al Covid-19 

Instrucciones:

- Corre el código presionando el ícono run> o presiona ctrl+enter(Windows, Linux) y cmd+enter(Mac).

- Espera a que se instalen las librerias requeridas, no te preocupes todo esto ocurre en un servidor web, nada se instalará en tu computadora.

- Una vez que se instalaron las librerías requeridas, podrás
leer en la ventana del lado derecho lo que ha generado el algoritmo, y del lado izquierdo estará los archivos "markovid-19.wav" los cuales podrás reproducir al darles click.

¿Cómo funciona?

Las cadenas de markov deben su nombre al matemático Andréi Márkov y  parten de procesos aleatorios donde la probabilidad de que ocurra un evento depende solamente del estado inmediatamente anterior de un conjunto de valores. En las diccionarios de primer orden el algoritmo toma como referencia la penúltima palabra para decidir cual le podría seguir partiendo de una selección aleatoria de palabras de acuerdo con la base de datos introducida. En cambio, las diccionarios de tercer orden toman como referencia 3 palabras antes de seleccionar la siguiente. Dependiendo de la cantidad de palabras diferentes que le sigan a una palabra dada, será la probabilidad de aparición que se le asignará a las posibles palabras o grupo de palabras consecuentes.

Referencias:
https://setosa.io/ev/markov-chains/
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
    lineas = lineas.replace('\r', ' ').replace('\n', '')
    nuevas_palabras = lineas.split(' ')
    nuevas_palabras = [palabra for palabra in nuevas_palabras if palabra not in ['', ' ']]
    palabras = palabras + nuevas_palabras

diccionario = {}
n_palabras = len(palabras)

for i, palabra in enumerate(palabras):
    if n_palabras > (i + 1):
        nueva_palabra = palabras[i + 1]
        if palabra not in diccionario:
            diccionario[palabra] = [nueva_palabra]
        else:
            diccionario[palabra].append(nueva_palabra)

w1 = random.choice(palabras)
tweet = w1
while len(tweet) < 350:
    w2 = random.choice(diccionario[w1])
    tweet += ' ' + w2
    w1 = w2

print('Hay un Corpus de: ', str(n_palabras), ' palabras.', 'y un total de: ', str(len(diccionario)), ' palabras diferentes.')

print('\n', 'Markovid-19 de primer orden')
print('\n', tweet)

salida = gTTS(text=tweet, lang=lang)
salida.save('./markovid-19_primer_orden.wav')

#### Markovid-19 de segundo orden ####

diccionario = {}  
n_words = len(palabras)  
for i, palabra1 in enumerate(palabras):  
    if n_words > i + 2:
        palabra2 = palabras[i + 1]
        nueva_palabra = palabras[i + 2]
        if (palabra1, palabra2) not in diccionario:
            diccionario[(palabra1, palabra2)] = [nueva_palabra]
        else:
            diccionario[(palabra1, palabra2)].append(nueva_palabra)
        
r = random.randint(0, len(palabras) - 1) 
nueva_palabra = (palabras[r], palabras[r + 1])
tweet = nueva_palabra[0] + ' ' + nueva_palabra[1] 
while len(tweet) < 350:  
    w = random.choice(diccionario[nueva_palabra])
    tweet += (" " + w)
    nueva_palabra = (nueva_palabra[1], w)

print('\n', 'Markovid-19 de tercer orden')
print('\n', tweet)

salida = gTTS(text=tweet, lang=lang)
salida.save('./markovid-19_segundo_orden.wav')

#### Markovid-19 de tercer orden: adquiere un poco más de sentido lógico ####

diccionario = {}  
n_words = len(palabras)  
for i, palabra in enumerate(palabras):  
    if n_words > i + 3:
        palabra2 = palabras[i + 1]
        palabra3 = palabras[i + 2]
        nueva_palabra = palabras[i + 3]
        if (palabra, palabra2, palabra3) not in diccionario:
            diccionario[(palabra, palabra2, palabra3)] = [nueva_palabra]
        else:
            diccionario[(palabra, palabra2, palabra3)].append(nueva_palabra)  

r = random.randint(0, len(palabras) - 1) 
nueva_palabra = (palabras[r], palabras[r + 1], palabras[r + 2])
tweet = nueva_palabra[0] + ' ' + nueva_palabra[1] + ' ' +  nueva_palabra[2]
while len(tweet) < 350:  
    w = random.choice(diccionario[nueva_palabra])
    tweet += (" " + w)
    nueva_palabra = (nueva_palabra[1], nueva_palabra[2], w)

print('\n', 'Markovid-19 de tercer orden')
print('\n', tweet)

salida = gTTS(text=tweet, lang=lang)
salida.save('./markovid-19_tercer_orden.wav')


'''
Fuentes de la base de datos

fuentes: 

http://documentos.bancomundial.org/curated/es/360641469672178646/text/323020SPANISH0Handwashing.txt

https://www.who.int/es/emergencies/diseases/novel-coronavirus-2019/advice-for-public

https://elpais.com/ideas/2020-03-21/la-emergencia-viral-y-el-mundo-de-manana-byung-chul-han-el-filosofo-surcoreano-que-piensa-desde-berlin.html

https://elpais.com/especiales/2020/coronavirus-covid-19/predicciones/se-buscan-parejas-estables/

https://elpais.com/especiales/2020/coronavirus-covid-19/predicciones/organicemos-una-forma-de-vida-mas-modesta/

https://elpais.com/especiales/2020/coronavirus-covid-19/predicciones/el-aislamiento-puede-ser-creativo/

https://www.marca.com/claro-mx/trending/2020/05/01/5eababca22601d200e8b4578.html

https://elpais.com/america/sociedad/2020-05-03/coronavirus-en-america-ultimas-noticias-de-la-covid-19-en-vivo.html

https://www.clinicbarcelona.org/noticias/el-antiviral-remdesivir-muestra-eficacia-para-reducir-el-tiempo-de-recuperacion-de-pacientes-con-covid-19

https://www.clinicbarcelona.org/noticias/un-estudio-del-hospital-clinic-idibaps-y-el-csic-busca-predecir-la-gravedad-de-la-infeccion-por-el-sars-cov-2

http://www.sepsiq.org/file/InformacionSM/SEP%20COVID19-Salud%20Mental%20Cuarentena.pdf

https://www.rankiapro.com/covid-19-vs-gran-depresion-1929-diferencias-similitudes/
'''