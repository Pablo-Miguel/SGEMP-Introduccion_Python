from sqlite3 import *

def onCreate():
    try:
        bd = connect("db_ejercicio3.db")
        cursor = bd.cursor()
        sentencia = '''
            CREATE TABLE IF NOT EXISTS "Empleado" (
                "id_empleado"	INTEGER,
                "nombre"	TEXT,
                "apellido"	TEXT,
                "sueldo_base"	REAL,
                "afap"	TEXT,
                "fecha_ingreso"	TEXT,
                "cantidad_hijos"	INTEGER,
                PRIMARY KEY("id_empleado" AUTOINCREMENT)
            )
            '''
        cursor.execute(sentencia)
        print("Tablas creadas correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()