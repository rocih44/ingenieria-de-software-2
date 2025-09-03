from app.db.models.deposito import Deposito as DepositoORM
from .repository import Repository
from typing import List, Optional


class DepositoRepository(Repository[DepositoORM]):
    def add(self, item: DepositoORM) -> None:
        raise NotImplementedError

    def get(self, item_id) -> Optional[DepositoORM]:
        raise NotImplementedError

    def update(self, item: DepositoORM) -> None:
        raise NotImplementedError

    def delete(self, item_id) -> None:
        raise NotImplementedError

    def get_all(self) -> List[DepositoORM]:
        raise NotImplementedError

    def get_by_nombre(self, nombre: str) -> Optional[DepositoORM]:
        """Permite buscar un depósito por nombre"""
        raise NotImplementedError

    def get_by_ubicacion(self, ubicacion: str) -> List[DepositoORM]:
        """Permite listar depósitos en una ubicación"""
        raise NotImplementedError
