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
      🎧 Audio guardado en /audios

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
