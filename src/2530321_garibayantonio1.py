# Manejo de strings en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

# Definición de una cadena de texto

"""
    ¿Qué es un string en Python?

    Un string en Python es un tipo de dato que representa texto y es inmutable,
    lo que significa que no puede modificarse después de crearse.

    ¿Que operaciones basicas se pueden realizar?

    Se pueden realizar operaciones como concatenar, obtener su longitud, extraer subcadenas, buscar
    patrones y reemplazar partes del texto.

    ¿Por qué es importante validar y normalizar strings?

    Es importante validar y normalizar el texto de entrada (como correos, nombres o contraseñas) para evitar errores,
    inconsistencias o vulnerabilidades.

    ¿Que cubrira este documento?

    Este documento cubrirá la descripción de cada problema, el diseño de entradas y salidas, las validaciones aplicadas y
    el uso de métodos de string con casos de prueba, incluyendo el código utilizado.
"""

print("--------------------------------")

# 1st Problem: Full name formatter
"""
    Description: 
        A partir de una cadena que contenga el nombre completo de una persona (por ejemplo: 'juan carlos tovar'), 
        el programa deberá:
        Limpiar y estandarizar el texto eliminando espacios innecesarios y ajustando el uso de mayúsculas y minúsculas.
        Presentar el nombre con formato Title Case y generar sus iniciales (por ejemplo: J.C.T.)."**

Inputs:
-full_name 

Outputs:
- "Formatted name: <Name In Title Case>"
- "Initials: <X.X.X.>"

Validations:
- full_name no debe estar vacío después de strip().
- Debe contener al menos dos palabras (por ejemplo, nombre y apellido).
- No aceptar cadenas que sean solo espacios.

Test cases:
1) Normal: ivan antonio segura garibay
   Output:
   Formatted name: Ivan Antonio Segura Garibay
   Initials: I.A.S.G.
2) Border:iv
   Output:
    Formatted name: Iv
    Initials: I.
3) Error: "  "
   Output:
    Error: invalid input. The name cannot be empty or just spaces.
        
"""
# input full name
full_name = input("Enter full name: ")

# validate full name
if full_name.strip() == "":

    # print error for empty input
    print("Error: invalid input. The name cannot be empty or just spaces.")
elif len(full_name.strip()) < 2:

    # print error for insufficient words
    print("Error: invalid input. The name must contain at least two words.")
else:
    # Clean and standardize the text
    cleaned_name = " ".join(full_name.strip().title().split())
    
    # generate initials
    initials = ".".join([part[0].upper() for part in cleaned_name.split()]) + '.'
    
    print(f"Formatted name: {cleaned_name}")
    print(f"Initials: {initials}")

print("--------------------------------")

# 2nd Problem: Email Validator

"""
    Description: 
        Revisa si un correo está bien escrito de forma básica:
        Debe tener solo un @.
        Después del @ tiene que haber al menos un punto.
        No debe tener espacios.
        Si todo está correcto, también muestra el dominio, o sea, lo que va después del @.  

Inputs:
-email_text 

Outputs:
- "Valid email: true" o "Valid email: false"
- Si es válido: "Domain: <domain_part>"

Validations:
- email_text no vacío tras strip().
- Contar cuántas veces aparece '@'.
- Verificar que no haya espacios (no debe haber " " en email_text).

Test cases:
1) Normal: ivanantonio@gmai.com
    Output:
     Valid email: true
     Domain: gmai.com
2) Border: ivanantonio@gmaicom
    Output:
     Valid email: false
3) Error: "  "
   Output:
    Error: invalid input. The email cannot be empty or just spaces.
        
"""
# input email
email_text = input("Enter email address: ")

# validate email structure
if email_text.strip() == "":

    # print error for empty input
    print("Error: invalid input. The email cannot be empty or just spaces.")
elif email_text.count('@') != 1 or " " in email_text:

    # print invalid email
    print("Valid email: false") 
else:

    # split email into parts
    part1, part2 = email_text.split("@")

    # validate domain part
    if "." in part2:

        # print valid email and domain
        print("Valid email: true")
        print(f"Domain: {part2}")
    else:

        # print invalid email
        print("Valid email: false")

print("--------------------------------")

# 3rd Problem: Palindrome checker

"""
    Description: 
        Determina si una frase es un palíndromo, es decir,
        se lee igual de izquierda a derecha y de derecha a izquierda,
        ignorando espacios y mayúsculas/minúsculas. 

Inputs:
-phrase  

Outputs:
- "Is palindrome: true" o "Is palindrome: false"
- (Opcional) Mostrar también la versión normalizada de la frase.

Validations:
- phrase no vacía tras strip().
- Longitud mínima razonable después de limpiar espacios (por ejemplo, al menos 3 caracteres).

Test cases:
1) Normal: reconocer
   Output:
    Is palindrome:true 
    Normalized phrase: reconocer
2) Border: anita lava la noria
    Output:
     Is palindrome:false 
     Normalized phrase: anitalavalanoria
3) Error: "   "
   Output: 
    Error: invalid input. The phrase cannot be empty or just spaces.
        
"""
# input phrase
phrase = input("Enter a phrase: ")

# validate phrase
if phrase.strip() == "":

    # print error for empty input
    print("Error: invalid input. The phrase cannot be empty or just spaces.")   
