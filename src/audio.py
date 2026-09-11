'''
Este programa convierte texto en audio. Utiliza la biblioteca gtts para 
procesar el texto y generar audio.
'''

#---Importar paquetes---
from gtts import gTTS
from datetime import datetime
import os

'''
==============================================================================
                        Definición de la clase audio                       
==============================================================================
'''

class Audio:
    #---Inicializar la clase con el texto---
    def __init__(self, texto, idioma='es'):
        '''
        Constructor de la clase audio.

        Parámetros:
        texto (str): El texto que se desea convertir en audio.
        idioma (str): El idioma del audio. Por defecto es 'es' (español).
        '''
        self.texto = texto
        self.idioma = idioma

    #---convertir el texto en audio---
    def convertir(self):
        '''
        Convierte el texto en audio y lo guarda en un archivo mp3.
        '''
        tts = gTTS(text=self.texto, lang=self.idioma)

        fecha_hora = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        archivo = f'audios/audio_{fecha_hora}.mp3'

        os.makedirs('audios', exist_ok=True)

        tts.save(archivo)

        return archivo