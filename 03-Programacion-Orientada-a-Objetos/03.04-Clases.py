###################################################
# Clases                                          #
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




demo = Alumno("Borja", "Cabeza", "Rozas")

print(demo.getNombreCompleto())

if demo.setFechaNacimiento("12-03-1999"):
    print(f"Edad: {demo.getEdad()} años")


demo2 = Alumno("Ana", "Sanchez")

print(demo2.getNombreCompleto())

if demo2.setFechaNacimiento("12-03-1965"):
    print(f"Edad: {demo2.getEdad()} años")


alumnos = [Alumno("Ana", "Sánchez"), Alumno("Roberto", "Sánchez"), Alumno("Borja", "Sanz"), Alumno("Alfonso", "Perez")]
for alumno in alumnos:
    print(f"Alumno: {alumno.getNombreCompleto()}")