'''Este programa descarga y analiza los artículos de un sitio web, extrayendo 
información relevante como el título, autor, fecha de publicación, cantidad de
caracteres y resumen. Utiliza la biblioteca newspaper3K para procesar el HTML 
y obtener los datos necesarios.'''

#---Importar paquetes---
from newspaper import Article

#---Bienvenida al usuario---
print('')
print('==========================================')
print('Bienvenido al analizador de artículos web.')
print('==========================================')
print('')

#---Solicitar al usuario la URL del artículo a analizar---
url = input('Ingresa la URL del artículo que deseas analizar: ')

#---Intentar descargar y analizar el artículo---
try:
    article = Article(url)

    article.download()

    article.parse()

#---Manejo de errores en caso de que no se pueda analizar el artículo---
except Exception as e:
    print('No fue posible analizar el artículo.')
    print('')
    print('Verifica que: ')
    print('')
    print('-La URL sea correcta')
    print('-Tenga conexión a internet')
    print('-El sitio permita la extracción de contenido')

    exit()

print('')

#---Imprimir el titulo del artículo---
print('Título del artículo:')
print(article.title)
print('')

#---Imprimir el autor o autores del artículo---
print('Autor(es) del artículo:')
print(article.authors)
print('')

#---Imprimir la fecha de publicación del artículo---
#---Si la fecha de publicación no está disponible, se muestra un mensaje 
# indicando que no está disponible---
if article.publish_date is None:
    print('Fecha de publicación:')
    print('No disponible')
    print('')

#---Si la fecha de publicación está disponible, se muestra la fecha---
else:
    print('Fecha de publicación del artículo:')
    print(article.publish_date)
    print('')

#---Imprimir la cantidad de caracteres del artículo---
print('Caracteres del artículo:')
print(len(article.text))
print('')

#--Analizar el artículo para obtener un resumen---
article.nlp()

#---Imprimir el resumen del artículo---
print('Resumen del artículo:')
print(article.summary)