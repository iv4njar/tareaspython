# Manejo de Numeros y Booleanos en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

"""
    -¿Que son los tipos int y float en python? ¿En que se diferencian?
    En Python, los tipos int y float representan números enteros y números con decimales, respectivamente,
    y se diferencian en que los enteros no tienen parte fraccionaria mientras que los flotantes sí.
    
    -¿Que es un booleano y como se obtiene en un programa?
    Un booleano es un tipo de dato que solo puede ser True o False, y normalmente se obtiene mediante
    comparaciones como ==, >, < o >=, que evalúan condiciones en un programa.
    
    -¿Por que es importante validar rangos y evitar division entre cero en un programa?
    Validar rangos es esencial para evitar datos imposibles o incoherentes, y también para prevenir errores como la división entre cero,
    que detiene la ejecución del programa. Este documento cubrirá la descripción de cada problema,
    el diseño de las entradas y salidas, las validaciones aplicadas y la forma en que se utilizan enteros,
    flotantes y booleanos para tomar decisiones dentro de las soluciones.

"""

print("--------------------------------------------------------")

# 1st problem: Temperature converter and range flag

"""
    Description: 
        Convierte una temperatura en grados Celsius (float) a Fahrenheit y Kelvin. Además,
        determina un valor booleano is_high_temperature que sea true si la
        temperatura en Celsius es mayor o igual que 30.0 y false en caso contrario.

Inputs:
-temp_c (float:temperatura en grados Celsius) 

Outputs:
- "Fahrenheit:" <temp_f>
- "Kelvin:" <temp_k>
- "High temperature:" true|false

Validations:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).

Test cases:
1) Normal: 25.0
   Output:
    Fahrenheit: 77.0
    Kelvin: 298.15
    High temperature: false

2) Border: -509.67
   Output:
    Error: Temperature in Kelvin cannot be below 0.0 K.

3) Error: "abc "
   Output:
    Error: invalid input. Please enter a valid number for temperature.

"""

temp_c = input("Enter temperature in °C: ")

try:
    temc = float(temp_c)
    
    temf = (temc * 9/5) + 32
    temk = temc + 273.15
    
    if temk < 0.0:
        print("Error: Temperature in Kelvin cannot be below 0.0 K.")
    else:
        temhigh = temc >= 30.0
        
        print("Fahrenheit:", temf)
        print("Kelvin:", temk)
        print("High temperature:", temhigh)
except ValueError:
    print("Error: invalid input. Please enter a valid number for temperature.")


print("--------------------------------------------------------")


# 2nd problem: Work hours and overtime payment

"""
    Description: 
        Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float).
        Las horas extra (> 40) se pagan al 150% de la tarifa normal.
        Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Inputs:
- hours_worked (float; horas trabajadas en la semana).
- hourly_rate (float; pago por hora).

Outputs:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

Validations:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 45 horas, 100/hora
    Output:
     Regular pay: 4000.0
     Overtime pay: 750.0
     Total pay: 4750.0
     Has overtime: true

2) Border: -20 horas, 50/hora
   Output:
    Error: invalid input.

3) Error: "abc ", 50/hora
   Output: 
    Error: invalid input. Please enter a valid number for hours worked and hourly rate.

"""

hours_worked = input("Enter hours worked in the week: ")
hourly_rate = input("Enter hourly rate: ")

try:
    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)
    if hours_worked >= 0 and hourly_rate > 0:



        if hours_worked <= 40:
            regular_pay = hours_worked * hourly_rate
            over_pay = 0.0
            total_pay = regular_pay
            has_overtime = False
            print("Regular pay:", regular_pay)
            print("Overtime pay:", over_pay)
            print("Total pay:", total_pay)
            print("Has overtime:", has_overtime)
        elif hours_worked > 40:
            regular_pay = 40 * hourly_rate
            over_hours = hours_worked - 40
            over_pay = over_hours * hourly_rate * 1.5
            has_overtime = True
            total_pay = regular_pay + over_pay
            print("Regular pay:", regular_pay)
            print("Overtime pay:", over_pay)
            print("Total pay:", total_pay)
            print("Has overtime:", has_overtime)
    else:
        print("Error: invalid input.")  
