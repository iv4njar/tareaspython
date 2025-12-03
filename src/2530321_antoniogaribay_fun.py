
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


#Código: 
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


#Código: 
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



#Código: 
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


#Código: 
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



#Código: 
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