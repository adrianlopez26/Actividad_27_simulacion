'''
Crear estas clases
Define los atributos, métodos, constructores... que consideres
necesarios.

cursos:id,nombre, creditos, añosdeestudio
alumno:id, nombre, email
matricula:idmatricula, fechamatricula, idalumno, idcurso

Necesitamos.
mostrar la ficha del curso
mostrar la ficha de alumno
alumno1 se matricula en un curso
alumno2 se matricula en dos cursos
mostrar los datos de matrículo
reto*:método que muestra las mátriculas realizadas en mi centro
'''

from colorama import Fore, Style

class Curso:
    def __init__(self, id, nombre, creditos, a_de_estudio):
        self.id = id
        self.nombre = nombre
        self.creditos = creditos
        self.a_de_estudio = a_de_estudio

    def mostrar_ficha(self):
        print(f"{Fore.BLUE}Ficha del curso {self.nombre}:{Style.RESET_ALL}")
        print(f"{Fore.BLUE}ID: {self.id}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Créditos: {self.creditos}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}Años de estudio: {self.a_de_estudio}{Style.RESET_ALL}")
        print("\n")

class Alumno:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def mostrar_ficha(self):
        print(f"{Fore.CYAN}Ficha del alumno {self.nombre}:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}ID: {self.id}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Email: {self.email}{Style.RESET_ALL}")
        print("\n")

class Matricula:

    matriculas = []

    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso
        Matricula.matriculas.append(self)

    @staticmethod
    def mostrar_datos_matricula():
        print(f"{Fore.MAGENTA}Datos de Matrícula:{Style.RESET_ALL}")
        for matricula in Matricula.matriculas:
            print(f"{Fore.MAGENTA}ID Matrícula: {matricula.id_matricula}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}Fecha de Matrícula: {matricula.fecha_matricula}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}ID Alumno: {matricula.id_alumno}{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}ID Curso: {matricula.id_curso}{Style.RESET_ALL}")
            print("\n")

    @staticmethod
    def mostrar_matriculas_centro():
        print(f"{Fore.GREEN}Matrículas realizadas en el centro:{Style.RESET_ALL}")
        for matricula in Matricula.matriculas:
            print(f"{Fore.GREEN}ID Matrícula: {matricula.id_matricula}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}Fecha de Matrícula: {matricula.fecha_matricula}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}ID Alumno: {matricula.id_alumno}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}ID Curso: {matricula.id_curso}{Style.RESET_ALL}")
            print("\n")

# Crear instancias de las clases
curso1 = Curso(1, "Introducción a Python", 3, 1)
curso2 = Curso(2, "Programación Avanzada", 4, 2)

alumno1 = Alumno(1, "Juan Perez", "juan@example.com")
alumno2 = Alumno(2, "Maria Rodriguez", "maria@example.com")

matricula1 = Matricula(1, "2023-01-01", alumno1.id, curso1.id)
matricula2 = Matricula(2, "2023-01-15", alumno2.id, curso2.id)
matricula3 = Matricula(3, "2023-02-01", alumno2.id, curso1.id)

# Mostrar fichas
curso1.mostrar_ficha()
curso2.mostrar_ficha()

alumno1.mostrar_ficha()
alumno2.mostrar_ficha()

# Mostrar datos de matrícula
Matricula.mostrar_datos_matricula()

# Mostrar matrículas del centro
Matricula.mostrar_matriculas_centro()
