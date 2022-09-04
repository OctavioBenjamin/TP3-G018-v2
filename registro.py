import random

class Proyecto:
    def __init__(self, numero, titulo, dia, mes, año, lenguaje, lineas):
        self.numero = numero
        self.titulo = titulo
        self.dia = dia
        self.mes = mes
        self.año = año
        self.lenguaje = lenguaje
        self.lineas = lineas

lenguajes = ["Python", "Java", "C++", "Javascript", "Shell", "HTML", "Ruby", "Swift", "C#", "VB", "Go"]
titulos = ["Game: Dead by daylight", "Game: Phasmophobia", "Game: Grand Theft Auto V", "Game: Call Of Duty Warzone", "Game: Fallout 4", "Software: AutoCad", "Software: Sketchup", "Software: Lumion 3D", "Software: Photoshop", "Software: V-Ray"]

def toString(proyecto):
    if proyecto.año < 10:
        año =  f"200{proyecto.año}"
    else:
        año =  f"20{proyecto.año}"
    fecha = f"{proyecto.dia}-{proyecto.mes}-{año}"
    return f"Proyecto {proyecto.titulo} | Numero: {proyecto.numero} | Ultima Actualización: {fecha} | Lenguaje: {lenguajes[proyecto.lenguaje]} | Lineas: {proyecto.lineas}"

def numeros_de_proyectos(proyectos):
    numeros = []
    for proyecto in proyectos:
        numeros.append(proyecto.numero)
    return numeros

def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


def quitar_repetidos(numeros):
    result = []
    for numero in numeros:
        if numero not in result:
            result.append(numero)
    return result
    

def cargar_proyecto(n, proyectos, numeros):
    for i in range(n):
        num = random.randint(1, 99999)
        while num in numeros:
            num = random.randint(1, 999) 
        if num not in numeros:
            numeros.append(num)
        tit = random.choice(titulos)
        dd_actu = random.randint(1,30)
        mm_actu = random.randint(1, 12) 
        yy_actu = random.randint(0, 22)
        lenguaje = random.randint(0, 10)
        lineas = random.randint(100, 999)
        # numero, titulo, dia, mes, año, lenguaje, lineas
        nuevo_proyecto = Proyecto(num, tit, dd_actu, mm_actu, yy_actu, lenguaje, lineas)
        proyectos.append(nuevo_proyecto)
    print(len(numeros))
    print(numeros)
    print("¡PROYECTOS CARGADOS!\n")
    return proyectos, numeros



def cambiar_numeros(proyectos, numeros):
    for proyecto in proyectos:
        while proyecto.numero in numeros:
            proyecto.numero = random.randint(1, 99999)
        numeros.append(proyecto.numero)

def menu():
    print("""
╔═════════════════════════╗
║  G018 SOFTWARE COMPANY  ║
╠═════════════════════════╣
║1- Cargar Proyectos      ║
║2- Listar Proyectos      ║
║3- Actualizar Proyecto   ║
║4- Resumen de Lenguajes  ║
║5- Resumen por Año       ║
║6- Filtrar Lenguaje      ║
║7- Productividad         ║
║0- Salir                 ║
╚═════════════════════════╝""")
    op = int(input("Seleccione la opcion que desea: "))
    print(" ")
    return op

def validar_mayor_que(limite, mensaje="Ingrese un numero: "):
    numero = limite
    while numero <= limite:
        numero = int(input(mensaje))
        if numero <= limite:
            print(f"¡Error! El numero debe ser mayor a {limite}")
    return numero

def validar_rango(inicio, limite):
    numero = int(input(f"Ingrese un valor entre {inicio} y {limite}: "))
    while limite < numero < inicio:
        numero = int(input(f"Ingrese un valor entre {inicio} y {limite}: "))
    return numero


def ordenamiento_ss_num(proyectos):
    long= len(proyectos)

    for i in range(long-1):
        for j in range(i+1, long):
            if proyectos[i].numero > proyectos[j].numero:
                # Intercambiar
                proyectos[i], proyectos[j] = proyectos[j], proyectos[i]

def mostrar_proyectos(proyectos):
    for proyecto in proyectos:
        print(toString(proyecto))

def ordenamiento_ss_alf(proyectos):
    long= len(proyectos)
    for i in range(long-1):
        for j in range(i+1, long):
            if proyectos[i].titulo > proyectos[j].titulo:
                # Intercambiar
                proyectos[i], proyectos[j] = proyectos[j], proyectos[i]

def ordenamiento_ss_num(proyectos):
    long= len(proyectos)
    for i in range(long-1):
        for j in range(i+1, long):
            if proyectos[i].numero > proyectos[j].numero:
                # Intercambiar
                proyectos[i], proyectos[j] = proyectos[j], proyectos[i]

def binary_search_numeros(lista, filtro):
	# busqueda binaria... asume arreglo ordenado...
	izq, der = 0, len(lista) - 1
	while izq <= der:
		mid = (izq + der) // 2
		if filtro == lista[mid].numero:
			return mid
		elif filtro < lista[mid].numero:
			der = mid - 1
		else:
			izq = mid + 1
	return -1

def actualizar(proyecto, nuevas_lineas):
    proyecto.dia = random.randint(1, 30)
    proyecto.mes = random.randint(1, 12)
    proyecto.año = random.randint(0, 22)
    proyecto.lineas = nuevas_lineas

def contar_lineas(proyectos):
    contador = [0]*11
    for proyecto in proyectos:
        contador[proyecto.lenguaje] += proyecto.lineas
    return contador

def mostrar_contador(contador):
    print(f"""
    Python:     {contador[0]} lineas
    Java:       {contador[1]} lineas
    C++:        {contador[2]} lineas
    Javascript: {contador[3]} lineas
    Shell:      {contador[4]} lineas
    HTML:       {contador[5]} lineas
    Ruby:       {contador[6]} lineas
    Swift:      {contador[7]} lineas
    C#:         {contador[8]} lineas
    VB:         {contador[9]} lineas
    Go:         {contador[10]} lineas
    """)

def filtrar_lenguaje(proyectos, filtro):
    ordenamiento_ss_num(proyectos)
    for proyecto in proyectos:
        if proyecto.lenguaje == filtro:
            print(toString(proyecto))

