#Notas: 1.- utilizar funciones y mandar llamar desde otro archivo. 2.- Utilizar una lizta para almacenar los nombres de las peliculas 
import os
os.system("cls")

import peliculas_v1

opcion=True
while opcion:
    peliculas_v1.borrarPantalla()
    print("\n\t\t...::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t\t 1.- Agregar  \n\t\t\t 2.- Eliminar \n\t\t\t 3.- Actualizar \n\t\t\t 4.- Consultar \n\t\t\t 5.- Buscar \n\t\t\t 6.- Vaciar \n\t\t\t 7.- SALIR ")
    opcion=input("\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_v1.agregarPeliculas()
            peliculas_v1.esperaTecla ()
        case "2":
            peliculas_v1.eliminarPeliculas()
            peliculas_v1.esperaTecla () 
        case "3":
            peliculas_v1.actualizarPeliculas() 
            peliculas_v1.esperaTecla()     
        case "4":
            peliculas_v1.consultarPeliculas() 
            peliculas_v1.esperaTecla()
        case "5": 
            peliculas_v1.buscarPeliculas()
            peliculas_v1.esperaTecla()
        case "6": 
            peliculas_v1.vaciarPelicula()
            peliculas_v1.esperaTecla()
        case "7":
            opcion=False    
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")