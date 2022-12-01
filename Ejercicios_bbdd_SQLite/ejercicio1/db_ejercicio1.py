from sqlite3 import *


def conexion():
    try:
        bd = connect("db_ejercicio1.db")
        return bd
    except OperationalError as error:
        print("Error al abrir:", error)


def onCreate():
    try:
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
        tablas = [
            '''
            CREATE TABLE IF NOT EXISTS "Alumno" (
                "numMatricula"	INTEGER,
                "nombre"	TEXT NOT NULL,
                "fechaNac"	TEXT NOT NULL,
                "telefono"	TEXT,
                PRIMARY KEY("numMatricula" AUTOINCREMENT)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS "Profesor" (
                "idProf"	INTEGER,
                "nifProf"	TEXT NOT NULL,
                "nombre"	TEXT NOT NULL,
                "especialidad"	TEXT,
                "telefono"	TEXT,
                PRIMARY KEY("idProf" AUTOINCREMENT)
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS "Asignatura" (
                "codAsig"	INTEGER,
                "nombre"	TEXT NOT NULL,
                "codProf"	INTEGER,
                PRIMARY KEY("codAsig" AUTOINCREMENT),
                FOREIGN KEY("codProf") REFERENCES "Profesor"("idProf")
            )
            ''',
            '''
            CREATE TABLE IF NOT EXISTS "Alumno_Asignatura" (
                "codAlum"	INTEGER,
                "codAsig"	INTEGER,
                "codAlumAsig"	INTEGER,
                PRIMARY KEY("codAlumAsig" AUTOINCREMENT),
                FOREIGN KEY("codAlum") REFERENCES "Alumno"("numMatricula"),
                FOREIGN KEY("codAsig") REFERENCES "Asignatura"("codAsig")
            )
            '''
        ]
        for tabla in tablas:
            cursor.execute(tabla)
        print("Tablas creadas correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)


def onCreateInsertData():
    try:
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
        insterts = [
            """
            INSERT INTO Alumno
            (nombre, fechaNac, telefono)
            VALUES
            ('Pablo Miguel', '2003-03-20','000000000'),
            ('Marta', '2003-04-25', '000000000'),
            ('Manu', '2002-02-16', '000000000');
            """,
            """
            INSERT INTO Profesor
            (nifProf, nombre, especialidad, telefono)
            VALUES
            ('00000000A', 'Vicente', 'Informática','000000000');
            """,
            """
            INSERT INTO Asignatura
            (nombre, codProf)
            VALUES
            ('Informática', 1);
            """,
            """
            INSERT INTO Alumno_Asignatura
            (codAlum, codAsig)
            VALUES
            (1, 1),
            (2, 1),
            (3, 1);
            """
        ]
        for sentencia in insterts:
            cursor.execute(sentencia)
        bd.commit()
        print("Datos insertados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)