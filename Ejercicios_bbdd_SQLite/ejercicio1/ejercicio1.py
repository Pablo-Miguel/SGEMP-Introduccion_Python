from db_ejercicio1 import *
from sqlite3 import *

# onCreate()
# onCreateInsertData()

print("Se quiere saber el curso escolar en el que cada alumno está matriculado de cada asignatura.")
try:
    bd = connect("db_ejercicio1.db")
    cursor = bd.cursor()
    cursor.execute('''
        SELECT 
            A.nombre, 
            A2.nombre 
        FROM 
            Alumno A 
            JOIN Alumno_Asignatura AA 
            on A.numMatricula = AA.codAlum 
            JOIN Asignatura A2 
            on A2.codAsig = AA.codAsig;
    ''')

    asignaturaAlumno = cursor.fetchall()
    print("+{:-<20}+{:-<20}+".format("", ""))
    print("|{:^20}|{:^20}|".format("Nombre Alumno", "Nombre Asignatura"))
    print("+{:-<20}+{:-<20}+".format("", ""))

    for nombreAlumno, nombreAsig in asignaturaAlumno:
        print("|{:^20}|{:^20}|".format(nombreAlumno, nombreAsig))

    print("+{:-<20}+{:-<20}+".format("", ""))
except OperationalError as error:
    print("Error al abrir:", error)
finally:
    cursor.close()

print("En una asignatura habrá como mínimo 10 y como máximo 25 alumnos.")
try:
    bd = connect("db_ejercicio1.db")
    cursor = bd.cursor()
    cursor.execute('''
        SELECT 
            A.nombre, 
            COUNT(AA.codAlum) 
        FROM 
            Asignatura A 
            JOIN Alumno_Asignatura AA 
            on A.codAsig = AA.codAsig 
        GROUP BY 
            AA.codAsig;
    ''')

    contAlumnos = cursor.fetchall()
    print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
    print("|{:^20}|{:^20}|{:^20}|".format("Nombre asignatura", "Numero de alumnos", "¿Cumple requisitos?"))
    print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))

    for nombre, cont in contAlumnos:
        if(10 <= cont <= 25):
            print("|{:^20}|{:^20}|{:^20}|".format(nombre, cont, "SI"))
        else:
            print("|{:^20}|{:^20}|{:^20}|".format(nombre, cont, "NO"))

    print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
except OperationalError as error:
    print("Error al abrir:", error)
finally:
    cursor.close()

print("Un profesor podrá impartir varias asignaturas.")
try:
    bd = connect("db_ejercicio1.db")
    cursor = bd.cursor()
    cursor.execute('''
        SELECT 
            A.nombre, 
            P.nombre, 
            P.nifProf 
        FROM 
            Profesor P 
        JOIN 
            Asignatura A on P.idProf = A.codProf;
    ''')

    asigProf = cursor.fetchall()
    print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
    print("|{:^20}|{:^20}|{:^20}|".format("Nombre asignatura", "Nombre profesor", "NIF Profesor"))
    print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))

    for nombreAsig, nombreProf, nifProf in asigProf:
        print("|{:^20}|{:^20}|{:^20}|".format(nombreAsig, nombreProf, nifProf))

    print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
except OperationalError as error:
    print("Error al abrir:", error)
finally:
    cursor.close()


def insertarAlumno():
    nombre = input("Inserte nombre del alumno: ")
    fechaNac = input("Inserte fecha naciemiento con formato -> [YY-mm-dd]:")
    tel = input("Introduzca un número de teléfono: ")
    try:
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
        cursor.execute("INSERT INTO Alumno (nombre, fechaNac, telefono) VALUES (?, ?, ?);", (nombre, fechaNac, tel))
        bd.commit()
        cursor.close()
        print("Se ha añadido el alumno correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()


def insertarProfesor():
    nif = input("Inserte nif del profesor: ")
    nombre = input("Inserte nombre del profesor: ")
    especialidad = input("Inserte especialidad del profesor: ")
    tel = input("Introduzca un número de teléfono: ")
    try:
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
        cursor.execute("INSERT INTO Profesor (nifProf, nombre, especialidad, telefono) VALUES (?, ?, ?, ?);", (nif, nombre, especialidad, tel))
        bd.commit()
        cursor.close()
        print("Se ha añadido el profesor correctamente")
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()


def mostarProfesores():
    try:
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
        cursor.execute('''
            SELECT 
                idProf,
                nifProf,
                nombre
            FROM 
                Profesor;
        ''')

        prof = cursor.fetchall()
        print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
        print("|{:^20}|{:^20}|{:^20}|".format("Id profesor", "Nif profesor", "Nombre profesor"))
        print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))

        for idProf, nif, nombre in prof:
            print("|{:^20}|{:^20}|{:^20}|".format(idProf, nif, nombre))

        print("+{:-<20}+{:-<20}+{:-<20}+".format("", "", ""))
    except OperationalError as error:
        print("Error al abrir:", error)
    finally:
        cursor.close()


def eliminarProfesor():
    print("TABLA PROFESORES")
    mostarProfesores()
    id = input("Inserte id del profesor a eliminar: ")
    try:
        bd = connect("db_ejercicio1.db")
        cursor = bd.cursor()
        cursor.execute("DELETE FROM Profesor WHERE idProf=?;", (id))
        bd.commit()
        cursor.close()
        print("Se ha eliminado el profesor correctamente")
    except OperationalError as error:
        print("El profesor está asignado a una clase")
        print("Error al abrir:", error)
    finally:
        cursor.close()

# insertarAlumno()

# insertarProfesor()

# eliminarProfesor()