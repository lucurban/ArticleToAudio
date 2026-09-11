'''
Este programa toma un articulo de internet solicitando al usuario la url del 
articulo y lo convierte en audio.
'''

#---Importar paquetes---
from extractor import Extractor
from audio import Audio

#---Mostrar un mensaje de bienvenida al usuario---
print('')
print('=====================================================')
print('Bienvenido al convertidor de artículos web en audios')
print('=====================================================')
print('')

#---Solicitar al usuario la url del articulo a convertir en audio---
url = input('Ingresa la URL del artículo que deseas convertir en audio: ')

#---Analizar el articulo y extraer el texto y el idioma del mismo con la 
# clase extractor---
extractor = Extractor(url) # Instancia de la clase extractor

try: #Intentar descargar y analizar el artículo
    extractor.descargar()

    extractor.analizar()

    idioma = extractor.obtener_idioma() 

    if idioma is None: # Si no se pudo obtener el idioma del artículo, 
                       #solicitar al usuario que lo ingrese manualmente
        print('No fue posible obtener el idioma del artículo de manera ' \
              'automatica')

        idioma = input('Ingresa el idioma del artículo (por ejemplo, "es" para' \
        ' español, "en" para inglés o "fr" para francés, entre otros): ')

    print('')
    print(f'El idioma del artículo es: {idioma}')

    titulo = extractor.obtener_titulo()

    texto = extractor.obtener_texto()

except Exception: #Manejo de errores en caso de que no se pueda convertir
                  #el artículo
    print('No fue posible convertir el artículo.')
    print('')
    print('Verifica que: ')
    print('')
    print('-La URL sea correcta')
    print('-Tengas conexión a internet')
    print('-El sitio web permita la extracción de contenido')

    exit()

print('')
print('El articulo esta siendo convertido en audio, por favor espera...')

#---Convertir el texto del articulo en audio con la clase audio---
audio = Audio(texto, idioma) #Instancia de la clase audio

try: #Intentar convertir el texto del artículo en audio
    ruta = audio.convertir()

#---Manejo de errores en caso de que no se pueda convertir el articulo en 
# audio---
except Exception as e:
    print('error:', e)

    print('No fue posible convertir el artículo en ' \
    'audio.')
    print('Por favor verifica tu conexión a internet')

    exit()

#---Informar al usuario que el audio ha sido creado y guardado---
print('')
print(f'El artículo "{titulo}" ha sido convertido en audio y guardado en: ' \
      f'{ruta}.')
print('')