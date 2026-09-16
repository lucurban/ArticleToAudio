# 🎧 ArticleToAudio

🌐 **ArticleToAudio** es una aplicación desarrollada en **Python** que permite convertir el contenido de artículos web en archivos de audio en formato **MP3.**

🔗 El programa recibe la URL de un artículo, extrae y analiza su contenido utilizando newspaper3k, 🔤 identifica el idioma del texto y posteriormente 🔊 utiliza gTTS para generar el archivo de audio correspondiente.

🧱 Este proyecto fue desarrollado como parte de mi proceso de aprendizaje en desarrollo de software y representa una aplicación práctica de **Programación Orientada a Objetos (POO),** separación de responsabilidades, manejo de errores y uso de librerías externas.

🚀 La primera versión se centra en construir una base funcional y organizada sobre la cual puedan incorporarse nuevas características en futuras versiones.

## 📝 Descripción

**🎯 ArticleToAudio** nace como una herramienta para transformar artículos escritos en contenido de audio, facilitando su consumo mientras se realizan otras actividades.

⚙️ La aplicación automatiza el proceso completo:

* 🌐 Recibe la URL de un artículo web.
* 📥 Descarga y analiza su contenido.
* 📄 Extrae el título y el texto principal.
* 🔤 Determina el idioma del artículo mediante sus metadatos y, cuando no están disponibles, utiliza langdetect como alternativa.
* 🔊 Convierte el texto en audio utilizando gTTS.
* 💾 Guarda el resultado como un archivo .mp3.

🧩 El proyecto está organizado mediante **Programación Orientada a Objetos,** separando las responsabilidades relacionadas con la extracción del contenido y la generación del audio.

💡 Además de cumplir una función práctica, ArticleToAudio fue concebido como un proyecto de aprendizaje para aplicar conceptos de Python en una solución funcional, integrando diferentes librerías y resolviendo situaciones reales de manejo de datos, detección de idioma y generación de archivos.

## ✨ Características

* **🌐 Extracción de artículos web:** recibe una URL y descarga automáticamente el contenido del artículo.
* **📄 Obtención del contenido:** extrae el título y el texto principal del artículo.
* **🔤 Detección automática del idioma:** utiliza los metadatos del artículo y langdetect como alternativa cuando             estos no están disponibles.
* **🔊 Conversión de texto a voz:** transforma el contenido del artículo en un archivo de audio mediante gTTS.
* **🎧 Generación de archivos MP3:** guarda automáticamente el audio generado en formato .mp3.
* **🕐 Nombres de archivo dinámicos:** utiliza la fecha y hora de generación para identificar cada archivo de audio.
* **⚠️ Manejo de errores:** contempla situaciones como problemas de conexión, URLs incorrectas o dificultades durante         la extracción y conversión.
* **🧱 Programación Orientada a Objetos:** utiliza clases independientes para separar las responsabilidades                   principales de la aplicación.
* **📁 Organización del proyecto:** mantiene separadas las funciones de extracción de contenido y generación de audio         para facilitar su mantenimiento y futuras mejoras.

## 🛠️ Tecnologías y Librerías

### 🐍 Lenguaje

* **Python 3.12 —** Lenguaje utilizado para desarrollar toda la aplicación.
  
### 📚 Librerías

* **🌐 newspaper3k —** Descarga, analiza y extrae el contenido principal de los artículos web.
* **🔤 langdetect —** Detecta automáticamente el idioma del texto cuando no es posible obtenerlo desde los metadatos          del artículo.
* **🔊 gTTS —** Convierte el texto extraído en audio utilizando el servicio de Google Text-to-Speech.

### 🧩 Conceptos aplicados

* **🧱 Programación Orientada a Objetos (POO)**
* **🔄 Separación de responsabilidades**
* **⚠️ Manejo de excepciones**
* **📦 Uso y gestión de librerías externas**
* **📁 Organización modular del proyecto**
* **🖥️ Interacción con el usuario mediante consola**

## 📁 Estructura del Proyecto

El proyecto está organizado de manera modular, separando las responsabilidades principales de la aplicación:

<code>ArticleToAudio/
│
├── 📂 src/
│   ├── 📄 main.py
│   ├── 📄 extractor.py
│   └── 📄 audio.py
│
├── 📂 audios/
│   └── 🎧 Archivos MP3 generados
│
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md</code>

📄 Archivos principales

### 🖥️ main.py

Es el punto de entrada de la aplicación. Se encarga de interactuar con el usuario, coordinar el proceso de extracción y conversión, y mostrar los resultados.

