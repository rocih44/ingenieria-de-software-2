from typing import List, Optional
from app.db.models.usuarioRol import UsuarioRol
from app.db.dbConfig import Session
from app.domain.repositories.usuarioRolRepository import UsuarioRolRepository


class UsuarioRolRepositoryImpl(UsuarioRolRepository):
    def add(self, item: UsuarioRol) -> None:
        with Session() as session:
            session.add(item)
            session.commit()

    def get(self, usuario_id: int, rol_id: int) -> Optional[UsuarioRol]:
        with Session() as session:
            return session.query(UsuarioRol).filter(
                UsuarioRol.usuario_id == usuario_id,
                UsuarioRol.rol_id == rol_id
            ).first()

    def delete(self, usuario_id: int, rol_id: int) -> None:
        with Session() as session:
            ur = session.query(UsuarioRol).filter(
                UsuarioRol.usuario_id == usuario_id,
                UsuarioRol.rol_id == rol_id
            ).first()
            if ur:
                session.delete(ur)
                session.commit()

    def get_all(self) -> List[UsuarioRol]:
        with Session() as session:
            return session.query(UsuarioRol).all()

    def get_roles_by_usuario(self, usuario_id: int) -> List[UsuarioRol]:
        with Session() as session:
            return session.query(UsuarioRol).filter(
                UsuarioRol.usuario_id == usuario_id
            ).all()

    def get_usuarios_by_rol(self, rol_id: int) -> List[UsuarioRol]:
        with Session() as session:
            return session.query(UsuarioRol).filter(
                UsuarioRol.rol_id == rol_id
            ).all()
