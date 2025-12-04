# Manejo de Bucles en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

"""

    ¿Qué es un bucle for y para qué se usa típicamente?
    Un bucle for recorre un rango o colección y se usa típicamente cuando 
    sabemos de antemano cuántas iteraciones necesitamos realizar.  

    ¿Qué es un bucle while y cuándo es más natural usarlo?
    Un bucle while repite instrucciones mientras se cumpla una condición, 
    y es más natural cuando no sabemos cuántas veces se repetirá el proceso.  

    ¿Qué son un contador y un acumulador?
    Un contador lleva la cantidad de iteraciones o elementos procesados, 
    mientras que un acumulador suma o combina valores a lo largo del ciclo. 

    ¿Por qué es importante definir bien la condición de salida y evitar ciclos infinitos? 
    Es crucial definir correctamente la condición de salida para evitar ciclos 
    infinitos que bloqueen el programa o consuman recursos sin control.  

    ¿Qué cubrirá tu documento?
    El documento cubrirá: descripción de cada problema, diseño de entradas/salidas, 
    validaciones necesarias y el uso adecuado de for/while en recorridos, menús 
    y lecturas repetidas según la situación. 

"""
# 1st problem: Sum of range with for

"""
    Description: 
    Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n).
    Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.
        
Inputs:
- n (int; límite superior del rango).


Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>


Validations:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 
Enter n: 10
----------------------------------------
Sum 1..n: 55
Even sum 1..n: 30


2) Border:
Enter n: 1
----------------------------------------
Sum 1..n: 1
Even sum 1..n: 0


3) Error: 
Enter n: awd
----------------------------------------
Error: invalid input


"""
n_input = input("Enter n: ")

try:
    n = int(n_input)
    if n < 1:
        print("Error: invalid input")
    else:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum = total_sum + i

            if i % 2 == 0:
                even_sum = even_sum + i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
except ValueError:
    print("Error: invalid input")

print("---------------------------------------------")

# 2nd problem: Multiplication table with for


"""
    Description: 
            Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
            5 x 1 = 5
            5 x 2 = 10
            5 x 3 = 15
            5 x 4 = 20
        
Inputs:
- base (int)
- m (int; límite de la tabla)


Outputs:
- Línea por cada multiplicación:
- "5 x 1 = 5"
- "5 x 2 = 10"
- etc.


Validations:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".

Test cases:
1) Normal: 
Enter base: 10
Enter limit m: 8
----------------------------------------
10 x 1 = 10
10 x 2 = 20
10 x 3 = 30
10 x 4 = 40
10 x 5 = 50
10 x 6 = 60
10 x 7 = 70
10 x 8 = 80


2) Border:
Enter base: 1
Enter limit m: 1
----------------------------------------
1 x 1 = 1


3) Error: 
Enter base: 0
Enter limit m:
----------------------------------------
Error: invalid input



"""


base_input = input("Enter base: ")
m_input = input("Enter limit m: ")

try:
    base = int(base_input)
    m = int(m_input)
    if m < 1:
        print("Error: invalid input")
  
    for i in range(1, m + 1):
        result = base * i
        print(f"{base} x {i} = {result}")
except:
    print("Error: invalid input")

print("---------------------------------------------------")

# 3th problem: Average of numbers with while and sentinel

"""
    Description: 
    Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
    Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
    Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.
        
Inputs:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Outputs:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Validations:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.

Test cases:
1) Normal: 
Enter number (-7 to stop): 2
Enter number (-7 to stop): 32
Enter number (-7 to stop): 12.3
Enter number (-7 to stop): 23.34
Enter number (-7 to stop): 23
Enter number (-7 to stop): 13
Enter number (-7 to stop): 32
Enter number (-7 to stop): -7
----------------------------------------
Count: 7
Average: 19.662857142857142

2) Border:
Enter number (-7 to stop): 0
Enter number (-7 to stop): -7
----------------------------------------
Count: 1
Average: 0.0


3) Error: 
Enter number (-7 to stop): awd
----------------------------------------
Error: invalid input
Enter number (-7 to stop): -7
----------------------------------------
Error: no data


"""

SENTINEL = -7
count = 0
total = 0.0

while True:
    value_input = input("Enter number (-7 to stop): ")

    try:
        number = float(value_input)
    except:
        print("Error: invalid input")
        continue 

    if number == SENTINEL:
        break  
    total += number
    count += 1

