from sqlite3 import *


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
                    "nifProf"	TEXT NOT NULL UNIQUE,
                    "nombre"	TEXT NOT NULL,
                    "especialidad"	TEXT,
                    "telefono"	TEXT UNIQUE,
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


def conexion():
    try:
        onCreate()
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
    except OperationalError as error:
        print("Error al abrir:", error)


def onCreateInsertData():
    try:
        bd = connect("libros.db")
        cursor = bd.cursor()
        libros = [
            """
                INSERT INTO Alumno
                (nombre, nombre, telefono)
                VALUES
                ('Pablo Miguel', '20-03-2003','000000000'),
                ('Marta', '25-05-2003', '000000000'),
                ('Manu', '16-02-2002', '000000000');
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
                (1, 1);
            """
        ]
        for sentencia in libros:
            cursor.execute(sentencia);
        bd.commit()  # Guardamos los cambios al terminar el ciclo
        print("Libros insertados correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)