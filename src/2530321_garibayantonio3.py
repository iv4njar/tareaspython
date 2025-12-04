# Manejo de Tuplas, listas y diccionarios en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

"""
    ¿Qué es una lista, una tupla y un diccionario en Python y en qué se diferencian?
    Una lista en Python es una colección ordenada y mutable; una tupla es similar pero inmutable, 
    y un diccionario almacena pares clave–valor sin un orden fijo.

    ¿Qué significa que una lista sea mutable y una tupla inmutable?
    Que una lista sea mutable significa que puede modificarse (agregar, quitar o cambiar elementos);
    una tupla es inmutable, por lo que sus elementos no pueden alterarse después de creada.

    ¿Cómo se usan los diccionarios para asociar claves con valores?
    Los diccionarios permiten asociar claves únicas con valores, facilitando búsquedas rápidas y 
    organizando información por identificadores en lugar de posiciones.

    ¿Qué cubrirá tu documento?
    El documento cubrirá la descripción de cada problema, el diseño de entradas y salidas,
    las validaciones que se aplican y el uso práctico de listas, tuplas y diccionarios,
    incluyendo ejemplos como catálogos, registros de datos y cálculos estadísticos.

"""

print("--------------------------------------------------------")

# 1st problem: Shopping list basics

"""
    Description: 
        Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
        1) Crear una lista inicial de productos.
        2) Permitir agregar un nuevo producto al final.
        3) Mostrar la cantidad total de elementos en la lista.
        4) Verificar si un producto específico está en la lista (booleano is_in_list).
        
Inputs:
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).


Test cases:
1) Normal: 
    Enter initial items (separed by a comma): arroz,agua,sal
    Enter new item: tomate
    Enter item to search: arroz
    ----------------------------------------
    Items list: ['arroz', 'agua', 'sal', 'tomate']
    Total items: 4
    Found item: true

2) Border:
    Enter initial items (separed by a comma): arroz agua sal
    Enter new item: tomate
    Enter item to search: arroz
    ----------------------------------------
    Items list: ['arroz agua sal', 'tomate']
    Total items: 2
    Found item: false

3) Error: 
    Enter initial items (separed by a comma):
    Enter new item:
    Enter item to search:
    ----------------------------------------
    Error: invalid input

"""

 
initial_items_text = input("Enter initial items (separed by a comma): ").strip()
new_item = input("Enter new item: ").strip()
search_item = input("Enter item to search: ").strip()

# Validation for initial text
if initial_items_text == "":
    print("Error: invalid input")
else:
    # Convert text to list
    items_list = initial_items_text.split(",")
    
    # Del spaces
    cleaned_list = []
    for item in items_list:
        cleaned_item = item.strip()
        if cleaned_item != "":
            cleaned_list.append(cleaned_item)
    
    # Validate new and search items
    if new_item == "" or search_item == "":
        print("Error: invalid input")
    else:
        # Append new item
        cleaned_list.append(new_item)
        
        # Total items
        total_items = len(cleaned_list)
        
        # Check if search item exists
        is_in_list = search_item in cleaned_list
        
        # Output
        print("Items list:", cleaned_list)
        print("Total items:", total_items)
        print("Found item:", str(is_in_list).lower())

print("-------------------------------------------------------")

# 2nd Problem: Points and distances with tuples

"""
    Description: 
        Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
        1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
        2) Calcular la distancia euclidiana entre ambos puntos.
        3) Crear una nueva tupla midpoint con el punto medio entre ellos.
        
Inputs:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)


Validations:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.


Test cases:
1) Normal: 
    Enter x1: 5
    Enter y1: 5
    Enter x2: 5
    Enter y2: 5
    ----------------------------------------
    Point A: (5.0, 5.0)
    Point B: (5.0, 5.0)
    Distance: 0.0
    Midpoint: (5.0, 5.0)

2) Border:
    Enter x1:
    ----------------------------------------
    Error: Invalid numeric input.

3) Error: 
    Enter x1: 2
    Enter y1: 21
    Enter x2: a
    ----------------------------------------
    Error: Invalid numeric input.

"""

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: Invalid numeric input.")

