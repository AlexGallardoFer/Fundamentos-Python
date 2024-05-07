###################################################
# Clases - Herencia                               #
###################################################

from datetime import datetime

class Alumno:
    """Clase demostración del curso de Python"""

    # Variables de la clase
    Nombre = None
    Apellido1 = None
    Apellido2 = None
    FechaNacimiento = None

    # Constructor del objeto, se ejecuta al crear (instanciar) el objeto.
    # self es una variable que contiene el propio objeto
    def __init__(self, nombre, apellido1, apellido2 = "") -> None:
        self.Nombre = nombre
        self.Apellido1 = apellido1
        self.Apellido2 = apellido2

    # Diversas funciones de la clase Alumno
    def getNombreCompleto(self) -> str:
        return f"{self.Nombre} {self.Apellido1} {self.Apellido2}"
    
    def getEdad(self) -> int:
        try:
                resultado = datetime.now().date() - self.FechaNacimiento
                return resultado.days // 365
        except:
            return -1

    
    def setFechaNacimiento(self, fecha) -> bool:
        try:
            if len(fecha) == 10:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%Y").date()
            elif len(fecha) == 8:
                self.FechaNacimiento = datetime.strptime(fecha, "%d-%m-%y").date()
            else:
                return False
            
            return True
        except:
            return False


# Definición de la clase ESTUDIANTE que hereda de la clase Alumno
class Estudiante(Alumno):
    # Añadimos nuevas propiedades
    Curso = None

    # Sobreescribimos el constructor
    def __init__(self, nombre, apellido1, curso) -> None:
        # self.Nombre = nombre
        # self.Apellido1 = apellido1
        # self.Apellido2 = ""
        
        # Las líneas superiores no son necesarioas ya que es lógica escrita en la
        # clase base y podemos ejecutarla utilizando la función super()
        super().__init__(nombre, apellido1)

        # Añadimos la nueva funcionalidad al constructor
        self.Curso = curso

    # Sobreescribimos el método getNombreCompleto()
    def getNombreCompleto(self) -> str:
        # return f"{self.Nombre} {self.Apellido1} {self.Apellido2} - Curso: {self.Curso}"
        return f"{super().getNombreCompleto()} - Curso: {self.Curso}"
    
    # Añadimos nuevos métodos
    def test(self):
        return "Función test"

a = Alumno("Ana", "Sanz")
print(a.getNombreCompleto())
# a.test()

e = Estudiante("Borja", "Cabeza", "1A")
print(e.getNombreCompleto())
print(e.test())