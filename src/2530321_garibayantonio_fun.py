# Manejo de Funciones en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

"""
    ¿Qué es una función en Python y para qué sirve?
    Una función en Python es un bloque de código reutilizable que ejecuta una tarea específica.

    ¿Qué diferencia hay entre parámetros (definition) y argumentos (call)?
    Los parámetros se definen en la función y los argumentos son los valores reales que se envían al llamarla.

    ¿Por qué es útil separar la lógica en funciones reutilizables?
    Separar la lógica en funciones permite organizar mejor el programa y evitar repetir código.

    ¿Qué es un valor de retorno y por qué es mejor devolver resultados en lugar de solo imprimirlos?
    Un valor de retorno es el resultado que la función entrega; es mejor devolver datos que solo imprimirlos,
    porque así pueden reutilizarse en otros cálculos o pruebas.

    ¿Qué cubrirá tu documento?
    El documento cubrirá: descripción de cada problema, diseño de funciones, entradas, salidas,
    validaciones necesarias y pruebas básicas para verificar su funcionamiento.

"""

print("--------------------------------------------------------------")

# 1st problem: Rectangle area and perimeter (basic functions)

"""
    Description: 
        Define dos funciones:
        - calculate_area(width, height): regresa el área de un rectángulo.
        - calculate_perimeter(width, height): regresa el perímetro.
        El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.
        
Inputs:
- width (float)
- height (float)

Outputs:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validations:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.

Test cases:
1) Normal: 
Put width:10
Put height:20
--------------------
area: 200.0
perimeter: 60.0


2) Border:
Put width:0
Put height:0
--------------------
0 cant be a data


3) Error: 
Put width:
--------------------
Invalid input


"""


def calculate_area (width, height):
    return width* height
def calculate_perimeter (width, height):
    return (width+width+height+height)

width = 0
height = 0

try:
    width= float(input("Put width:"))
    height= float(input("Put height:"))
    if width>0 and height >0:
        try:
            area = calculate_area(width, height)
            perimeter = calculate_perimeter(width, height)
            print(f"area: {area}")
            print(f"perimeter: {perimeter}")
        except:
            print("Invalid input")
    else:
        print("0 cant be a data")
except:
    print("Invalid input")

print("--------------------------------------------------------------")

# 2nd Problem: Grade classifier (function with return string)

"""
    Description: 
        Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
        - "A" si score >= 90
        - "B" si 80 <= score < 90
        - "C" si 70 <= score < 80
        - "D" si 60 <= score < 70
        - "F" si score < 60
        El código principal debe llamar la función y mostrar el resultado.

        
Inputs:
- score (float o int)


Outputs:
- "Score:" <score>
- "Category:" <grade_letter>


Validations:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.


Test cases:
1) Normal: 
Enter score (0-100): 100
--------------------
Score: 100.0
Category: A


2) Border:
Enter score (0-100): 0
--------------------
Score: 0.0
Category: F


3) Error: 
Enter score (0-100):
--------------------
Error: invalid input


"""

def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter score (0-100): "))

    if 0 <= score <= 100:
        grade = classify_grade(score)
        print(f"Score: {score}")
        print(f"Category: {grade}")
    else:
        print("Error: invalid input")

except:
    print("Error: invalid input")

print("--------------------------------------------------------------")

# 3th Problem: List statistics function (min, max, average)

"""
    Description: 
        Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
        - "min": mínimo
        - "max": máximo
        - "average": promedio (float)
        El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), llamar la función y mostrar los valores.

        
Inputs:
- numbers_text (string; por ejemplo, "10,20,30")
- Internamente: numbers_list (list of float o int)

Outputs:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validations:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".

Test cases:
1) Normal:
Enter numbers separated by commas: 12,23,34
--------------------
Min: 12.0
Max: 34.0
Average: 23.0 


2) Border:
Enter numbers separated by commas: 0,0
--------------------
Min: 0.0
Max: 0.0
Average: 0.0


3) Error: 
Enter numbers separated by commas: Put width:
--------------------
Error: invalid input


"""

def summarize_numbers(numbers_list):
    stats = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return stats


numbers_text = input("Enter numbers separated by commas: ")

if numbers_text.strip() == "":
    print("Error: invalid input")
else:
    try:
        parts = numbers_text.split(",")
        numbers_list = []

        for p in parts:
            number = float(p.strip())
            numbers_list.append(number)

        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            stats = summarize_numbers(numbers_list)
            print(f"Min: {stats['min']}")
            print(f"Max: {stats['max']}")
            print(f"Average: {stats['average']}")

    except:
        print("Error: invalid input")

print("--------------------------------------------------------------")

# 4th Problem: Apply discount list (pure function)

