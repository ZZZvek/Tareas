from typing import List
from CL_Producto import Producto

class Inventario:
    def __init__(self):
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def calcular_valor_inventario(self) -> float:
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def mostrar_inventario(self) -> str:

        detalles = "Inventario de Productos:\n\n"

        for producto in self.productos:
            detalles += producto.mostrar_detalles() + "\n"
        valor_total = self.calcular_valor_inventario()
        detalles += f"\nValor total del inventario: ${valor_total:.2f}"
        
        return detalles