1. Realizar la debida instalación de Python, el intérprete o IDE de acuerdo a la Guia de Aprendizaje 1.</p>
Hecho

2. Determina luego de -> (sin programar) el resultado que aparecerá por pantalla a partir de las siguientes variables:
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
Listado de errores:

 * Se está intentando hacer una división entre variables de tipo string. La solución sería convertir a variables numéricas antes de realizar la división.
 * La palabra clave print inició en mayúsculas, cuando debería estar en minúsculas.
 * la frase "La nota media es " debería estar entre comillas simples o dobles.

Código corregido:
``` python
numero_1 = int("9")
numero_2 = int("3")
numero_3 = int("6")

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)
La nota media es 6.0
```


