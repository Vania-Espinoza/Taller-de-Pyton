#Tarea 1

f = open("El_Caos_Reptante.txt","rt",encoding="utf-8")

Numero_Lineas=0
Numero_Palabras_Total=0
Numero_Palabras_No_Repetidas=0
Numero_Caracteres_Con_Espacio=0
Numero_Caracteres_Sin_Espacio=0

for x in f:
    print(x)
    if "\n" in x:
        Numero_Lineas += 1
    

print("el numero de lineas es: ",Numero_Lineas)



