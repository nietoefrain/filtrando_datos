#nombres
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = ['Messi', 'Pele', 'Juanes']

# funcion magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = 'El gran ' + magos[i]

# funcion imprimir lista (nombres)
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# lista completa
todos = magos + cientificos + otros
print("Todos los nombres:")
imprimir_nombres(todos)

# modificar magos
hacer_grandioso(magos)
print("\nMagos grandiosos:")
imprimir_nombres(magos)

# científicos
print("\nCientíficos:")
imprimir_nombres(cientificos)

# otros
print("\nOtros:")
imprimir_nombres(otros)
