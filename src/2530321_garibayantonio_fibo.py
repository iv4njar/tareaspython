# Series Fibonacci en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

"""

    ¿Qué es la serie de Fibonacci?
    La serie de Fibonacci es una sucesión donde cada número resulta de sumar los dos anteriores, comenzando típicamente con 0 y 1. 

    ¿Qué significa “calcular la serie hasta un número de términos n”?
    Calcular la serie hasta un número de términos n significa generar los primeros n valores siguiendo esa regla.

    ¿Qué cubrirá tu programa?
    Mi programa leerá el valor de n, realizará una validación básica para asegurar que sea un entero válido y luego 
    generará la serie completa hasta esa cantidad de términos.

"""

print("----------------FIBONACCI-----------------")

"""
Problem: Fibonacci series generator  

Description: Program that reads an integer n and prints the first n terms of the Fibonacci series starting at 0 and 1.  


Inputs:  
- n (int; number of terms to generate)  

Outputs:  
- "Fibonacci series:" followed by the n terms separated by spaces or commas  

Validations:  
- n must be an integer  
- n must be >= 1  
- (Optional) n must be <= 50  

Test cases:  
1) Normal:  
Number of terms: 20
--------------------
Fibonacci series: 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181

2) Border:
Number of terms: 10000000000000
--------------------
Error: invalid input

3) Error:
Number of terms: 0
--------------------
Error: invalid input

"""

user_input = input("Number of terms: ")


try:
    n = int(user_input)
except ValueError:
    print("Error: invalid input")
    exit()


if n < 1 or n > 50:
    print("Error: invalid input")
    exit()

print("Fibonacci series:", end=" ")

if n == 1:
    print(0)
else:
    a, b = 0, 1
    print(a, b, end=" ")
    for _ in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a, b = b, c

print("------------END------------------")

# Conclusion

"""

    El uso de un bucle facilitó generar cada nuevo término a partir de los anteriores sin repetir código manualmente. 
    Es importante manejar bien los casos n = 1 y n = 2 porque la serie tiene inicios especiales que no 
    siguen exactamente el patrón general del bucle. 
    Además, esta lógica puede reutilizarse en programas que requieran secuencias numéricas, 
    cálculos progresivos o análisis de crecimiento basado en pasos recurrentes.

"""

# Referencias

"""
    https://www.geeksforgeeks.org/python/python-program-to-print-the-fibonacci-sequence/

    https://www.youtube.com/watch?v=7Sv4NmvdHcw

    https://www.youtube.com/watch?v=sNjoLvV9nFI

"""