else:

    # normalize phrase
    phrase_normalized = "".join(phrase.strip().lower().split())
    
    # check if palindrome
    palindrome = phrase_normalized == phrase_normalized[::-1]
    
    # print results
    print("Is palindrome:" + str(palindrome))
    print(f"Normalized phrase: {phrase_normalized}")

print("--------------------------------")

# 4th Problem: Sentence word stats

"""
    Description: 
        Dada una oración, el programa debe:
            1) Normalizar espacios (quitar espacios al principio y al final).
            2) Separar las palabras por espacios.
            3) Mostrar:
                - Número total de palabras.
                - Primera palabra.
                - Última palabra.
                - Palabra más corta y más larga (por longitud). 

Inputs:
-sentence   

Outputs:
- "Word count: <n>"
- "First word: <...>"
- "Last word: <...>"
- "Shortest word: <...>"
- "Longest word: <...>"

Validations:
- Oración no vacía tras strip().
- Debe contener al menos una palabra válida después de split().

Test cases:
1) Normal: hola a todos
    Outpot:
    Word count:3
    First word:hola
    Last word:todos
    Shortest word:a
    Longest word:todos
2) Border: 
3) Error: "   "
   Output: 
    Error: invalid input. The phrase cannot be empty or just spaces.
        
"""

# input sentence
sentence = input("Enter a sentence: ")

# validate sentence
if sentence.strip() == "":

    # print error for empty input
    print("Error: invalid input. The sentence cannot be empty or just spaces.")

else:

    # normalize sentence
    cleaned_sentence = sentence.strip()

    # separate words
    words = cleaned_sentence.split()

    # print results
    print("Word count:"+ str(len(words)))
    print("Frist word:"+ words[0])
    print("Last word:"+ words[-1])
    print("Shortest word:"+ min(words, key=len))
    print("Longest word:"+ max(words, key=len))

print("--------------------------------")

# 5th Problem: Password strength classifier

"""
    Description: 
        Dada una contraseña Clasifica una contraseña como
        "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas,
        pero documéntalas en los comentarios). 

Inputs:
-password_input    

Outputs:
- "Password strength: weak"
- "Password strength: medium"
- "Password strength: strong"

Validations:
- No aceptar contraseña vacía.
- Verificar longitud con len().

Test cases:
1) Normal:longpasswordWITH123
    Outpot:
    Password strength: strong
2) Border: ivan
    Outpot:
    Password strength: weak
3) Error: ""
   Output: 
    Error: invalid input. The phrase cannot be empty or just spaces.
        
"""
# input password
password_input = (input("Enter a password: "))
password_input.strip()

if password_input == "":

    # print error for empty input
    print("Error: invalid input. The password cannot be empty or just spaces.")
elif len(password_input) < 8 and password_input.islower() or password_input.isdigit():
    print("Password strength: weak")
elif len(password_input) >= 8 and any(password_input.islower() for c in password_input) and any(password_input.isupper() for c in password_input) and any(password_input.isdigit() for c in password_input) and any(not c.isalnum() for c in password_input):
    print("Password strength: Strong")
else:
    print("Password strength: Medium")


print("--------------------------------")

# 6th Problem: Product label formatter (fixed-width text)

"""
    Description: 
        Dado el nombre de un producto y su precio,
        genera una etiqueta en una sola línea con el siguiente formato:


Inputs:
- product_name (string).
- price_value (puede leerse como string o número; conviértelo a string para mostrarlo).
 

Outputs:
- "Label: <exactly 30 characters>"
(Puedes mostrar la etiqueta entre comillas para que se vean los espacios.)

Validations:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.

Test cases:
1) Normal: 
2) Border: 
3) Error: "   "
   Output: 
    Error: invalid input. The phrase cannot be empty or just spaces.
        
"""

product_name = input("name product :")
price_value = (str(input("price product :")))

if product_name.strip() == "":
    print("Error: invalid input. The product name cannot be empty or just spaces.")
else:
    try:
        price_float = float(price_value)
        if price_float < 0:
            raise ValueError("Negative price")
        
        label = f"{product_name.strip():.<20}${price_float:>7.2f}"
        print(f'Label: "{label}"')
    except ValueError:
        print("Error: invalid input. The price must be a positive number.")
 
    

# Conclusion:

"""
    El manejo de strings es esencial en la entrada y salida de datos porque casi toda la información
    que recibe un programa —nombres, correos, comandos, respuestas— llega en forma de texto.
    Funciones como lower(), strip(), split() o join() convienen cuando queremos limpiar, organizar
    o transformar cadenas para que sean consistentes. Normalizar el texto antes de compararlo es
    importante para evitar errores por mayúsculas, espacios o formatos diferentes. Un buen diseño de
    validaciones previene datos basura y hace que los programas sean más robustos. Además, entender la
    inmutabilidad de los strings y el uso de slices ayuda a manipular texto sin modificar el original.
"""

# Referencias: 

"""
    https://ellibrodepython.com/cadenas-python

    https://www.w3schools.com/python/python_strings.asp

    https://www.youtube.com/watch?v=CSGedJV6Yv8

    http://programaenpython.com/fundamentos/strings-en-python/

    https://programminghistorian.org/es/lecciones/manipular-cadenas-de-caracteres-en-python

"""