from app.domain.repositories.rolRepository import RolRepository
from typing import List, Optional
from app.db.models.rol import Rol
from app.db.dbConfig import Session


class RolRepositoryImpl(RolRepository):
    def add(self, item: Rol) -> None:
        with Session() as session:
            session.add(item)
            session.commit()

    def get(self, item_id) -> Optional[Rol]:
        with Session() as session:
            return session.get(Rol, item_id)

    def update(self, item: Rol) -> None:
        with Session() as session:
            session.merge(item)
            session.commit()

    def delete(self, item_id) -> None:
        with Session() as session:
            item = session.get(Rol, item_id)
            if item:
                session.delete(item)
                session.commit()

    def get_all(self) -> List[Rol]:
        with Session() as session:
            return session.query(Rol).all()

    def get_by_nombre(self, nombre: str) -> Optional[Rol]:
        with Session() as session:
            return session.query(Rol).filter(Rol.nombre == nombre).first()