print("-------------------------------------------------------")

# 3rd Problem: Product catalog with dictionary

"""
    Description: 
        Administra un pequeño catálogo de productos usando un diccionario donde:
        - clave: nombre del producto (string)
        - valor: precio unitario (float)
        El programa debe:
        1) Crear un diccionario inicial con al menos 3 productos.
        2) Leer el nombre de un producto y la cantidad a comprar.
        3) Calcular el total a pagar si el producto existe.
        4) Si el producto no existe, mostrar un mensaje de error.
        
Inputs:
- product_name (string).
- quantity (int; cantidad a comprar).

Outputs:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"


Validations:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).


Test cases:
1) Normal: 
    Enter product name (apple, chilli or orange): apple
    Enter quantity: 8
    ----------------------------------------
    Unit price: 10.0
    Quantity: 8
    Total: 80.0

2) Border:
    Enter product name (apple, chilli or orange): mango
    Enter quantity: 2
    ----------------------------------------
    Error: product not found

3) Error: 
    Enter product name (apple, chilli or orange):
    Enter quantity: 10
    ----------------------------------------
    Error: product name cannot be empty.

"""

product_prices = {"apple": 10.0, "chilli": 14.0, "orange": 25.0}

product_name = input("Enter product name (apple, chilli or orange): ").strip()
quantity_input = input("Enter quantity: ")

try:
    quantity = int(quantity_input)

    if product_name == "":
        print("Error: product name cannot be empty.")
    elif quantity <= 0:
        print("Error: quantity must be greater than 0.")
    else:
        if product_name in product_prices:
            unit_price = product_prices[product_name]
            total_price = unit_price * quantity

            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", total_price)
        else:
            print("Error: product not found")

except ValueError:
    print("Error: quantity must be a number.")



# 4th Problem: Student grades with dict and list

"""
    Description: 
        Administra las calificaciones de un grupo usando un diccionario:
        - clave: nombre del estudiante (string)
        - valor: lista de calificaciones (list of float)
        El programa debe:
        1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
        2) Leer el nombre de un estudiante.
        3) Calcular el promedio de sus calificaciones.
        4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.
        
Inputs:
- student_name (string).

Outputs:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"


Validations:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.


Test cases:
1) Normal: 
    Enter student name (ivan, antonio, pelon): pelon
    ----------------------------------------
    Grades: [100.0, 100.0, 100.0]
    Average: 100.0
    Passed: True

2) Border:
    Enter student name (ivan, antonio, pelon): chaparro
    ----------------------------------------
    Error: student not found

3) Error: 
    Enter student name (ivan, antonio, pelon):
    ----------------------------------------
    Error: no student name
    

"""

#Código:
student_grades = {"ivan": [90.0, 95.0, 90.0], "antonio": [100.0, 50.0, 60.0],
"pelon": [100.0, 100.0, 100.0]}

student_name = input("Enter student name (ivan, antonio, pelon): ").strip().lower()

if student_name == "":
    print("Error: no student name")
else:
    if student_name in student_grades:
        grades_list = student_grades[student_name]

        if len(grades_list) == 0:
            print("Error: this student has no grades.")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70.0

            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", is_passed)
    else:
        print("Error: student not found")

print("---------------------------------------------------")

# 5th Problem: Word frequency counter (list + dict)

"""
    Description: 
        Cuenta la frecuencia de cada palabra en una oración usando:
        - Una lista de palabras.
        - Un diccionario donde:
        - clave: palabra (string)
        - valor: frecuencia (int)
        El programa debe:
        1) Leer una oración.
        2) Convertirla a minúsculas y separarla en una lista de palabras.
        3) Construir un diccionario de frecuencias.
        4) Mostrar el diccionario completo y la palabra más frecuente.
        
Inputs:
- sentence (string).

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)


Validations:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.


Test cases:
1) Normal: 
    Enter a sentence: pelon pelon chaparron
    ----------------------------------------
    Words list: ['pelon', 'pelon', 'chaparron']
    Frequencies: {'pelon': 2, 'chaparron': 1}
    Most common word: pelon

2) Border:
    Enter a sentence: aawd
    ----------------------------------------
    Words list: ['aawd']
    Frequencies: {'aawd': 1}
    Most common word: aawd

3) Error: 
    Enter a sentence:
    ----------------------------------------
    Error: there isn't a sentence.

"""

