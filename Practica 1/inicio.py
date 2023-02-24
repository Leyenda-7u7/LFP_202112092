import carga as c
import os
import subprocess



def filtraraño():
    añoselec = input("Ingrese el año: ")
    for pelicula in c.peliculas:
        peliculanueva = c.peliculas[pelicula]
        nombre = peliculanueva.nombre
        año = peliculanueva.anio
        if añoselec == año:
            print(f"Nombre: {nombre} Año: {año}")
            
def filtrargenero():
    generoselec = input("Ingrese el genero: ")
    for pelicula in c.peliculas:
        peliculanueva = c.peliculas[pelicula]
        nombre = peliculanueva.nombre
        genero = peliculanueva.genero
        if generoselec == genero:
            print(f"Nombre: {nombre} Genero: {genero}")
            
def filtraractor():
    actorselec = input("Ingrese el actor: ")
    for pelicula in c.peliculas:
        peliculanueva = c.peliculas[pelicula]
        nombre = peliculanueva.nombre
        for actor in peliculanueva.autores:
            if actorselec == actor:
                print(f"Nombre: {nombre} Actor: {actor}")
    
def menufiltrado():
    print("1.Filtrar Actor")
    print("2.Filtrar Año")
    print("3.Filtrar Genero")
    sel = int(input("Seleccione una opcion:"))
    if sel == 1:
        filtraractor()
    if sel == 2:
        filtraraño()
    if sel == 3:
        filtrargenero()

def mostraractores():

    for pelicula in c.peliculas:
        peliculanueva = c.peliculas[pelicula]
        nombre = peliculanueva.nombre
        print(nombre)

    eleccion = input("Seleccione una pelicula: ")
    if eleccion in c.peliculas:
        peliculanueva = c.peliculas[eleccion]
        nombre = peliculanueva.nombre
        for actor in peliculanueva.autores:
            print(f"Nombre: {nombre} Actor: {actor}")

def grafico():
    entradaarchivo = 'Lagrafica.dot'
    salidaarchivo = 'grafico.png'
    
    subprocess.run(['dot', '-Tpng', entradaarchivo, '-o', salidaarchivo])
    
    os.startfile(salidaarchivo)

def realizargrafico():
    wendy = 'digraph grafo {\n rankdir = LR \n  node [shape = none]'
    
    
    for pelicula in c.peliculas:
        pelicula = c.peliculas[pelicula]
        nombre = pelicula.nombre
        anio = pelicula.anio
        genero = pelicula.genero
        
        
        wendy += '"'+ nombre +'"[label= <<table border="0" cellspacing="0">\
        <tr><td border="1" colspan="2" bgcolor="brown">'+ nombre + '</td></tr>\
        <tr><td border="1">'+ genero + '</td><td border="1">'+ anio + '</td></tr>\
        </table>>]'
        
        for actor in pelicula.autores:
            wendy += '"'+ actor + '"[label= <<table border="0" cellspacing="0">\
            <tr><td border="1" bgcolor="teal">'+ actor + '</td></tr>\
            </table>>]'
            
            wendy+= '"'+ nombre + '" -> "' + actor + '"'
            
    wendy += '}'   
    
    archivo = open("Lagrafica.dot","w")
    archivo.write(wendy)     
    archivo.close()
    
def inicio():
    print("Seccion B+ / 202112092 / Brandon Eduardo Pablo Garcia")
    print("Bienvenido al sistema de carga de peliculas")
    print("--------------------------------------")
    input()

    open = 0

    while open != 5:
        print("\n--------------------------------------")
        print("Menu Principal")
        print("1. Cargar peliculas")
        print("2. Gestionar peliculas")
        print("3. Fitrar peliculas")
        print("4. Grafico de peliculas")
        print("5. Salir")
        print("--------------------------------------")
        print("Ingrese una opcion: ")
        open = int(input())
        if open == 1:
            print("Cargar peliculas")
            c.leerArchivoEntrada()
            print("Peliculas cargadas con exito")
        elif open == 2:
            print("\n--------------------------------------")
            print("Gestionar peliculas")
            print("1. Mostrar peliculas")
            print("2. Mostrar actores")
            print("--------------------------------------")
            gestion = int(input("Ingrese una opcion: "))
            if gestion == 1:
                c.mostrar()
            elif gestion == 2:
                mostraractores()
        elif open == 3:
            menufiltrado()
        elif open == 4:
            realizargrafico()
            grafico()
        elif open == 5:
            print("Vuelva pronto")
            break

if __name__ == "__main__":
    inicio()
