from db_ejercicio3 import *
from datetime import *

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

onCreate()

EMPLEADOS = 1
PORCENTAJE_MES = 1
PORCENTAJE_HIJO = 5
IMPUESTO_SALUD = 7
IMPUESTO_AFAP = 12

print("APARTADO A")
for i in range(EMPLEADOS):
    print("NUEVO EMPLEADO: ")
    salir = False
    while not salir:
        nombre = input("Inserte nombre del empleado: ")
        if nombre == "":
            print("El nombre no puede estar vacío")
        else:
            salir = True

    salir = False
    while not salir:
        apellido = input("Inserte apellido del empleado: ")
        if apellido == "":
            print("El apellido no puede estar vacío")
        else:
            salir = True

    salir = False
    while not salir:
        try:
            sueldo_base = round(float(input("Introduzca sueldo_base del empleado: ")), 2)
            salir = True
        except:
            print("Has introducido caracteres erroneos en el sueldo")

    salir = False
    while not salir:
        opc = input("Inserte si el empleado pertenece a un AFAP (Si -> s / No -> n): ")
        if opc.lower() == "s" or opc.lower() == "si" or opc.lower() == "n" or opc.lower() == "no":
            if opc.lower() == "s" or opc.lower() == "si":
                afap = True
            else:
                afap = False

            salir = True
        else:
            print("Caracter incorrecto, introduzca si o no al AFAP")

    salir = False
    while not salir:
        try:
            ano_ingreso = int(input("Inserte año de ingreso del empleado: "))
            if len(str(ano_ingreso)) != 4:
                print("El año tiene que ser un número de 4 cifras")
            else:
                salir = True
        except:
            print("Has introducido un caracter incorrecto del año")

    salir = False
    while not salir:
        try:
            mes_ingreso = int(input("Inserte mes de ingreso del empleado: "))
            if not(1 <= len(str(mes_ingreso)) <= 2):
                print("El mes tiene que ser un número de 1 o 2 cifras")
            else:
                salir = True
        except:
            print("Has introducido un caracter incorrecto del mes")

    salir = False
    while not salir:
        try:
            dia_ingreso = int(input("Inserte dia de ingreso del empleado: "))
            if not(1 <= len(str(dia_ingreso)) <= 2):
                print("El dia tiene que ser un número de 1 o 2 cifras")
            else:
                try:
                    fecha_ingreso = date(ano_ingreso, mes_ingreso, dia_ingreso)
                    salir = True
                except:
                    print("Dia fuera de intervalo del mes")

        except:
            print("Has introducido un caracter incorrecto del dia")

    salir = False
    while not salir:
        try:
            cantidad_hijos = int(input("Introduzca cantidad_hijos del empleado: "))
            salir = True
        except:
            print("Has introducido caracteres erroneos en la cantidad_hijos")

    try:
        bd = connect("db_ejercicio3.db")
        cursor = bd.cursor()
        cursor.execute(
            "INSERT INTO Empleado (nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos) VALUES (?, ?, ?, ?, ?, ?);",
            (nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos))
        bd.commit()
        print("Se ha añadido el empleado correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()

print("TABLA EMPLEADOS")
try:
    bd = connect("db_ejercicio3.db")
    cursor = bd.cursor()
    cursor.execute('''
        SELECT 
            *
        FROM 
            Empleado;
    ''')

    empleados = cursor.fetchall()
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", "", ""))
    print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format("id_empleado", "nombre", "apellido", "sueldo_base", "afap", "fecha_ingreso", "cantidad_hijos"))
    print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", "", ""))

    for id_empleado, nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos in empleados:
        print("|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|".format(id_empleado, nombre, apellido, sueldo_base, afap, fecha_ingreso, cantidad_hijos))

    print("+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+{:-<20}+".format("", "", "", "", "", "", ""))
except OperationalError as error:
    print("Error al abrir:", error)
finally:
    cursor.close()


salir = False
while not salir:
    try:
        id_empleado = int(input("Introduzca id_empleado a calcular la base imponente: "))
        salir = True
    except:
        print("Has introducido caracteres erroneos en el id_empleado")


try:
    bd = connect("db_ejercicio3.db")
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM Empleado WHERE id_empleado=?;", (str(id_empleado)))

    empleado: Row = cursor.fetchone()

    sueldo_base = float(empleado[3])
    afap = bool(empleado[4])
    fecha_ingreso = date(int(empleado[5].split("-")[0]), int(empleado[5].split("-")[1]), int(empleado[5].split("-")[2]))
    cantidad_hijos = int(empleado[6])

except OperationalError as error:
    print("Error al abrir:", error)
finally:
    cursor.close()

meses = diff_month(date.today(), fecha_ingreso)

base_imponible = (sueldo_base * (((meses * PORCENTAJE_MES) + 100) / 100)) + (sueldo_base * (((cantidad_hijos * PORCENTAJE_HIJO) + 100) / 100))

print("APARTADO B")
print(f"Base imponible total: {round(base_imponible, 2)}€")
print(f"Base imponible aplicando impuestos: {round(base_imponible * (((100 - IMPUESTO_SALUD) / 100)), 2)}€")

print("APARTADO C")
print(f"Pagar a FONSA: {round(base_imponible * (IMPUESTO_SALUD / 100), 2)}€")

if afap:
    print(f"Pagar a AFAP: {round(base_imponible * (IMPUESTO_AFAP / 100), 2)}")

print("APARTADO D")
try:
    bd = connect("db_ejercicio3.db")
    cursor = bd.cursor()
    cursor.execute("SELECT AVG(sueldo_base) FROM Empleado;")

    empleado: Row = cursor.fetchone()

    media = round(float(empleado[0]))

except OperationalError as error:
    print("Error al abrir:", error)
finally:
    cursor.close()

print(f"La media de pago de todos los empleados es: {media}€")