from pydantic import BaseModel, Field
from typing import List

class Movimiento(BaseModel):  # Para que pase las pruebas, después se puede eliminar
    tipo: str
    cantidad: int

class Producto(BaseModel):
    id: int
    nombre: str
    sku: str
    descripcion: str
    stock: int
    movimientos: List[Movimiento] = Field(default_factory=list)  # Lista de movimientos del producto, por defecto, asigna una lista vacía