except ValueError:
    print("Error: invalid input. Please enter a valid number for hours worked and hourly rate.")

print("--------------------------------------------------------")

# 3rd problem: Discount eligibility with booleans

"""
    Description: 
        Determina si un cliente obtiene un descuento en su compra. La regla es:
        - Tiene descuento si:
        - is_student es true OR
        - is_senior es true OR
        - purchase_total >= 1000.0
        Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Inputs:
- purchase_total (float; total de la compra).
- is_student_text (string; "YES" o "NO").
- is_senior_text (string; "YES" o "NO").

Outputs:
- "Discount eligible:" true|false
- "Final total:" <final_total>

Validations:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".

Test cases:
1) Normal: 
    Enter purchase total: 1000
    Is the customer a student? (YES/NO): yes
    Is the customer a senior? (YES/NO): no
    --------------------------
    Discount eligible: True
    Final total: 900.0
            

2) Border: 
    Enter purchase total: 900
    Is the customer a student? (YES/NO): no
    Is the customer a senior? (YES/NO): no
    Discount eligible: False
    Final total: 900.0

3) Error: 

"""

# set values int and booleans
purchase_total = input("Enter purchase total: ")
is_student_text = input("Is the customer a student? (YES/NO): ")
is_senior_text = input("Is the customer a senior? (YES/NO): ")

# validate conversion 
try:
    int(purchase_total) >= 0
    purchase_total = float(purchase_total)
        
    # normalize strings
    is_student_text = is_student_text.strip().upper()
    is_senior_text = is_senior_text.strip().upper()
    
    # conversion strings to boolens
    if is_student_text =="YES":
        is_student = True
    if is_senior_text=="YES":
        is_senior= True
    if is_student_text =="NO":
        is_student= False
    if is_senior_text=="NO":
        is_senior= False

        
  
    # validate discount 
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    if discount_eligible == True:

        # do a operation and print results
        final_total = purchase_total * 0.9
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total}" )     
    else:

        # conditional false
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {purchase_total}")  
    # error message
except ValueError:
    print("Error: invalid input.")

print("----------------------------------------------------------")

# 4th problem: Basic statistics of three integers

"""
    Description: 
        Lee tres números enteros y calcula: suma, promedio (float),
        valor máximo, valor mínimo y un booleano all_even que indique si los tres números son pares.

Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

Outputs:
- "Sum:" <sum_value>
- "Average:" <average_value>
- "Max:" <max_value>
- "Min:" <min_value>
- "All even:" true|false

Validations:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).

Test cases:
1) Normal:
    First value: 3
    Second value: 8
    Third value: 15
    --------------------------
    Sum: 26
    Average: 8.666666666666666
    Max: 15
    Min: 3
    All even: False

2) Border: 
    First value: 12
    Second value: 23.4
    Third value: 2
    --------------------------
    Error: Invalid value

3) Error: 
    First value: ola
    Second value: cuatro
    Third value: dos
    --------------------------
    Error: Invalid value

"""
# input all values
n1 = input("First value: ")
n2 = input("Second value: ")
n3 = input("Third value: ")

# validate a conversion
try:
    num1 = int(n1)
    num2 = int(n2)
    num3 = int(n3)

    # do operations
    sum = num1 + num2 + num3
    avrg = sum/3
    max_n = max(num1, num2, num3)
    min_n = min(num1, num2, num3)

    # validate the all_even
    all_even = (num1 % 2 == 0) and (num2 % 2 == 0) and (num3 % 2 == 0)
    
    # print results
    print(f"Sum: {sum}") 
    print(f"Average: {avrg}")
    print(f"Max: {max_n}")
    print(f"Min: {min_n}")
    print(f"All even: {all_even}")

    # error message
except ValueError:
    print("Error: Invalid value")


print("--------------------------------------------------------")

# 5th problem: Loan eligibility

