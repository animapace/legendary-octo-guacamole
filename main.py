print("1. Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído")

x=int(input("Ingrese un numero entero: "))

while x>1 :

 x=x-1

 print(x)

else: 

 print("Fin")



print("2. Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.")

num = int(input("Ingrese un número entero: "))

for i in range(1, num+1):

  if i % 2 == 0:  

    print(i)



print(" Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.")

num=int(input("Ingrese un numero: "))

for i in range(1,num+1):

 if (num%i==0):

  print(i)



print("4. Leer dos números y mostrar todos los enteros comprendidos entre ellos.")

Num1=int(input("Ingrese el primer numero: "))

Num2=int(input("Ingrese el segundo numero: "))

for i in range(Num1,Num2+1):

 print(i)



print("5. Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.")

num1=int(input("Ingrese el primer numero: "))

num2=int(input("Ingrese el segundo numero: "))

for i in range(num1,num2+1):

 print(i)



print("6. Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.")

num=int(input("Ingrese un numero de 3 digitos: "))

Digito1=num//100

Digito2=(num//10)%10

Digito3=num%10

print(f"Los numeros comprendidos entre 1 y {Digito1} son: ")

for i in range(1,Digito1+1):

  print(i)

print(f"Los numeros comprendidos entre 1 y {Digito2} son: ")

for i in range(1,Digito2+1):

  print(i)

print(f"Los numeros comprendidos entre 1 y {Digito3} son: ")

for i in range(1,Digito3+1):

  print(i)



print("7. Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.")

for i in range(1,100+1):

 print(i)



print("8. Mostrar en pantalla todos los pares comprendidos entre 20 y 200.")

num=20

while num<=200:

 print(num)

 num=num+2



print("9. Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.")

num = 25

while num <= 205:

    if num % 10 == 6:

      print(num)

    num += 1





print("10. Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.")

num=int(input("Ingrese un numero entero: "))

suma=0

for i in range(1,num+1):

 suma=suma+i

print("La suma de los numeros enteros comprendidos entre 1 y ",num," es: ",suma)



print("11. Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.")

num=int(input("Ingrese un numero de dos digitos: "))

digito1=num//10

digito2=num%10

for i in range(digito1,digito2+1):

 print(i)



print("12. Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.")

num=input("Ingrese un numero de 3 digitos: ")

if(num[0]=="1" or num[1]=="1" or num[2]=="1"):

 print("El numero tiene el digito 1")

else:

 print("El numero no tiene el digito 1")



print("13. Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.")

num = int(input("Ingrese un número entero: "))

for i in range(1, num+1):

  if i % 5 == 0:

    print(i)



print("14. Mostrar en pantalla los primeros 20 múltiplos de 3.")

for i in range(1,21):

 print(i*3)

  

print("15. Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.")

num=0

for i in range(1,21):

 num=num+3

 print(num)



print("16. Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.")

num1=int(input("Ingrese el primer numero: "))

num2=int(input("Ingrese el segundo numero: "))

sum1=0

sum2=1

for i in range(1,num1+1):

  sum1=sum1+(i*2)

sum1=sum1/sum2

for i in range(1,num2+1):

  sum2=sum2+(i*5)

sum2=sum2/num2

if sum1>sum2:

  print("El promedio de los primeros ",num1," multiplos de 2 es mayor que el promedio de los primeros ",num2," multiplos de 5")



print("17. Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.")

def promedio_numeros_terminados_en_5():

 numeros = []

 while True:

   numero = int(input("Ingresa un número (0 para terminar): "))

   if numero == 0:

     break

   if numero % 10 == 5:

     numeros.append(numero)

 if numeros:

   promedio = sum(numeros) / len(numeros)

   print(f"El promedio de los números terminados en 5 es: {promedio}")

 else:

   print("No se ingresaron números terminados en 5.")



promedio_numeros_terminados_en_5()



print("18. Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.")

def generar_numeros():

 for i in range(10,0,-1):

  print(11-i)

generar_numeros()



print("19. Leer un número entero y mostrar en pantalla su tabla de multiplicar.")

def tabla_multiplicar(numero):

  for i in range(1, 11):

    resultado = numero * i

    print(f"{numero} x {i} = {resultado}")

numero = int(input("Ingrese un número entero: "))

tabla_multiplicar(numero)



print("20. Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.")

num = int(input("Ingrese un número entero: "))

suma = 0

for i in range(1, num+1):

  factorial = 1

  for j in range(1, i+1):

    factorial *= j

  suma += factorial

print("La sumatoria de las factoriales de los números comprendidos entre 1 y", num, "es:", suma)
