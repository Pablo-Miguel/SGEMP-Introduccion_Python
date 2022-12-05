from db_ejercicio2 import *

onCreate()
onCreateInsertData()

DESPIDOS = 3
AGREGAR = 8

for i in range(DESPIDOS):
    print("TABLA EMPLEADOS")
    try:
        bd = connect("db_ejercicio2.db")
        cursor = bd.cursor()
        cursor.execute('''
            SELECT 
                *
            FROM 
                Empleado;
        ''')

        empleados = cursor.fetchall()
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("id_empleado", "dni_empleado", "nombre", "telefono", "salario"))
        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))

        for id_empleado, dni_empleado, nombre, telefono, salario, cod_localidad in empleados:
            print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(id_empleado, dni_empleado, nombre, telefono, salario))

        print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", ""))
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

    id_empleado = input(f"Inserte el id_empleado número {i + 1} a despedir: ")

    try:
        bd = connect("db_ejercicio2.db")
        cursor = bd.cursor()
        cursor.execute("DELETE FROM Empleado WHERE id_empleado=?;", (id_empleado))
        bd.commit()
        print("Empleado eliminado correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()


for i in range(AGREGAR):
    print("NUEVO EMPLEADO: ")
    dni_empleado = input("Inserte dni_empleado: ")
    nombreEmpl = input("Inserte nombre del empleado: ")
    telefono = input("Introduzca telefono del empleado: ")
    salario = input("Inserte salario del empleado: ")

    print("\nTABLA LOCALIDADES")
    try:
        bd = connect("db_ejercicio2.db")
        cursor = bd.cursor()
        cursor.execute('''
                        SELECT 
                            cod_localidad, 
                            nombre
                        FROM 
                            Localidad;
                    ''')

        licalidades = cursor.fetchall()
        print("+{:-<20}+{:-<20}+".format("", ""))
        print("|{:^20}|{:^20}|".format("cod_localidad", "nombre"))
        print("+{:-<20}+{:-<20}+".format("", ""))

        for cod_localidad, nombre in licalidades:
            print("|{:^20}|{:^20}|".format(cod_localidad, nombre))

        print("+{:-<20}+{:-<20}+".format("", ""))
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

    cod_localidad = input("Inserte cod_localidad del empleado: ")

    try:
        bd = connect("db_ejercicio2.db")
        cursor = bd.cursor()
        cursor.execute("INSERT INTO Empleado (dni_empleado, nombre, telefono, salario, cod_localidad) VALUES (?, ?, ?, ?, ?);", (dni_empleado, nombreEmpl, telefono, salario, cod_localidad))
        bd.commit()
        print("Se ha añadido el empleado correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()