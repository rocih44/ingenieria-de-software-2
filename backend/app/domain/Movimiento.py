from dataclasses import dataclass
from datetime import datetime

from producto import Producto
from Deposito import Deposito
from Usuario import Usuario
from app.db.models.movimiento import TipoMovimiento 

@dataclass
class Movimiento:
    id: int
    producto_id: int
    deposito_origen_id: int
    deposito_destino_id: int
    usuario_id: int
    cantidad: int
    fecha: datetime
    tipo: TipoMovimiento
    producto: Producto
    deposito_origen: Deposito
    deposito_destino: Deposito
    usuario: Usuario

    def es_entrada(self) -> bool:
        return self.tipo == "entrada"   

    def es_salida(self) -> bool:
        return self.tipo == "salida"    

    def validar_cantidad(self):
        if self.cantidad <= 0:
            raise ValueError("La cantidad debe ser un número positivo")

    def validar_fechas(self):
        if self.fecha > datetime.now():
            raise ValueError("La fecha del movimiento no puede ser en el futuro")

    def validar_depositos(self):
        if self.deposito_origen_id == self.deposito_destino_id:
            raise ValueError("El depósito de origen y destino no pueden ser el mismo")

    def validar_producto(self):
        if not self.producto.disponible():
            raise ValueError("El producto no está disponible en stock")