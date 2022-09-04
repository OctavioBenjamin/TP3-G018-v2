from registro import *

def main():
    opcion = -1

    while opcion != 0:
        opcion = menu()
        cargados = False
        if opcion == 1 and cargados == False:
            proyectos, numeros = [], []
            n = validar_mayor_que(0)
            proyectos, numeros = cargar_proyecto(n, proyectos, numeros)
            
            cargados = True
            opcion = menu()

        elif opcion == 0:
            print("¡Nos Vemos!")

        if len(proyectos) > 0:
            if opcion == 2:
                
                # cambiar_numeros(proyectos, numeros)
                ordenamiento_ss_alf(proyectos)
                mostrar_proyectos(proyectos)
                opcion = menu()

            elif opcion == 1 and cargados == True: #Agrega proyectos
                n = validar_mayor_que(0)
                # numeros = numeros_de_proyectos(proyectos)
                # numeros = quitar_repetidos(numeros)
                proyectos, numeros = cargar_proyecto(n, proyectos, numeros)

                opcion = menu()

            elif opcion == 3:
                
                num_filtro = validar_mayor_que(0, "Ingrese un numero de proyecto a buscar: ")
                ordenamiento_ss_num(proyectos)
                indice = binary_search_numeros(proyectos, num_filtro)
                if indice >= 0:
                    print(toString(proyectos[indice]))
                    nuevas_lineas = validar_mayor_que(0, "Nueva cantidad de lineas: ")
                    actualizar(proyectos[indice], nuevas_lineas)
                    print(f"ACTUALIZACION: {toString(proyectos[indice])}")
                else:
                    print("No se ha encontrado el proyecto\n")

                opcion = menu()

            elif opcion == 4:
                contador = contar_lineas(proyectos)
                mostrar_contador(contador)
            
            


if __name__ == "__main__":
    main()