if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)

print("------------------------------------------------")

# 4th problem: Password attempts with while

"""
    Description: 
    Implementa un sistema sencillo de intento de contraseña. 
    Define en el código una contraseña correcta (por ejemplo, "admin123"). 
    El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
    Si acierta dentro del límite, mostrar un mensaje de éxito. 
    Si agota los intentos, mostrar un mensaje de bloqueo.
        
Inputs:
- user_password (string; se lee en cada intento).

Outputs:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Validations:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.

Test cases:
1) Normal: 
Enter password: ivan321
Enter password: 321ivan
Enter password: ivan123
----------------------------------------
Login success

2) Border:
Enter password:
Enter password:
Enter password:
Enter password:
----------------------------------------
Account locked


3) Error: 
Enter password: 1234
Enter password: 4231
Enter password: ivan1324
Enter password: pelon123
----------------------------------------
Account locked


"""
#Código: 
CORRECT_PASSWORD = "ivan123"
MAX_ATTEMPTS = 4

attempts = 0
success = False

while attempts < MAX_ATTEMPTS:
    password = input("Enter password: ")

    if password == CORRECT_PASSWORD:
        print("Login success")
        success = True
        break
    else:
        attempts += 1

if not success:
    print("Account locked")

print("-------------------------------------------------")

# 5th problem: Simple menu with while

"""
    Description: 
    Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. 
    Ejemplo de menú:
        1) Show greeting
        2) Show current counter value
        3) Increment counter
        0) Exit
        El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar 
        el menú hasta que se elija 0.
        
Inputs:
- option (string o int; elección del usuario).

Outputs:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Validations:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.

Test cases:
1) Normal: 
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 1
----------------------------------------
¡Hello!
----------------------------------------
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 3
----------------------------------------
Counter incremented 1
----------------------------------------
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 2
----------------------------------------
Counter: 1
----------------------------------------
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 0
----------------------------------------
¡Goodbye!


2) Border:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: show greting
----------------------------------------
Error: invalid option


3) Error: 
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
Choose an option: 6
----------------------------------------
Error: invalid option


"""
counter = 0

while True:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_input = input("Choose an option: ")

    try:
        option = int(option_input)
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("¡Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented 1") 
    elif option == 0:
        print("¡Goodbye!")
        break
    else:
        print("Error: invalid option")

print("---------------------------------------------------")

# 6th problem: Pattern printing with nested loops

"""
    Description:
        Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo.
        Por ejemplo, para n = 4:
        *
        **
        ***
        ****
        Además, imprime un segundo patrón invertido (opcional si lo deseas extender, pero documenta tu decisión).
        
Inputs:
- n (int; número de filas del patrón).

Outputs:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"
- (Opcional) Patrón invertido si se implementa.


Validations:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".



Test cases:
1) Normal: 
Enter n: 7
----------------------------------------
*
**
***
****
*****
******
*******


2) Border:
Enter n: 1
----------------------------------------
*


3) Error: 
Enter n: 0
----------------------------------------
Error: invalid input


"""

n_input = input("Enter n: ")

try:
    n = int(n_input)
except:
    print("Error: invalid input")
    exit()

if n < 1:
    print("Error: invalid input")
    exit()

for i in range(1, n + 1):
    line = ""
    for j in range(i):
        line += "*"
    print(line)


# Conclusion

"""

    El for resulta práctico cuando conozco el número de repeticiones, mientras que el while
    es más flexible para procesos que dependen de una condición cambiante.  
    Los contadores y acumuladores me ayudaron a llevar control de iteraciones y a sumar datos
    sin necesidad de variables externas complicadas.  
    El while presenta riesgos como los ciclos infinitos si la condición nunca cambia o se
    actualiza incorrectamente.  
    Los menús interactivos y los intentos de contraseña son buenos ejemplos de while porque
    dependen de la elección del usuario o de validar una condición hasta que sea correcta.  
    Con los bucles anidados aprendí a generar patrones y a recorrer estructuras en múltiples
    dimensiones de forma ordenada. 

"""

# Referencias

"""
    https://ellibrodepython.com/for-python

    https://tutorial.recursospython.com/bucles/#google_vignette
    
    https://www.youtube.com/watch?v=IyI2ZuOq_xQ

    https://www.youtube.com/watch?v=moUHTWl7QCQ

    https://www.w3schools.com/python/python_for_loops.asp

"""