"""
    Description: 
        Determina si una persona es elegible para un préstamo con base en:
        - monthly_income (float)
        - monthly_debt (float)
        - credit_score (int)
        La regla es:
        - debt_ratio = monthly_debt / monthly_income
        - eligible es true si:
        - monthly_income >= 8000.0 AND
        - debt_ratio <= 0.4 AND
        - credit_score >= 650

Inputs:
- monthly_income (float; ingreso mensual).
- monthly_debt (float; pagos mensuales de deuda).
- credit_score (int; puntaje de crédito).

Outputs:
- "Debt ratio:" <debt_ratio>
- "Eligible:" true|false

Validations:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".

Test cases:
1) Normal:
    Give me your monthly income: 8000
    Give me your monthly debt: 1000
    Give me your credit score: 700
    --------------------------
    your debt ratio is : 0.125
    eligible: True

2) Border: 
    Give me your monthly income: 8000
    Give me your monthly debt: 1000
    Give me your credit score: 500
    --------------------------
    your debt ratio is : 0.125
    eligible: False

3) Error: 
    Give me your monthly income: askdkj
    Give me your monthly debt: "  "
    Give me your credit score: 10
    --------------------------
    Error: invalid input

"""

monthly_income1 = input("Give me your monthly income: ")
monthly_debt1 = input("Give me your monthly debt: ")
credit_score1 = input("Give me your credit score: ")

try:
    monthly_income = float(monthly_income1)
    monthly_debt = float(monthly_debt1)
    credit_score = int(credit_score1)


    # Validate ranges
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")



        
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
    print(f"your debt ratio is : {debt_ratio}")
    print(f"eligible: {eligible}")

except ValueError:
    print("Error: invalid input")

print("--------------------------------------------------------")

# 6th problem: Body Mass Index (BMI) calculator and category flag

"""
    Description: 
        - bmi = weight_kg / (height_m * height_m)
        Además, genera booleanos para indicar:
        - is_underweight (bmi < 18.5)
        - is_normal (18.5 <= bmi < 25.0)
        - is_overweight (bmi >= 25.0)

Inputs:
- weight_kg (float; peso en kilogramos).
- height_m (float; estatura en metros).

Outputs:
- "BMI:" <bmi_redondeado>
- "Underweight:" true|false
- "Normal:" true|false
- "Overweight:" true|false

Validations:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".

Test cases:
1) Normal: 
    Set your weight: 70
    Set your height: 1.65
    --------------------------
    BMI: 25.71
    Underweight: False
    Normal: False
    Overweight: True

2) Border:
    Set your weight: -2
    Set your height: -3.43
    --------------------------
    invalid values

3) Error: 
    Set your weight: hola
    Set your height: ivan
    --------------------------
    Error: Invalid values

"""

# input values
weight_kg = input("Set your weight: ")
height_m = input("Set your height: ")

# validate conversion to float
try:
    weight_f = float(weight_kg)
    height_f = float(height_m)

    # validate correct values
    if weight_f <= 0.0 or height_f <= 0.0:
        print("invalid values")
        exit()

        
    # do operations
    bmi = weight_f / (height_f * height_f)
    bmi_redondeado = round(bmi, 2)

    # validate in booleans
    is_underweight = bmi < 18.5
    is_normal = 18.5 <= bmi < 25.0
    is_overweight = bmi >= 25.0

    # print a results
    print(f"BMI: {bmi_redondeado}")
    print(f"Underweight: {str(is_underweight)}")
    print(f"Normal: {str(is_normal)}")
    print(f"Overweight: {str(is_overweight)}")

    # Error message
except ValueError:
    print("Error: Invalid values")


# conclusion

""" 
    Los enteros y flotantes suelen usarse juntos para representar cantidades reales y realizar cálculos precisos.
    Las comparaciones generan booleanos que permiten controlar el flujo del programa mediante if.
    También es clave validar rangos y evitar errores como dividir entre cero.
    Al combinar condiciones con and, or y not, aprendí a expresar reglas más completas y útiles.
    Estos mismos patrones aparecen en problemas prácticos como nóminas, descuentos o préstamos,
    donde se requiere evaluar datos y tomar decisiones basadas en ellos.

"""

# Referencias:

"""

    https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

    https://docs.python.org/3/library/stdtypes.html#boolean-values

    https://docs.python.org/3/reference/expressions.html

    https://ellibrodepython.com/booleano-python

    https://www.youtube.com/watch?v=cRAI35f50ls

"""