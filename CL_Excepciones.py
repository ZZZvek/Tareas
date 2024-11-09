class ProductoInvalidoException(Exception):
    def __init__(self, mensaje="El nombre del producto no puede estar vacío o ser nulo."):
        super().__init__(mensaje)

class PrecioInvalidoException(Exception):
    def __init__(self, mensaje="El precio del producto debe ser mayor que cero."):
        super().__init__(mensaje)

class CantidadInvalidaException(Exception):
    def __init__(self, mensaje="La cantidad del producto no puede ser negativa."):
        super().__init__(mensaje)