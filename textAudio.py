'''Este programa toma un texto creado por el usuario y lo convierte en audio. 
Utiliza la biblioteca gTTS para convertir el texto en audio.'''

#---Importar paquetes---
from gtts import gTTS

#---Bienvenida al usuario---
print('')
print('==========================================')
print('Bienvenido al convertidor de frases en audio.')
print('==========================================')
print('')

#---Solicitar al usuario la frase a convertir en audio---
frase = input('Ingresa la frase que deseas convertir en audio: ')

if not frase.strip():
    print('Debes ingresar una frase')
    exit()

#---Solicitar al usuario el idioma en que desea el audio---
idioma = input('Ingresa el idioma del audio (por ejemplo, "es" ' \
'para español, "en" para inglés): ')

if not idioma.strip():
    print('Debes ingresar un idioma')
    exit()

#---Intentar convertir la frase en audio---
try:
    tts = gTTS(text=frase, lang=idioma)

    archivo = 'audios/frase.mp3'

    tts.save(archivo)

    print(f'La frase ha sido convertida en audio y guardada en "{archivo}".')

#---Manejo de errores en caso de que no se pueda convertir la frase en audio---
except Exception as e:
    print('No fue posible convertir la frase en audio.')
    print('Por favor verifica tu conexión a internet o el idioma ingresado.')