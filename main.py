from registro import *

def main():
    
    opcion = menu()
    
    cargados = False
    actualizo = False
    proyectos, numeros, conteo_proyectos = [], [], [0]*23
    while opcion != 0:

        if opcion == 1 and cargados == False:
            n = validar_mayor_que(0)
            proyectos, numeros = cargar_proyecto(n, proyectos, numeros)
            
            cargados = True
            
            opcion = menu()

        if opcion == 0:
            print("¡Nos Vemos!")

        if len(proyectos) > 0:
            if opcion == 2:
                
                # cambiar_numeros(proyectos, numeros)
                ordenamiento_ss_alf(proyectos)
                mostrar_proyectos(proyectos)
                opcion = menu()

            if opcion == 1 and cargados == True: #Agrega proyectos
                n = validar_mayor_que(0)
                proyectos, numeros = cargar_proyecto(n, proyectos, numeros)

                opcion = menu()

            if opcion == 3:
                print("Bandera")
                num_filtro = validar_mayor_que(0, "Ingrese un numero de proyecto a buscar: ")
                ordenamiento_ss_num(proyectos)
                indice = binary_search_numeros(proyectos, num_filtro)
                if indice >= 0:
                    print(toString(proyectos[indice]))
                    nuevas_lineas = validar_mayor_que(0, "Nueva cantidad de lineas: ")
                    actualizar(proyectos[indice], nuevas_lineas)
                    print(f"ACTUALIZACION: {toString(proyectos[indice])}")

                    proyecto_año(proyectos, num_filtro, conteo_proyectos)   
                    actualizo = True
                else:
                    print("No se ha encontrado el proyecto\n")

                
                opcion = menu()

            if opcion == 4:
                contador = contar_lineas(proyectos)
                mostrar_contador(contador)
                opcion = menu()

            if opcion == 5:
                print(actualizo)
                if actualizo:
                    print(conteo_proyectos)
                    mostrar_por_año(conteo_proyectos)
                else:
                    print("No se han encontrado actualizaciones.\n")
                opcion = menu()
            
            if opcion == 6:
                print("""0 - Python
1 - Java
2 - C++
3 - Javascript
4 - Shell
5 - HTML
6 - Ruby     
7 - Swift    
8 - C#      
9 - VB       
10 - Go""")
                filtro_lenguaje = validar_rango(0, 10)
                filtrar_lenguaje(proyectos, filtro_lenguaje)
                opcion = menu()

            if opcion == 7:
                if actualizo:
                    mostrar_cambios(conteo_proyectos)
                else:
                    print("No se han encontrado actualizaciones.\n")
                opcion = menu()
        else:
            print("¡Error! No hay proyectos cargados")
            opcion = menu()


if __name__ == "__main__":
    main()