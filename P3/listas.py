#ejemplo 1 Crear una lista de numeros e imprimir el contenido
import os
os.system("cls")

numeros=[100,34,23,12]
print(numeros)

#2da forma 

for i in numeros:
    print(i)

#3ra forma
for i in range(0,len(numeros)):
    print(numeros[1])

#ejemplo 2 Crear una lista de palabras y posteriormente buscar la cioncidencia de una palabra 
import os
os.system("cls")

palabras=["gato","cel","table","cargador"]
print(palabras)
palabra=input("ingrese una palabra a buscar:")
#1ra forma
if palabra in palabras:
    print("se encontro la palabra")
else:
    print("no se encotro la palabra")

#2da forma
encontro = False
for i in palabras:
    if i ==palabras:
        print("se encontro la palabra")
        encuentro = True
if encontro:
    print("se encontro la palabra")

#3ra forma
encontro = False
for i in range(0,len(numeros)):
    if palabras[i] ==palabra:


        encuentro = True
if encontro:
    print("no encontro la palabra")

#ejemplo 3 añadir elementos a ala lista
import os 
os.system("cls")
opc="si"
while opc=="si":
    numeros.append=(float(input("Dame un numero entero o decimal:")))
poc=input("¿Deseas solicitar otro numero (si/no)").lower()

print(numeros)


#ejemplo 4 crear una lista multimensional (matriz) que almacene el nombre y telefono de 4 personas

agenda =[
    ["Ivan", "123456789"],
    ["Alonso", "978837890"],
    ["Axel", "456789123"],
    ["Emiliano", "747898798"]   
]

print(agenda)

for r in range(0,3):
    for c in range(0,2):
        valores+=f"{agenda[r][r]},"
        valores+=f"\n"
print(valores)
1

       
    
        