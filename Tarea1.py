#Tarea 1


def menu():
    print ("Listado de libros a utilizar")
    print ("\t1 - El_Arbol_de_la_Colina")
    print ("\t2 - El_Caos_Raptante")
    print ("\t3 - En_El_Mar_Remoto")
    print ("\t4 - Lazarillo_De_Tormes")
    print ("\t5 - Para_Leer_Al_Atardecer")
    print ("\t6 - Una_corta_historia_del_eBook")
    print ("\t7 - Salir")

def menu2():
    print ("¿Qué desea hacer con el libro seleccionado?")
    print ("\t1 - Conocer su estadistica")
    print ("\t2 - Buscar una palabra y ver cuantas veces se repite")
    print ("\t3 - Remplazar una palabra en el texto")
    print ("\t4 - Salir")

Numero_Lineas = 0
Repeticiones = 0
Espacios = 0
Numero_Caracteres_Con_Espacio=0
menu()
opcionMenu = input("Seleccione un número: ")
print ("\n")

if opcionMenu=="1":
    a  = open("El_Arbol_de_la_Colina.txt","rt",encoding="utf-8")
    menu2()
    opciónMenu2 = input("Escriba el numero: ")
    print ("\n")
    if opciónMenu2=="1":
        datos = a.read()
        palabras = datos.split()
        for x in datos:
            if "\n" in x:
                Numero_Lineas += 1
            Espacios += x.count(" ")
            Numero_Caracteres_Con_Espacio += len(x)
            Numero_Caracteres_Sin_Espacio = Numero_Caracteres_Con_Espacio - Espacios
        print("La estadística del libro seleccionado es la siguiente")
        print("El numero de lineas es: ",Numero_Lineas)
        print("El numero total de palabras es: ", len(palabras))
        print("El numero de palabras no repetidas es: ", )
        print("El numero de caracteres con espacios es: ", Numero_Caracteres_Con_Espacio)
        print("El numero de caracteres sin espacios es: ", Numero_Caracteres_Sin_Espacio)

    elif opciónMenu2=="2":
        Palabra_Buscada = input("Ingrese la palabra a buscar: ")
        datos = a.read()
        palabras = datos.split()
        for x in datos:
            y = x.lower() 
            Palabra_Buscada = Palabra_Buscada.lower()
            Repeticiones += y.count(Palabra_Buscada)
        print("La palabra", Palabra_Buscada, "se repite", Repeticiones, "veces")

    elif  opciónMenu2=="3":
        Palabra = input("Ingrese la palabra que desea cambiar: ")
    print ("\n")


if opcionMenu=="2":
    archivo = open("El_Caos_Reptante.txt", "rt", encoding="utf-8")
    menu2()
    opciónMenu2 = input("Escriba el numero: ")
    print ("\n")
    datos = archivo.read()
    palabras = datos.split()
    for x in datos:
        if "\n" in x:
            Numero_Lineas += 1
    print("El numero de lineas es: ",Numero_Lineas)
    print('Número de palabras en el archivo de texto :', len(palabras))
    print ("\n")


if opcionMenu=="3":
    archivo = open("En_El_Mar_Remoto.txt", "rt")
    menu2()
    opciónMenu2 = input("Escriba el numero: ")
    datos = archivo.read()
    palabras = datos.split()
    Numero_Lineas=0
    for x in datos:
        if "\n" in x:
            Numero_Lineas += 1
    print("El numero de lineas es: ",Numero_Lineas)
    print('Número de palabras en el archivo de texto :', len(palabras))
print ("\n")


