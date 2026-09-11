main.py
'''
    try: #Intentar obtener el idioma del artículo
        idioma = extractor.obtener_idioma()

    except Exception as e: #Manejo de errores en caso de que no se pueda 
                           #obtener el idioma
        print('error:', e)

        print('No fue posible obtener el idioma del artículo de manera ' \
        'automatica.')

        idioma = input('Por favor ingresa el idioma del artículo (por ejemplo, ' \
        '"es" para español, "en" para inglés): ')
    '''

extractor.py
'''
if self.article.meta_lang is not None:
            return self.article.meta_lang

        else:
            print('El articulo no tiene un idioma especificado')

            idioma = detect(self.article.text)

            #idioma = None

            if idioma is not None:
                return idioma

            else:
                print('No fue posible detectar el idioma del articulo')
                return idioma
'''