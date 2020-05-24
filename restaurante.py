import sqlite3

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("la tabla de categorias ya existe")
    else:
        print("La tabla de categorias se ha creado correctamente")

    try:
        cursor.execute('''CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id)
        )''')
    except sqlite3.OperationalError:    
        print("la tabla Platos ya existe")
    else:
        print("la tabla Platos se ha creado correctamente")

    conexion.close()

def agregar_categoria():
    categoria = input("¿Nombre de la Nueva Categoria?\n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(
            categoria) )
    except sqlite3.IntegrityError:
        print("la categoria '{}' ya existe.".format(categoria))
    else:
        print("categoria '{}' creada correctamente.".format(categoria))

    conexion.commit()
    conexion.close()


def agregar_plato():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("selecciona una categoria para añadir el plato: ")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario = int(input("> "))

    plato = input("¿Nombre del nuevo plato?\n")

    try:
        cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario) )

    except sqlite3.IntegrityError:
        print("El PLato '{}' ya existe".format(plato))
    else:
        print("PLato '{}' creado correctamente".format(plato))

    conexion.commit()
    conexion.close()

def mostrar_menu():

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categorias:
        print(categoria[1])
        platos = cursor.execute(
            "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()

        for platos in platos:
            print("\t{}".format(plato[1]))

    conexion.close()

crear_db()



#menu de opciones
while True:

    #opcion = '0'
    
    print("\nBienvenido al gestor del restaurante!")

        
    print("Introduce una opción: ")
    print("[1] Agregar una categoría") 
    print("[2] Agregar un plato") 
    print("[3] Mostrar el menú")
    print("[4] Salir del programa") 
    opcion = input()
    

    if opcion == '1':
        agregar_categoria()

    elif opcion == '2':
        agregar_plato()

    elif opcion == '3':
        mostrar_menu()

    elif opcion == '4':
        print('nos vemos')
        break

    else:
        print('opcion incorrecta')