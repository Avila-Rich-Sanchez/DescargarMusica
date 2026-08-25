import yt_dlp
import imageio_ffmpeg
import os
import subprocess

def limpiar_consola():
    """Limpia la consola según el sistema operativo"""
    try:
        if os.name == 'nt':
            subprocess.run('cls', shell=True, check=True)
    except:
        print('\n' * 50)

def mostrar_menu():
    """Muestra el menú principal"""
    print("1. Buscar y descargar música")
    print("2. Cambiar carpeta de destino")
    print("3. Cambiar calidad de audio")
    print("4. Salir")

def obtener_opciones_descarga(ruta_destino, calidad):
    """Retorna las opciones de descarga configuradas"""
    return {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(ruta_destino, '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
        'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe(),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': calidad,
        }]
    }

def realizar_busqueda(termino, cantidad=4):
    """Realiza la búsqueda y retorna los resultados"""
    opciones_busqueda = {
        'extract_flat': True,
        'skip_download': True,
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(opciones_busqueda) as ydl:
        resultados = ydl.extract_info(f"ytsearch{cantidad}:{termino}", download=False)
        return resultados.get('entries', [])

def descargar_video(link, ruta_destino, calidad):
    """Descarga el video seleccionado en formato MP3"""
    try:
        opciones = obtener_opciones_descarga(ruta_destino, calidad)
        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([link])
        return True, "¡Descarga completada con éxito!"
    except Exception as e:
        return False, f"Error al descargar: {str(e)}"

def configuracion_inicial():
    """Solicita la configuración inicial al usuario"""
    limpiar_consola()

    ruta_default = os.path.expanduser("~/Music/Musica")
    print(f"\nCarpeta de destino actual: {ruta_default}")
    cambiar_ruta = input("¿Desea cambiar la carpeta? (s/N): ").strip().lower()
    
    if cambiar_ruta == 's':
        nueva_ruta = input("Ingrese la nueva ruta: ").strip()
        if nueva_ruta:
            ruta_default = nueva_ruta
    
    print("\nCalidad de audio disponible:")
    print("1. 128 kbps (Básica)")
    print("2. 192 kbps (Recomendada)")
    print("3. 320 kbps (Alta calidad)")
    
    while True:
        try:
            opcion_calidad = int(input("Seleccione una opción (1-3): "))
            if opcion_calidad == 1:
                calidad = '128'
                break
            elif opcion_calidad == 2:
                calidad = '192'
                break
            elif opcion_calidad == 3:
                calidad = '320'
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    
    return ruta_default, calidad

def menu_principal():
    """Función principal del programa"""
    ruta_destino, calidad = configuracion_inicial()
    
    while True:
        limpiar_consola()
        mostrar_menu()
        print(f"Carpeta: {ruta_destino}")
        print(f"Calidad: {calidad} kbps")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            limpiar_consola()
            
            termino = input("Ingrese el término de búsqueda: ").strip()
            
            if not termino:
                print("Término de búsqueda vacío.")
                input("Presione Enter para continuar...")
                continue
            
            print("\nBuscando...")
            videos = realizar_busqueda(termino)
            
            if not videos:
                print("No se encontraron resultados.")
                input("Presione Enter para continuar...")
                continue
            
            limpiar_consola()
            for i, video in enumerate(videos, start=1):
                titulo = video.get('title', 'Sin título')
                duracion = video.get('duration', '?')
                if duracion:
                    minutos = int(duracion // 60)
                    segundos = int(duracion % 60)
                    print(f"{i}. {titulo[:60]}... ({minutos:02d}:{segundos:02d})")
                else:
                    print(f"{i}. {titulo[:60]}... (Duración desconocida)")
            
            print("0. Volver al menú principal")

            while True:
                try:
                    eleccion = input("Seleccione el número del video: ").strip()
                    if eleccion == "0":
                        break
                    
                    eleccion = int(eleccion)
                    if 1 <= eleccion <= len(videos):
                        link_elegido = videos[eleccion-1].get('url')
                        titulo = videos[eleccion-1].get('title', 'Sin título')
                        
                        print(f"\nDescargando: {titulo[:60]}...")
                        print("Por favor espere...")
                        
                        mensaje = descargar_video(link_elegido, ruta_destino, calidad)
                        print(mensaje)
                        input("Presione Enter para continuar...")
                        break
                    else:
                        print(f"Elija un número entre 1 y {len(videos)}")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                except KeyboardInterrupt:
                    print("\nOperación cancelada.")
                    break
        
        elif opcion == "2":
            limpiar_consola()
            print(f"Carpeta actual: {ruta_destino}")
            
            nueva_ruta = input("Ingrese la nueva ruta (Enter para mantener): ").strip()
            if nueva_ruta:
                if os.path.exists(nueva_ruta):
                    ruta_destino = nueva_ruta
                    print("Carpeta actualizada correctamente.")
                else:
                    print("La ruta no existe. ¿Desea crearla?")
                    crear = input("Crear carpeta? (s/N): ").strip().lower()
                    if crear == 's':
                        try:
                            os.makedirs(nueva_ruta, exist_ok=True)
                            ruta_destino = nueva_ruta
                            print("Carpeta creada y actualizada correctamente.")
                        except Exception as e:
                            print(f"Error al crear la carpeta: {e}")
            else:
                print("Carpeta no modificada.")
            
            input("Presione Enter para continuar...")
        
        elif opcion == "3":
            limpiar_consola()
            print(f"Calidad actual: {calidad} kbps")
            print("\nOpciones disponibles:")
            print("1. 128 kbps (Básica)")
            print("2. 192 kbps (Recomendada)")
            print("3. 320 kbps (Alta calidad)")
            
            while True:
                try:
                    opcion_calidad = int(input("Seleccione una opción (1-3, 0 para cancelar): "))
                    if opcion_calidad == 0:
                        break
                    elif opcion_calidad == 1:
                        calidad = '128'
                        print("Calidad actualizada a 128 kbps")
                        break
                    elif opcion_calidad == 2:
                        calidad = '192'
                        print("Calidad actualizada a 192 kbps")
                        break
                    elif opcion_calidad == 3:
                        calidad = '320'
                        print("Calidad actualizada a 320 kbps")
                        break
                    else:
                        print("Opción inválida. Intente nuevamente.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            
            input("Presione Enter para continuar...")
        
        elif opcion == "4":
            limpiar_consola()
            print("¡Hasta pronto!")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        limpiar_consola()
        print("\n¡Programa finalizado por el usuario!")
    except Exception as e:
        print(f"Error inesperado: {e}")
        input("Presione Enter para salir...")