# Código: 
sentence = input("Enter a sentence: ").strip()

if sentence == "":
    print("Error: there isn't a sentence.")
else:
    clean_text = sentence.lower()

    # Remove simple punctuation 
    """ I prefer to use replace() to remove .,!? 
    because it is straightforward and easy to understand.
    It is used to replace substrings within 
    a text string with other specified substrings.
"""

    clean_text = clean_text.replace(".", "")
    clean_text = clean_text.replace(",", "")
    clean_text = clean_text.replace("!", "")
    clean_text = clean_text.replace("?", "")

    words_list = clean_text.split()

    if len(words_list) == 0:
        print("Error: no words found.")
    else:
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # Find la puta palabra 
        most_common_word = ""
        highest_count = 0

        for word in freq_dict:
            if freq_dict[word] > highest_count:
                highest_count = freq_dict[word]
                most_common_word = word

        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)

print("----------------------------------------------------")

# 6th Problem: Simple contact book (dictionary CRUD)

"""
    Description: 
        Implementa un mini "contact book" usando un diccionario donde:
        - clave: nombre de contacto (string)
        - valor: número de teléfono (string)
        El programa debe:
        1) Crear un diccionario inicial con algunos contactos.
        2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
        3) Según la acción:
        - "ADD": lee name y phone, agrega o actualiza el contacto.
        - "SEARCH": lee name y muestra el teléfono si existe.
        - "DELETE": lee name y elimina el contacto si existe.
        4) Mostrar un mensaje indicando el resultado de la operación.
        
Inputs:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD").

Outputs:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"


Validations:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().


Test cases:
1) Normal: 
    Enter action (ADD, SEARCH, DELETE): SEARCH
    Enter contact name (pellon, ivan, antonio): ivan
    ----------------------------------------
    Phone: 8342012939

2) Border:
    Enter action (ADD, SEARCH, DELETE): add
    Enter contact name (pellon, ivan, antonio): pellon
    Enter phone number: 1234wd
    ----------------------------------------
    Contact saved: pellon 1234wd

3) Error: 
    Enter action (ADD, SEARCH, DELETE):
    ----------------------------------------
    Error: invalid action.

"""

contacts = {
    "pellon": "812345409",
    "ivan": "8342012939",
    "antonio": "091209120912"
}

action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action.")
else:
    name = input("Enter contact name (pellon, ivan, antonio): ").strip()

    if name == "":
        print("Error: name cannot be empty.")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()

            if phone == "":
                print("Error: phone cannot be empty.")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: invalid input")

print("--------------------------------------------------------")

# Conclusion

"""
    Las listas convienen cuando necesitamos colecciones dinámicas que cambian durante la ejecución.
    Su capacidad de agregar y eliminar elementos facilita manejar datos variables o acumulativos.
    Las tuplas son útiles cuando los valores deben permanecer fijos, como coordenadas o configuraciones.
    Los diccionarios destacan por permitir búsquedas rápidas mediante claves en lugar de posiciones.
    Un patrón común es usar diccionarios que almacenan listas, lo que permite agrupar múltiples elementos
    bajo una misma clave y organizar mejor la información en estructuras más complejas.

"""

# Referencias

"""
    https://ellibrodepython.com/tuplas-python
    
    https://elpythonista.com/tuplas-en-python-tuple

    https://ellibrodepython.com/listas-en-python

    https://ellibrodepython.com/diccionarios-en-python

    https://www.w3schools.com/python/python_dictionaries.asp

"""