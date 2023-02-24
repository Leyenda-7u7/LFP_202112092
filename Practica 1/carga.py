peliculas = {}

class Pelicula:
    def __init__(self, nombre, autores, anio, genero):
        self.nombre = nombre
        self.autores = autores
        self.anio = anio
        self.genero = genero   

def crear(listapeliculas):
    for linea in listapeliculas:
        separado = linea.split(";")
        separado[1] = separado[1].split(",")
        nombre = separado[0]
        
        genero = separado[3].replace("\n", "")  
        pelicula = Pelicula(nombre, separado[1], separado[2], genero)
        peliculas[nombre] = pelicula
        
def leerArchivoEntrada():
    ruta = input("Ingrese la ruta del archivo: ")
    archivo = open(ruta, "r")
    lineas = archivo.readlines()
    
    crear(lineas)
    archivo.close()     

def mostrar():
    for pelicula in peliculas:
        peliculanueva = peliculas[pelicula]
        nombre = peliculanueva.nombre
        genero = peliculanueva.genero
        año = peliculanueva.anio 
        print(f"Nombre: {nombre} Genero: {genero} Año: {año}")
        
