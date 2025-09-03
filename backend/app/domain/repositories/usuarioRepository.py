from app.db.models.usuario import Usuario as UsuarioORM
from .repository import Repository
from typing import List, Optional


class UsuarioRepository(Repository[UsuarioORM]):
    def add(self, item: UsuarioORM) -> None:
        raise NotImplementedError

    def get(self, item_id) -> Optional[UsuarioORM]:
        raise NotImplementedError

    def update(self, item: UsuarioORM) -> None:
        raise NotImplementedError

    def delete(self, item_id) -> None:
        raise NotImplementedError

    def get_all(self) -> List[UsuarioORM]:
        raise NotImplementedError

    def get_by_email(self, email: str) -> Optional[UsuarioORM]:
        raise NotImplementedError
