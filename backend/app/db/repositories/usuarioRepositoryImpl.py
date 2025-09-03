from app.domain.repositories.usuarioRepository import UsuarioRepository
from typing import List, Optional
from app.db.models.usuario import Usuario
from app.db.dbConfig import Session


class UsuarioRepositoryImpl(UsuarioRepository):
    def add(self, item: Usuario) -> None:
        with Session() as session:
            session.add(item)
            session.commit()

    def get(self, item_id) -> Optional[Usuario]:
        with Session() as session:
            return session.get(Usuario, item_id)

    def update(self, item: Usuario) -> None:
        with Session() as session:
            session.merge(item)
            session.commit()

    def delete(self, item_id) -> None:
        with Session() as session:
            item = session.get(Usuario, item_id)
            if item:
                session.delete(item)
                session.commit()

    def get_all(self) -> List[Usuario]:
        with Session() as session:
            return session.query(Usuario).all()

    def get_by_email(self, email: str) -> Optional[Usuario]:
        with Session() as session:
            return session.query(Usuario).filter(Usuario.email == email).first()
