
# FlashMusic

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Android-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen)

> Un descargador de música de YouTube con interfaz por consola interactiva. Diseñado para ser simple, robusto y fácil de usar.

## Tabla de Contenidos

- [Características Principales](#-características-principales)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Uso Básico](#-uso-básico)
- [Estructura del Código](#-estructura-del-código)
- [Guía de Solución de Problemas](#-guía-de-solución-de-problemas)
- [Personalización](#-personalización)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

## Características Principales

- **Búsqueda Integrada**: Busca hasta 4 videos de YouTube directamente desde la consola
- **Descarga en MP3**: Convierte automáticamente a audio MP3 con calidad ajustable (128, 192, 320 kbps)
- **Gestión de Archivos**: Permite seleccionar la carpeta de destino para las descargas
- **Manejo Robusto de Errores**: No se cierra ante errores del usuario, permite corregir acciones
- **Configuración Dinámica**: Cambia calidad y carpeta de destino sin reiniciar el programa
- **Interfaz Limpia**: Limpieza automática de consola para mejor experiencia
- **Formato de Duración**: Muestra la duración de los videos en formato MM:SS

## Requisitos Previos

### Dependencias del Sistema

- **Python 3.7 o superior**
- **ffmpeg** (necesario para la conversión de audio)

### Librerías de Python

```bash
pip install yt-dlp imageio-ffmpeg
````

## Instalación

### Clonar Repositorio

```bash
git clone https://github.com/tu-usuario/youtube-music-downloader.git
cd youtube-music-downloader
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Configurar FFmpeg

#### Windows
La forma más sencilla es usar el gestor de paquetes integrado de Windows:

```bash
winget install --id Gyan.FFmpeg --source winget
````
Esto instalará FFmpeg automáticamente y lo añadirá al PATH del sistema.

#### Linux

````bash
sudo apt install ffmpeg  # Ubuntu/Debian
sudo dnf install ffmpeg  # Fedora
````

#### Mac

````bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar FFmpeg
brew install ffmpeg
````

#### Verificar Instalación

Independientemente del método usado, verifica que FFmpeg esté correctamente instalado ejecutando:

````bash
ffmpeg -version
````

Deberías ver algo similar a:

````bash
ffmpeg version 9.0-full_build-www.gyan.dev Copyright (c) 2000-2026 the FFmpeg developers
````
### Solucion de Problemas

#### Windows:

Si ````ffmpeg```` no es reconocido, reinicia la terminal después de añadirlo al PATH

Asegúrate de que la ruta ````C:\ffmpeg\bin```` esté correctamente añadida

Prueba cerrar y abrir la terminal para que los cambios surtan efecto

#### Linux/Mac:

Si tienes problemas de permisos, usa ````sudo```` antes del comando de instalación

En algunas distribuciones, puede ser necesario instalar paquetes adicionales

#### Nota: FFmpeg es una herramienta esencial para este proyecto. Sin ella, no podrás convertir los videos a MP3 correctamente.

### Ejecutar la Aplicación

````bash
python main.py
````
## Uso Basico

### Menu Principal
Cuando ejecutes el programa, verás este menú:

````bash
DESCARGADOR DE MÚSICA YOUTUBE

1. Buscar y descargar música
2. Cambiar carpeta de destino
3. Cambiar calidad de audio
4. Salir

Carpeta: /home/usuario/Music/Musica
Calidad: 192 kbps
````

### Flujo de Trabajo

1. Selecciona "Buscar y descargar música" (opción 1)

2. Ingresa el término de búsqueda (ej. "bad bunny dakiti")

3. Selecciona un video de la lista de resultados

4. Espera la descarga (el archivo aparecerá en tu carpeta de música)

#### Ejemplo de búsqueda

````bash
RESULTADOS DE BÚSQUEDA

1. Bad Bunny - Dákiti (03:25)
2. Bad Bunny - Yo Perreo Sola (02:52)
3. Bad Bunny - Callaíta (03:23)
4. Bad Bunny - Safaera (03:45)

0. Volver al menú principal
````

### Configuracion de calidad de audio

El programa ofrece tres opciones de calidad:

| Opcion | Calidad     | Uso recomendado                |
| :-------- | :------- | :------------------------- |
| 1 | 	128 kbps | Ahorro de espacio, calidad básica |
| 2 | 192 kbps | Calidad equilibrada (recomendada) |
| 3 | 	320 kbps | Alta calidad, mayor tamaño |


### Estructura del Código

````bash
main.py
├── limpiar_consola()        # Limpia la pantalla según SO
├── mostrar_menu()           # Muestra el menú principal
├── obtener_opciones_descarga()  # Configura opciones de yt-dlp
├── realizar_busqueda()      # Busca videos en YouTube
├── descargar_video()        # Descarga y convierte a MP3
├── configuracion_inicial()  # Configuración al iniciar
└── menu_principal()         # Bucle principal del programa
````
## Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Haz un Fork del proyecto
2. Crea tu rama de características (````git checkout -b feature/AmazingFeature````)

3. Commit tus cambios (````git commit -m 'Add some AmazingFeature````)

4. Push a la rama (````git push origin feature/AmazingFeature````)

5. Abre un Pull Request

### Areas de Mejora
1.  Añadir soporte para listas de reproducción
2.  Implementar descarga por lotes
3.  Añadir opción para elegir formato de audio (MP3, M4A, etc.)
4.  Mejorar el manejo de errores de red
5.  Añadir barra de progreso visual
## Licencia

Este proyecto está bajo la Licencia [MIT](https://choosealicense.com/licenses/mit/) - ver el archivo [LICENSE](https://choosealicense.com/licenses/) para más detalles.


## Agradecimientos

 - [yt-dlp](https://github.com/yt-dlp/yt-dlp) - La columna vertebral del proyecto
 - [FFmpeg](https://ffmpeg.org/) - Para el procesamiento de audio
 - [imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg) - Para la integración con FFmpeg
 - A todos los contribuyentes de la comunidad open-source


## Aviso Legal

Este proyecto es solo para fines educativos y personales. Por favor:

- Respeta los derechos de autor y los términos de servicio de YouTube

- No uses este software para descargar contenido protegido por derechos de autor sin permiso

- No abuses del servicio de YouTube (evita hacer demasiadas peticiones en poco tiempo)

⭐ **¡Si te gusta este proyecto, no olvides darle una estrella en GitHub!**

