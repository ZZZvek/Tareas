class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_valor_total(self) -> float:
        return self.precio * self.cantidad

    def mostrar_detalles(self) -> str:

        valor_total = self.calcular_valor_total()
        
        return (f"Producto: {self.nombre}\n"
                f"Precio: ${self.precio:.2f}\n"
                f"Cantidad en inventario: {self.cantidad}\n"
                f"Valor total en inventario: ${valor_total:.2f}\n")