"""
    Description: 
        Define una función apply_discount(prices_list, discount_rate) que:
        - reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
        - regrese una nueva lista con los precios ya descontados (no modificar la lista original).
        El código principal debe:
        - Crear una lista de precios.
        - Llamar a la función.
        - Mostrar la lista original y la nueva lista con descuento.

        
Inputs:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)


Outputs:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Validations:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".

Test cases:
1) Normal: 
Enter prices separated by commas: 100,10
Enter discount rate (0 to 1): 1
--------------------
Original prices: [100.0, 10.0]
Discounted prices: [0.0, 0.0]


2) Border:
Enter prices separated by commas: 0
Enter discount rate (0 to 1): 0
--------------------
Error: invalid input


3) Error: 
Enter prices separated by commas:
Enter discount rate (0 to 1):
--------------------
Error: invalid input


"""

def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    return discounted

prices_text = input("Enter prices separated by commas: ")
discount_text = input("Enter discount rate (0 to 1): ")

if prices_text.strip() == "":
    print("Error: invalid input")
else:
    try:
        discount_rate = float(discount_text)

        if discount_rate < 0 or discount_rate > 1:
            print("Error: invalid input")
        else:
            parts = prices_text.split(",")
            prices_list = []

            for p in parts:
                price = float(p.strip())
                if price <= 0:
                    raise ValueError
                prices_list.append(price)

            if len(prices_list) == 0:
                print("Error: invalid input")
            else:
                discounted = apply_discount(prices_list, discount_rate)

                print(f"Original prices: {prices_list}")
                print(f"Discounted prices: {discounted}")

    except:
        print("Error: invalid input")


print("--------------------------------------------------------------")

# 5th Problem: Greeting function with default parameters

"""
    Description: 
        Define una función greet(name, title="") que:
        - Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
        - Regrese el mensaje: "Hello, <full_name>!"
        Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.

        
Inputs:
- name (string)
- title (string opcional)

Outputs:
- "Greeting:" <greeting_message>

Validations:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().

Test cases:
1) Normal: 
Enter name: ivan pelon
Enter title (optional): Ing Pelon
--------------------
Greeting: Hello, Ing Pelon ivan pelon!


2) Border:
Enter name: 00
Enter title (optional): 00
--------------------
Greeting: Hello, 00 00!


3) Error: 
Enter name:
Enter title (optional):
--------------------
Error: invalid input


"""

def greet(name, title=""):
    name = name.strip()
    title = title.strip()

    if title == "":
        full_name = name
    else:
        full_name = f"{title} {name}"

    return f"Hello, {full_name}!"

name_input = input("Enter name: ").strip()
title_input = input("Enter title (optional): ").strip()

if name_input == "":
    print("Error: invalid input")
else:
    greeting_message = greet(name_input, title_input)

    print(f"Greeting: {greeting_message}")


print("--------------------------------------------------------------")

# 6th Problem: Factorial function (iterative or recursive)

"""
    Description: 
        Define una función factorial(n) que regrese n! (n factorial). Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. El código principal debe:
        - Leer/definir n.
        - Validar n.
        - Llamar a factorial(n).
        - Mostrar el resultado.
        
Inputs:
- n (int)

Outputs:
- "n:" <n>
- "Factorial:" <factorial_value>

Validations:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; 
si no se cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 
Enter n: 1
--------------------
n: 1
Factorial: 1


2) Border:
Enter n: 0
--------------------
n: 0
Factorial: 1


3) Error: 
Enter n:
--------------------
Error: invalid input


"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

value_text = input("Enter n: ")

try:
    n = int(value_text)

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        result = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {result}")

except:
    print("Error: invalid input")


# Conclusion

"""
    Las funciones permiten organizar el código en bloques claros y reutilizables, evitando repetir instrucciones y facilitando el mantenimiento. 
    Usar return en lugar de imprimir ofrece más flexibilidad, porque permite seguir trabajando con el valor devuelto en otras partes del programa. 
    Además, los parámetros y valores por defecto hacen que una misma función pueda adaptarse a distintos escenarios sin necesidad de duplicar código. 
    Personalmente, resultó más cómodo encapsular lógica cuando había cálculos repetidos o validaciones que debía ejecutar varias veces. 
    Finalmente, comprendí mejor la diferencia entre la lógica “principal”, que coordina el flujo general del programa, y las funciones de apoyo, 
    que se encargan de tareas específicas y bien definidas.

"""

# Referencias

"""
    https://ellibrodepython.com/funciones-en-python

    https://www.datacamp.com/es/tutorial/functions-python-tutorial

    https://www.youtube.com/watch?v=7KPTQIwcWpk

    https://www.youtube.com/watch?v=hrv1ruHxiQY

    https://docs.python.org/es/3.13/library/functions.html
"""