from app.db.models.usuarioRol import UsuarioRol as UsuarioRolORM
from .repository import Repository
from typing import List, Optional


class UsuarioRolRepository(Repository[UsuarioRolORM]):
    def add(self, item: UsuarioRolORM) -> None:
        raise NotImplementedError

    def get(self, usuario_id: int, rol_id: int) -> Optional[UsuarioRolORM]:
        """Buscar una relación específica usuario-rol"""
        raise NotImplementedError

    def delete(self, usuario_id: int, rol_id: int) -> None:
        """Eliminar la relación usuario-rol"""
        raise NotImplementedError

    def get_all(self) -> List[UsuarioRolORM]:
        raise NotImplementedError

    def get_roles_by_usuario(self, usuario_id: int) -> List[UsuarioRolORM]:
        """Obtener todos los roles asociados a un usuario"""
        raise NotImplementedError

    def get_usuarios_by_rol(self, rol_id: int) -> List[UsuarioRolORM]:
        """Obtener todos los usuarios asociados a un rol"""
        raise NotImplementedError
