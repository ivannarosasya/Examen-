# Clase base Persona (Herencia aplicada)
class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre  # Encapsulamiento: atributo privado
    
    def obtener_nombre(self):  # Encapsulamiento: getter
        return self.__nombre
    
    def actualizar_cuenta(self):  # Polimorfismo: método base
        print(f"Cuenta actualizada para: {self.__nombre}")
    
# Clase Usuario que hereda de Persona
class Usuario(Persona):
    def actualizar_cuenta(self):  # Polimorfismo: sobrescribe el método
        print(f"Cuenta del usuario {self.obtener_nombre()} actualizada.")

# Clase Libro
class Libro:
    def __init__(self, titulo, disponible):
        self.__titulo = titulo  # Encapsulamiento: atributo privado
        self.__disponible = disponible  # Encapsulamiento: atributo privado
    
    def verificar_disponibilidad(self):  # Método para verificar disponibilidad
        return self.__disponible
    
    def obtener_titulo(self):  # Encapsulamiento: getter
        return self.__titulo

# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario  # Encapsulamiento: relación entre clases
        self.libro = libro      # Encapsulamiento: relación entre clases
    
    def realizar_prestamo(self):
        try:
            if self.libro.verificar_disponibilidad():
                print(f"Préstamo realizado para {self.usuario.obtener_nombre()} del libro '{self.libro.obtener_titulo()}'.")
            else:
                raise Exception("El libro no está disponible.")  # Manejo de errores
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores con try-catch
    
    def generar_recibo(self):
        print(f"Recibo generado para {self.usuario.obtener_nombre()} por el libro '{self.libro.obtener_titulo()}'.")

# Ejemplo de uso con entrada de datos desde la terminal
if __name__ == "__main__":
    # Solicitar los datos al usuario
    nombre_usuario = input("Ingrese el nombre del usuario: ")
    titulo_libro = input("Ingrese el título del libro: ")
    disponible = input("¿Está disponible el libro? (Sí/No): ").strip().lower() == "sí"
    
    # Crear objetos
    usuario = Usuario(nombre_usuario)
    libro = Libro(titulo_libro, disponible)
    prestamo = Prestamo(usuario, libro)
    
    # Operaciones
    prestamo.realizar_prestamo()  # Realizar préstamo
    usuario.actualizar_cuenta()  # Actualizar cuenta del usuario
    prestamo.generar_recibo()  # Generar recibo
