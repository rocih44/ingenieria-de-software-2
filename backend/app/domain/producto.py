from dataclasses import dataclass, field
from typing import List

@dataclass
class Producto:
    
    id: int
    nombre: str 
    sku: str 
    descripcion: str
    stock: int 
    stock_minimo: int 
    movimientos: List["Movimiento"] = field(default_factory=list)
    """Linea de arriba permite establecer la clase más adelante en el codigo"""

    def reducir_stock(self, cantidad: int):
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad

    def aumentar_stock(self, cantidad: int):
        self.stock += cantidad

    def disponible(self) -> bool:
        return self.stock > 0
    
    def stock_mayor_a_minimo(self) -> bool:
        return self.stock >= self.stock_minimo
    
    def stock_menor_a_minimo(self) -> bool:
        return self.stock <= self.stock_minimo