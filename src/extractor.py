'''
Este programa descarga y analiza un sitio web para obtener su contenido 
textual. Utiliza la biblioteca newspaper3K para procesar el HTML y obtener el 
texto.
'''

#---Importar paquetes---
from newspaper import Article

'''
==============================================================================
                        Definición de la clase extractor                       
==============================================================================
'''

class Extractor:
    #---Inicializar la clase con la URL del artículo---
    def __init__(self, url):
        '''
        Constructor de la clase extractor.

        Parámetros:
        url (str): La URL del artículo a analizar. 
        '''
        self.url = url
        self.article = None

    '''
    ==========================================================================
                        Metodos principales de la clase                     
    ==========================================================================
    '''

    #---Método para descargar el articulo
    def descargar(self):
        '''
        Descarga el artículo desde la URL proporcionada y lo almacena en un objeto Article.
        '''
        self.article = Article(self.url)

        self.article.download()

    #---Método para analizar el artículo---
    def analizar(self):
        '''
        Analiza el artículo descargado.
        '''
        #---Analizar el artículo descargado---
        self.article.parse()

    def obtener_texto(self):
        '''
        Obtiene el texto completo del artículo.
        '''
        return self.article.text