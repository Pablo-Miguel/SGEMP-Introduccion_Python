from sqlite3 import *

def onCreate():
    try:
        bd = connect("db_ejercicio2.db")
        cursor = bd.cursor()
        tablas = [
            '''
            CREATE TABLE IF NOT EXISTS "Region" (
                "nombre_region"	TEXT,
                PRIMARY KEY("nombre_region")
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS "Provincia" (
                "cod_provincia"	INTEGER,
                "nombre_provincia"	TEXT,
                "nombre_region"	INTEGER,
                PRIMARY KEY("cod_provincia" AUTOINCREMENT),
                FOREIGN KEY("nombre_region") REFERENCES "Region"("nombre_region")
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS "Localidad" (
                "cod_localidad"	INTEGER,
                "nombre"	TEXT,
                "cod_provincia"	INTEGER,
                PRIMARY KEY("cod_localidad" AUTOINCREMENT),
                FOREIGN KEY("cod_provincia") REFERENCES "Provincia"("cod_provincia")
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS "Empleado" (
                "id_empleado"	INTEGER,
                "dni_empleado"	TEXT,
                "nombre"	TEXT,
                "telefono"	TEXT,
                "salario"	REAL,
                "cod_localidad"	INTEGER,
                PRIMARY KEY("id_empleado" AUTOINCREMENT),
                FOREIGN KEY("cod_localidad") REFERENCES "Localidad"("cod_localidad")
            )
            '''
        ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()


def onCreateInsertData():
    try:
        bd = connect("db_ejercicio2.db")
        cursor = bd.cursor()
        insterts = [
            """
            INSERT INTO Region
            (nombre_region)
            VALUES
            ('Andalucia');
            """,
            """
            INSERT INTO Provincia
            (nombre_provincia, nombre_region)
            VALUES
            ('Cadiz', 'Andalucia');
            """,
            """
            INSERT INTO Localidad
            (nombre, cod_provincia)
            VALUES
            ('Jerez de la frontera', 1);
            """,
            """
            INSERT INTO Empleado
            (dni_empleado, nombre, telefono, salario, cod_localidad)
            VALUES
            ('00000000A', 'Empleado1','000000001', 1100.00, 1),
            ('00000000B', 'Empleado2','000000002', 1200.00, 1),
            ('00000000C', 'Empleado3','000000003', 1300.00, 1),
            ('00000000D', 'Empleado4','000000004', 1400.00, 1),
            ('00000000E', 'Empleado5','000000005', 1500.00, 1),
            ('00000000F', 'Empleado6','000000006', 1600.00, 1),
            ('00000000G', 'Empleado7','000000007', 1700.00, 1),
            ('00000000H', 'Empleado8','000000008', 1800.00, 1),
            ('00000000I', 'Empleado9','000000009', 1900.00, 1),
            ('00000000J', 'Empleado10','000000010', 2000.00, 1);
            """
        ]
        for sentencia in insterts:
            cursor.execute(sentencia)
        bd.commit()
        print("Datos insertados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()