1. Consultar y profundizar sobre el ciclo while().
 Características principales.
 Como se usa.


2. Consultar y profundizar sobre los argumentos en funciones *args y **kwargs
 Características principales.
 Cuando y como se usa

El principal uso de *args y **kwargs es en la definición de funciones. Ambos permiten pasar un número variable de argumentos a una función, por lo que si quieres definir una función cuyo número de parámetros de entrada puede ser variable, considera el uso de *args o **kwargs como una opción. De hecho, el nombre de args viene de argumentos, que es como se denominan en programación a los parámetros de entrada de una función.

``` python
def test_var_args(f_arg, *argv):
    print("primer argumento normal:", f_arg)
    for arg in argv:
        print("argumentos de *argv:", arg)

test_var_args('python', 'foo', 'bar')

primer argumento normal: python
argumentos de *argv: foo
argumentos de *argv: bar

```

Uso de **kwargs
**kwargs permite pasar argumentos de longitud variable asociados con un nombre o key a una función. Deberías usar **kwargs si quieres manejar argumentos con nombre como entrada a una función. Aquí tienes un ejemplo de su uso.
``` python
def saludame(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

>>> saludame(nombre="Covadonga")
nombre = Covadonga
```

3. Consultar y profundizar sobre la función input()
 Características principales
 Como se usa
 Como hacer cast de una cadena de texto a un entero


4. Determina luego de -> (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:
``` python
a = 10
b = -5
c = "Hola "
d = [1, 2, 3]

 print(a * 5)
  50
 print(a - b) 
  15
 
 print(c + "Mundo")
  Hola Mundo 
 
 print(c * 2) 
  Hola Hola
 
 print(d + d) 
    [1,2,3,1,2,3]
 
 print((c + "mundo")* 5) 
    Hola mundoHola mundoHola mundo Hola mundo Hola mundo 
```
3.  Realice mediante un código o script lo siguiente:
 - cree 3 variables con los nombres nota_1, nota_2 y nota_3
 - asígnele valores enteros entre 0 y 5

 - cree una tercer variable nota_final que calcule el promedio de las 3 variables
  ```python 
     nota_1=0
     nota_2=5
     nota_3=1.1
     nota_final = (nota_1 + nota_2 + nota_3) / 3     
   ```
 - Imprima en pantalla una cadena de texto que le indique “Su nota final es: "" y el resultado de nota_final
   ``` python
    nota_final = (nota_1 + nota_2 + nota_3) / 3     
    print("Su nota final es: "+str(nota_final)) 
    "Su nota final es: 2.033333333333333"
   ```
4. Cree una lista vacía, e inserte los valores de las notas 1, 2, 3, e imprima en pantalla la lista. Lista = []
``` python
Lista=[]
Lista.append(nota_1)
Lista.append(nota_2)
Lista.append(nota_3)
print(Lista)
```

5. Realice mediante un código o script lo siguiente: 
cree 3 variables con nombres de productos.
asigne a cada una un valor numérico.
en una nueva variable llamada total, sume el valor de los 3 productos.
en otra variable, calcule el valor de iva de los 3 productos 19%.
imprima en pantalla el valor total y el valor de iva.

``` python
arroz = 12500
papa = 23000
harina = 5300

total = arroz+papa+harina
iva = total*0.19
print ('Debe pagar un total de : {2}, consistente en una suma de productos {0} y un iva de {1}'.format(total,iva,total+iva))
> Debe pagar un total de : 48552.0, consistente en una suma de productos 40800 y un iva de 7752.0
```
6. El siguiente código NO funciona, identifique los errores y corrija el script. 
``` python
numero_1 = “9”
numero_2 = “3”
numero_3 = “6”
media = (numero_1 + numero_2 + numero_3) / 3 
Print(La nota media es, media)
```
8. Generar una función que reciba números como argumentos.
 Si el primer número es mayor que el segundo, entonces que indique cual
es el número mayor
 si el segundo número es mayor que el primero, entonces que indique
cual es el número menor
 o si son iguales, que indique que ambos números son iguales.



9.Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
Por ejemplo:
pares, impares = separar([6,5,2,1,7]) print(pares) # valdría [2, 6] print(impares) # valdría [1, 5, 7]
Nota: Para ordenar una lista automáticamente puedes usar el método .sort().

``` python
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
```