### 🌐 extractor.py

Contiene la clase Extractor, responsable de descargar y analizar el artículo, así como de obtener su título, texto e idioma.

### 🔊 audio.py

Contiene la clase Audio, responsable de convertir el texto recibido en un archivo de audio .mp3 mediante gTTS.

### 📂 Otros elementos

#### 🎧 audios/

Directorio destinado a almacenar los archivos MP3 generados por la aplicación. Estos archivos son ignorados por Git mediante .gitignore.

#### 📦 requirements.txt

Contiene las dependencias necesarias para instalar las librerías utilizadas por el proyecto.

#### 🚫 .gitignore

Define los archivos y directorios que no deben ser incluidos en el control de versiones, como los archivos de audio generados y la configuración local de VS Code.

#### 📖 README.md

Documento principal del proyecto, donde se describe su funcionamiento, estructura, instalación y uso.

## ⚙️ Funcionamiento

ArticleToAudio sigue un flujo sencillo en el que cada componente de la aplicación se encarga de una responsabilidad específica.

### 🔄 Flujo de ejecución

<code>👤 Usuario
          │
          │ Introduce la URL
          ▼
      🖥️ main.py
          │
          ▼
      🌐 Extractor
          │
          ├── 📥 Descarga el artículo
          │
          ├── 🔎 Analiza su contenido
          │
          ├── 📄 Obtiene el título
          │
          ├── 📝 Obtiene el texto
          │
          └── 🔤 Obtiene el idioma
          │
          ▼
      🔊 Audio
          │
          ├── Recibe texto + idioma
          │
          ├── ⚙️ Procesa el texto con gTTS
          │
          └── 💾 Genera el archivo MP3
          │
          ▼
      🎧 Audio guardado en /audios</code>

### 1. 🌐 Recepción y extracción del artículo

El usuario introduce la URL del artículo que desea convertir. main.py crea una instancia de la clase Extractor y le proporciona dicha URL.

Extractor utiliza **newspaper3k** para descargar y analizar el contenido de la página web.

### 2. 📄 Obtención de la información

Una vez analizado el artículo, Extractor obtiene:

* 📰 El título.
* 📝 El texto principal.
* 🔤 El idioma.

Para determinar el idioma, primero se consulta la información disponible en los metadatos del artículo. Si no está disponible, se utiliza langdetect para intentar identificarlo a partir del texto.

### 3. 🔊 Conversión a audio

main.py crea una instancia de la clase Audio utilizando el texto extraído y el idioma detectado.

La clase Audio utiliza **gTTS** para convertir el texto en voz y genera un archivo en formato .mp3.

### 4. 💾 Almacenamiento

El archivo generado se guarda dentro del directorio audios/ utilizando un nombre basado en la fecha y hora de creación:

audios/audio_YYYY-MM-DD_HH-MM-SS.mp3

Finalmente, main.py informa al usuario que el proceso ha terminado y muestra la ubicación del archivo generado.

#### 🔤 Flujo alternativo para el idioma

Si no es posible determinar automáticamente el idioma del artículo, la aplicación solicita al usuario que lo introduzca manualmente.

              ¿Idioma disponible?
                       │
                 ┌─────┴───────┐
                Sí             No
                 │             │
                 ▼             ▼
            Usar idioma     langdetect
            encontrado         │
                               │
                       ¿Se pudo detectar?
                               │
                         ┌─────┴─────┐
                        Sí           No
                         │           │
                         ▼           ▼
                  Usar idioma    Solicitar idioma
                  detectado      al usuario

De esta manera, ArticleToAudio dispone de tres posibilidades para obtener el idioma: metadatos del artículo, detección mediante langdetect o introducción manual por parte del usuario.

## 📦 Instalación

Para ejecutar ArticleToAudio, es necesario tener instalado Python 3.12 y configurar un entorno con las dependencias del proyecto.

### 1. 📥 Clonar el repositorio

Clona el repositorio desde GitHub:

git clone https://github.com/lucurban/ArticleToAudio.git

Después, entra en la carpeta del proyecto:

cd ArticleToAudio

### 2. 🐍 Crear un entorno virtual

Se recomienda utilizar un entorno virtual para mantener aisladas las dependencias del proyecto.

python3 -m venv .venv

Activa el entorno virtual:

**🐧 Linux / macOS**
source .venv/bin/activate

**🪟 Windows**
.venv\Scripts\activate

### 3. 📚 Instalar las dependencias

Con el entorno virtual activado, instala las librerías necesarias mediante el archivo requirements.txt:

