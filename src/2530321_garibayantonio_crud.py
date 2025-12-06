# CRUD en Python

# Hecho por Ivan Antonio Segura Garibay
# Matrícula: 2530321
# grupo: 1-1 IM

"""
    ¿Qué es un CRUD y qué significan Create, Read, Update, Delete?
    Un CRUD es un conjunto de operaciones básicas para gestionar datos:
    Create (crear), Read (leer), Update (actualizar) y Delete (eliminar).

    ¿Qué estructura de datos elegiste (dict o list de dicts) y por qué?
    Elegí usar una lista de diccionarios porque permite almacenar múltiples
    elementos estructurados y manejar cada registro de forma flexible.

    ¿Cómo te ayuda usar funciones para organizar la lógica del CRUD?
    El uso de funciones ayuda a separar la lógica de cada operación, evitando
    repetir código y haciendo el programa más claro y mantenible.

    ¿Qué cubre tu programa?
    Mi programa incluye un menú principal y funciones para crear, leer,
    actualizar, eliminar y listar todos los elementos registrados.

"""

print("-----------------CRUD-----------------")

"""
Problem: In-memory CRUD manager with functions  


Descripción: 
Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar) simple para elementos almacenados 
en un diccionario y/o lista, usando funciones para cada operación y un menú de texto para interactuar con el usuario.

Inputs:
- User menu options (string or int).
- For CREATE/UPDATE: item_id, name, price, quantity (or the fields you define).
- For READ/DELETE: item_id.

Outputs:
- Messages indicating the result of each operation:
  - "Item created", "Item updated", "Item deleted", "Item not found", "Items list:", etc.

Validations:
- Menu option must be valid (for example, 0..4 o 0..5 según tu diseño).
- item_id must not be empty.
- Numeric fields must be valid numbers and greater than or equal to 0.
- Disallow creating an item with an id that is already in use (or document tu decisión).
- For READ/UPDATE/DELETE, if the id does not exist, show "Item not found".

Test cases:
1) Normal:
-----------------CRUD-----------------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Enter item id: 2530321
Enter name: ivan
Enter price: 1000
Enter quantity: 5
----------------
Item created
----------------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 2
Enter item id: 2530321
----------------
Item found: {'name': 'ivan', 'price': 1000.0, 'quantity': 5}
----------------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 3
Enter item id: 2530321
Enter new name: pelon
Enter new price: 150
Enter new quantity: 10
----------------
Item updated
----------------
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 4
Enter item id: 2530321
----------------
Item deleted
----------------


2) Border: 
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 1
Enter item id: #$%
Enter name: 23
Enter price: 2
Enter quantity:
-----------------
Error: invalid input
-----------------

3) Error:
1) Create item
2) Read item by id
3) Update item by id
4) Delete item by id
5) List all items
0) Exit
Choose an option: 10
--------------------
Error: invalid input
--------------------

"""

def create_item(data, item_id, name, price, quantity):
    if item_id in data:
        return False 
    data[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(data, item_id):
    return data.get(item_id)


def update_item(data, item_id, new_name, new_price, new_quantity):
    if item_id not in data:
        return False
    data[item_id] = {
        "name": new_name,
        "price": new_price,
        "quantity": new_quantity
    }
    return True


def delete_item(data, item_id):
    if item_id in data:
        del data[item_id]
        return True
    return False


def list_items(data):
    if not data:
        print("No items")
    else:
        print("Items list:")
        for _id, info in data.items():
            print(f"- id: {_id}, name: {info['name']}, price: {info['price']}, quantity: {info['quantity']}")

def main():
    items = {} 
    while True:
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")

        option = input("Choose an option: ").strip()

        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        elif option == "1":
            item_id = input("Enter item id: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            name = input("Enter name: ").strip()
            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            if create_item(items, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: id already exists")

        elif option == "2":
            item_id = input("Enter item id: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            item = read_item(items, item_id)
            if item is None:
                print("Item not found")
            else:
                print("Item found:", item)

        elif option == "3":
            item_id = input("Enter item id: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            name = input("Enter new name: ").strip()
            try:
                price = float(input("Enter new price: "))
                quantity = int(input("Enter new quantity: "))
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            if update_item(items, item_id, name, price, quantity):
                print("Item updated")
            else:
                print("Item not found")

        elif option == "4":
            item_id = input("Enter item id: ").strip()
            if item_id == "":
                print("Error: invalid input")
                continue

            if delete_item(items, item_id):
                print("Item deleted")
            else:
                print("Item not found")
        elif option == "5":
            list_items(items)


if __name__ == "__main__":
    main()

# Conclusion

"""
    El uso de funciones simplificó el CRUD porque permitió separar claramente cada
    operación (crear, leer, actualizar y eliminar), evitando repetir lógica y haciendo
    que el código principal fuera más limpio y fácil de mantener. Trabajar con un
    diccionario o una lista de diccionarios resultó útil para organizar los datos de
    manera flexible y acceder rápido a los elementos. La validación de entradas fue
    uno de los mayores retos, especialmente al convertir precios y cantidades a números,
    pero se resolvió usando try/except y comprobando rangos válidos. Este CRUD podría
    ampliarse fácilmente para guardar datos en archivos JSON, CSV o incluso conectarse
    a una base de datos, permitiendo persistencia y un sistema más robusto.

"""

# Referencias

"""
    https://www.youtube.com/watch?v=Ro2m95m8QkI

    https://keepcoding.io/blog/crud-en-python/

    https://www.youtube.com/watch?v=u4tafm-8E3M

"""