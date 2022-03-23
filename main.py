# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def check_numbers():
    numeros = [1, 3, 6, 9]
    i = 0
    while i not in numeros:
        print('Ingrese un número')
        i = input()
        print('El número ingresado es: ' + i)
        try:
            i = int(i)
            if (i in numeros):
                print("Wow si está")
                return
            else:
                print("no, no está " + str(type(i)))
        except:
            print("No se pudo convertir lo ingresado")

def separar(lista):
    lista.sort()
    new_lista_par = []
    new_lista_impar = []
    for num in lista:
        if num % 2 == 0:
            new_lista_par.append(num)
        else:
            new_lista_impar.append(num)
    print(new_lista_par)
    print(new_lista_impar)
    return new_lista_par, new_lista_impar


def args_number_comparative (*argv):
    if len(argv)!=2:
        print("La cantidad de números no es exactamente 2")
    elif (type(argv[0])==int and type(argv[1])==int):
        if (argv[0]>argv[1]):
            print("El número {0} es mayor a {1}".format(argv[0],argv[1]))
        elif(argv[0]<argv[1]):
            print("El número {1} es mayor a {0}".format(argv[0],argv[1]))
        else:
            print("Los números a comparar son iguales: {0}".format(argv[0]))
    else:
        print("Los argumentos ingresados no son números.")

if __name__ == '__main__':
    print_hi('PyCharm')
    #check_numbers()
    #pares, impares = separar([6, 5, 2, 1, 7])

    args_number_comparative()
    args_number_comparative("z","b")
    args_number_comparative(1, 2)
    args_number_comparative(2, 2)
    args_number_comparative(32,2)
    # valdría [2, 6] print(impares) # valdría [1, 5, 7]

"""
Punto 1:
Uso de *args
El principal uso de *args y **kwargs es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción. De hecho, el nombre de args viene de argumentos, que es como se denominan en programación a los parámetros de entrada de una función.

def test_var_args(f_arg, *argv):
    print("primer argumento normal:", f_arg)
    for arg in argv:
        print("argumentos de *argv:", arg)

test_var_args('python', 'foo', 'bar')

primer argumento normal: python
argumentos de *argv: foo
argumentos de *argv: bar


Uso de **kwargs
**kwargs permite pasar argumentos de longitud variable asociados con un nombre o key a una función. Deberías usar **kwargs si quieres manejar argumentos con nombre como entrada a una función. Aquí tienes un ejemplo de su uso.

def saludame(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> saludame(nombre="Covadonga")
nombre = Covadonga

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    
    # Primero con *args
>>> args = ("dos", 3, 5)
>>> test_args_kwargs(*args)
arg1: dos
arg2: 3
arg3: 5

# Ahora con **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "dos", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: dos
arg3: 3

funcion(fargs, *args, **kwargs)

Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
numeros = [1, 3, 6, 9]
"""
