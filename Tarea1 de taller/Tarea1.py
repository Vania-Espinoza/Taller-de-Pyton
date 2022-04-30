#Tarea 1    Franco Paredes - Vania Espinoza

import sys
import fileinput
from typing import List

#Menu de libros
def menu():
    print ("Listado de libros a utilizar")
    print ("\t1 - El_Arbol_de_la_Colina")
    print ("\t2 - El_Caos_Raptante")
    print ("\t3 - En_El_Mar_Remoto")
    print ("\t4 - Lazarillo_De_Tormes")
    print ("\t5 - Para_Leer_Al_Atardecer")
    print ("\t6 - Una_corta_historia_del_eBook")
    print ("\t7 - Salir")
    return input("Seleccione un número: ")
#Menu de opciones
def menu2():
    print ("¿Qué desea hacer con el libro seleccionado?")
    print ("\t1 - Conocer su estadistica")
    print ("\t2 - Buscar una palabra y ver cuantas veces se repite")
    print ("\t3 - Remplazar una palabra en el texto")
    print ("\t4 - Salir")
    return input("Escriba el numero: ")
def start(name_text):
    #Declaracion de listas
    Lista_Palabras = list()
    Lista_Filas = list()
    #Declaracion de variables de conteo
    Numero_Lineas = 0
    Repeticiones = 0
    Espacios = 0
    Numero_Caracteres_Con_Espacio=0
    Numero_Palabras=0
    a  = open(name_text,"r+",encoding="utf-8")
    opciónMenu2 = menu2()    
    print ("\n")
    if opciónMenu2=="1":
        for x in a:
            if "\n" in x:
                Numero_Lineas += 1
            Espacios += x.count(" ")
            Numero_Palabras += len(x.split())
            Lista_Palabras += x.split()
            Numero_Caracteres_Con_Espacio += len(x)
        for aux in range(len(Lista_Palabras)):
            Palabra_comparar=Lista_Palabras[aux]
            var = Lista_Palabras.count(Palabra_comparar)
            if var > 1:
                Repeticiones += 1
        Numero_Caracteres_Con_Espacio -= Numero_Lineas
        Numero_Caracteres_Sin_Espacio = Numero_Caracteres_Con_Espacio - Espacios
        Numero_Palabras_No_Repetidas = Numero_Palabras - Repeticiones
        print("La estadística del libro seleccionado es la siguiente")
        print("El numero de lineas es: ",Numero_Lineas)
        print("El numero total de palabras es: ", Numero_Palabras)
        print("El numero de palabras no repetidas es: ", Numero_Palabras_No_Repetidas)
        print("El numero de caracteres con espacios es: ", Numero_Caracteres_Con_Espacio)
        print("El numero de caracteres sin espacios es: ", Numero_Caracteres_Sin_Espacio)

    elif opciónMenu2=="2":
        Palabra_Buscada = input("Ingrese la palabra a buscar: ")
        for x in a:
            y = x.lower() 
            Palabra_Buscada = Palabra_Buscada.lower()
            Repeticiones += y.count(Palabra_Buscada)
        print("La palabra", Palabra_Buscada, "se repite", Repeticiones, "veces")

    elif  opciónMenu2=="3":
        Palabra1 = input("Ingrese la palabra que desea cambiar: ")
        Palabra2 = input("Ingrese la palabra que irá en el texto: ")              
        for x in a:            
            Lista_Palabras += x.split()
        var = Lista_Palabras.count(Palabra1)        
        if var==0:
            print("No se escuentra la palabra que desea cambiar")
        elif var >= 1:
            for x in fileinput.input(files = name_text,encoding="utf-8"):
                x = x.replace(Palabra1,Palabra2)
                sys.stdout.write(x)
    print("\n")

opcionMenu = menu()

print ("\n")

if opcionMenu=="1":
    start("El_Arbol_De_La_Colina.txt")
    
elif opcionMenu=="2":
    start("El_Caos_Reptante.txt")

elif opcionMenu=="3":
    start("En_El_Mar_Remoto.txt")

elif opcionMenu=="4":
    start("Lazarillo_de_Tormes.txt")
    
elif opcionMenu=="5":
    start("Para_Leer_Al_Atardecer.txt")

elif opcionMenu=="6":
    start("Una_corta_historia_del_eBook.txt")