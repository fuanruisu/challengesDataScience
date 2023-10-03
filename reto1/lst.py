import pathlib
import sys
import mimetypes

text_extensions = {'.txt', '.csv', '.log', '.xml', '.json', '.html'}  # Add more text file extensions as needed
def main(carpeta):    
    # Se obtiene carpeta desde el usuario
    ruta = pathlib.Path(carpeta)
    
    # Se obtiene la lista de archivos a partir de ruta
    archivos = obtener_archivos_texto(ruta)  # Se asume que existirá una función que resolverá la tarea
    
    # Se imprime la lista
    print("La lista de archivos de texto es:")
    for nom in archivos:
        print(nom)
        
def obtener_archivos_texto(ruta):
    """ Obtiene la lista de archivos de ruta y regresa sólo los que son
    archivos de texto """
    archivos = []
    for item in ruta.iterdir():  # como ruta es de tipo PosixPath o WindowsPath
        if item.is_file():  # Si el item es un archivo lo agregamos a la lista
            ## Complementa con un if y una función para determinar si el archivo es de
            ## texto entonces lo agregamos a la lista, si no, no hacemos nada y pasamos
            ## al siguiente
            if es_archivo_texto(item):
                archivos.append(item)
        else:  # Si el item no es un archivo entonces es una carpeta y otenemos la lista de arcivos
            lista_archivos_subruta = obtener_archivos_texto(item)  # <-ruta
            archivos = archivos + lista_archivos_subruta  # Lo concatemos a la lista de archivos[]
    return archivos 

def es_archivo_texto(file_path):
    mime_type, encoding = mimetypes.guess_type(file_path)
    if mime_type:
        return mime_type.startswith('text/')
    else:
        return False

        
if __name__ == "__main__":
    if len(sys.argv) != 2:

        raise ValueError("You must provide exactly one argument i.e. python lst.py <directorio>")

    else:

        try:

            arg1 = sys.argv[1]
            main(arg1)

        except Exception as e:
            print(f"An error occurred: {e}")


