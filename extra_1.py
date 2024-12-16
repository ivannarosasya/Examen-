# Clase base Persona para herencia
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo público

    def obtener_nombre(self):
        return self.nombre

# Clase Informes (para manejo de pedidos)
class Informes:
    def __init__(self, datos_pedido):
        self.datos_pedido = datos_pedido  # Atributo privado

    def validar_datos(self):
        """Valida que los datos del pedido no estén vacíos."""
        if not self.datos_pedido:
            raise ValueError("Error: El pedido no puede estar vacío.")  # Manejo de errores (si los datos están vacíos)
        return True

    def emitir_comprobante(self):
        """Devuelve un comprobante del pedido."""
        return f"Comprobante: {self.datos_pedido}"


# Clase Pedidos (hereda de Persona)
class Pedidos(Persona):
    def __init__(self, id_pedido, descripcion, nombre_cliente):
        super().__init__(nombre_cliente)  # Hereda el nombre del cliente de la clase Persona
        self.id_pedido = id_pedido  # Atributo público (encapsulamiento)
        self.descripcion = descripcion  # Atributo público (encapsulamiento)

    def crear_pedido(self):
        """Crea un pedido con validación de datos."""
        informe = Informes(self.descripcion)  # Se crea un objeto de la clase Informes
        if informe.validar_datos():  # Se llama al método de validación de la clase Informes
            return f"Pedido creado con ID {self.id_pedido}: {self.descripcion}"

    def preparar_plato(self):
        """Simula la preparación del plato."""
        return f"Preparando el plato: {self.descripcion}"


# Clase ControlPedidos (maneja la lista de pedidos)
class ControlPedidos:
    def __init__(self):
        self.lista_pedidos = []  # Lista para guardar los pedidos (encapsulamiento)

    def agregar_pedido(self, pedido):
        """Añade un pedido a la lista si no está duplicado."""
        for p in self.lista_pedidos:
            if p.id_pedido == pedido.id_pedido:
                raise ValueError("Error: El pedido ya existe.")  # Manejo de errores (control de duplicados)
        self.lista_pedidos.append(pedido)
        return "Pedido añadido al control correctamente."


# Clase Cliente (hereda de Persona)
class Cliente(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)  # Hereda el nombre de la clase Persona

    def realizar_pedido(self, id_pedido, descripcion):
        """Cliente realiza un pedido."""
        try:
            pedido = Pedidos(id_pedido, descripcion, self.nombre)  # Se crea un objeto de la clase Pedidos
            print(pedido.crear_pedido())  # Llama al método de creación de pedido
            print(pedido.preparar_plato())  # Llama al método de preparación de plato
            return pedido
        except ValueError as e:
            print(e)  # Manejo de errores (captura de excepciones en el pedido)

    def recibir_comprobante(self, pedido):
        """Cliente recibe un comprobante."""
        informe = Informes(pedido.descripcion)  # Se crea un objeto de la clase Informes
        print(informe.emitir_comprobante())  # Llama al método para emitir el comprobante


# Programa principal
if __name__ == "__main__":
    try:
        # Cliente realiza un pedido
        print("Cliente: Ivanna Rosas Yañez")
        cliente1 = Cliente("Ivanna Rosas Yañez")  # Se crea un objeto de la clase Cliente
        pedido1 = cliente1.realizar_pedido(1, "Pizza Margarita")  # Se realiza el pedido

        # Control de pedidos
        control = ControlPedidos()  # Se crea un objeto de la clase ControlPedidos
        print(control.agregar_pedido(pedido1))  # Agrega el pedido a la lista

        # Cliente recibe el comprobante
        cliente1.recibir_comprobante(pedido1)  # Cliente recibe su comprobante

    except Exception as e:
        print(f"Error: {e}")  # Manejo de errores (captura de cualquier excepción global)
