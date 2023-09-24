import pathlib
text_extensions = {'.txt', '.csv', '.log', '.xml', '.json', '.html'}  # Add more text file extensions as needed
def main():
    # Se obtiene carpeta desde el usuario
    ruta_str = input("Escribe la carpeta ")
    ruta = pathlib.Path(ruta_str)
    
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

def es_archivo_texto(name):
    return get_file_extension(str(name)).lower() in text_extensions

def get_file_extension(filename):
    # Find the last dot in the filename
    last_dot_index = filename.rfind('.')
    
    if last_dot_index != -1:
        # Extract and return the file extension
        return filename[last_dot_index:].lower()
    else:
        # If there is no dot in the filename, return an empty string
        return ""
        
if __name__ == "__main__":
    main()