pip install -r requirements.txt

### 4. ▶️ Ejecutar la aplicación

Finalmente, ejecuta el archivo principal:

python src/main.py

La aplicación solicitará la URL del artículo que deseas convertir en audio.

## ▶️ Uso

Una vez instaladas las dependencias, ejecuta la aplicación desde la carpeta raíz del proyecto:

python src/main.py

### 📝 Pasos para utilizar ArticleToAudio

1. 🌐 Introduce la URL del artículo web que deseas convertir.
2. 📥 Espera mientras la aplicación descarga y analiza el contenido.
3. 🔤 Si el idioma no puede detectarse automáticamente, introdúcelo manualmente utilizando su código correspondiente.
4. 🔊 Espera mientras el texto se convierte en audio.&nbsp;
5. 🎧 Consulta la ruta mostrada en consola para acceder al archivo .mp3 generado.

### 💻 Ejemplo de uso

Bienvenido al convertidor de artículos web en audios

Ingresa la URL del artículo que deseas convertir en audio: https://ejemplo.com/articulo

El idioma del artículo es: es

El articulo esta siendo convertido en audio, por favor espera...

El artículo "articulo" ha sido convertido en audio y guardado en: audios/audio_2026-09-15_19-35-44.mp3.

## 🔤 Detección del idioma

ArticleToAudio utiliza un proceso de detección de idioma para seleccionar la configuración adecuada de conversión de texto a voz.

La aplicación emplea dos métodos principales:

### 1. 🌐 Detección mediante metadatos

En primer lugar, 'Extractor.py' consulta los metadatos del artículo obtenidos mediante **'newspaper3k'**.

Si el idioma está disponible en dichos metadatos, se utiliza directamente.

### 2. 🧠 Detección mediante el texto

Si los metadatos no contienen información sobre el idioma, la aplicación utiliza la librería **'langdetect'** para analizar el texto extraído e intentar identificar su idioma.

### 3. 👤 Introducción manual del idioma

Si ninguno de los métodos anteriores permite identificar el idioma, la aplicación solicita al usuario que lo introduzca manualmente.

Por ejemplo:

--------
No fue posible obtener el idioma del artículo de manera automatica

Ingresa el idioma del artículo (por ejemplo, "es" para  español, "en" para inglés o "fr" para francés, entre otros):

--------


De esta manera, ArticleToAudio puede continuar con la conversión siempre que el usuario proporcione un código de idioma compatible con gTTS.

ℹ️ La detección automática puede presentar dificultades cuando el texto es demasiado corto, contiene varios idiomas o no tiene suficiente información para identificarlo correctamente.

## ⚠️ Manejo de errores

ArticleToAudio incorpora un manejo básico de errores para informar al usuario cuando ocurre algún problema durante la extracción del artículo o la generación del archivo de audio.

### 🌐 Errores durante la extracción

Si se presenta un problema al descargar o analizar el artículo, la aplicación muestra el siguiente mensaje:

--------
text

No fue posible convertir el artículo.

Verifica que:

-La URL sea correcta

-Tengas conexión a internet

-El sitio web permita la extracción de contenido

--------

Este bloque contempla posibles situaciones como:

* 🔗 Una URL incorrecta o no válida.
* 🌐 Problemas de conexión a internet.
* 🚫 Sitios web que no permiten la extracción de contenido.
* 📄 Errores durante la descarga o el análisis del artículo.

### 🔤 Error en la detección del idioma

Si no es posible obtener automáticamente el idioma del artículo, la aplicación solicita al usuario que lo introduzca manualmente.

--------
No fue posible obtener el idioma del artículo de manera automatica

Ingresa el idioma del artículo (por ejemplo, "es" para español, "en" para inglés o "fr" para franccés, entre otros):

--------

De esta manera, el proceso puede continuar utilizando el código de idioma proporcionado por el usuario.

### 🔊 Errores durante la conversión a audio

Si ocurre un problema al convertir el texto en audio, la aplicación muestra un mensaje informativo:

--------
No fue posible convertir el artículo en audio.
Por favor verifica tu conexión a internet

--------

Este error puede producirse, por ejemplo, cuando:

🌐 No existe conexión a internet.

🔊 El servicio utilizado por gTTS no está disponible.
⚙️ Se presenta un problema durante la generación o el guardado del archivo MP3.

### 🧩 Implementación

El manejo de errores se realiza mediante bloques try y except, que permiten controlar las excepciones y mostrar mensajes comprensibles para el usuario en lugar de finalizar el programa mostrando únicamente un error técnico.
