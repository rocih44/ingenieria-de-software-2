from .repository import Repository
from typing import List, Optional
from app.db.models.movimiento import Movimiento as MovimientoORM

class MovimientoRepository(Repository[MovimientoORM]):

    def add(self, movimiento: MovimientoORM) -> None:
        raise NotImplementedError("El método agregar debe ser implementado")

    def get_by_id(self, movimiento_id: int) -> Optional[MovimientoORM]:
        raise NotImplementedError("El método obtener_por_id debe ser implementado")

    def update(self, movimiento: MovimientoORM) -> MovimientoORM:
        raise NotImplementedError("El método actualizar debe ser implementado")

    def delete(self, movimiento_id: int) -> None:
        raise NotImplementedError("El método eliminar debe ser implementado")

    def get_all(self) -> List[MovimientoORM]:
        raise NotImplementedError("El método listar debe ser implementado")

    def get_by_user(self, usuario_id: int) -> List[MovimientoORM]:
        raise NotImplementedError("El método obtener_por_usuario debe ser implementado")
