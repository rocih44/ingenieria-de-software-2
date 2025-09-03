from app.db.models.rol import Rol as RolORM
from .repository import Repository
from typing import List, Optional


class RolRepository(Repository[RolORM]):
    def add(self, item: RolORM) -> None:
        raise NotImplementedError

    def get(self, item_id) -> Optional[RolORM]:
        raise NotImplementedError

    def update(self, item: RolORM) -> None:
        raise NotImplementedError

    def delete(self, item_id) -> None:
        raise NotImplementedError

    def get_all(self) -> List[RolORM]:
        raise NotImplementedError

    def get_by_nombre(self, nombre: str) -> Optional[RolORM]:
        """Permite buscar un rol por nombre"""
        raise NotImplementedError
