from app.domain.repositories.depositoRepository import DepositoRepository
from typing import List, Optional
from app.db.models.deposito import Deposito
from app.db.dbConfig import Session


class DepositoRepositoryImpl(DepositoRepository):
    def add(self, item: Deposito) -> None:
        with Session() as session:
            session.add(item)
            session.commit()

    def get(self, item_id) -> Optional[Deposito]:
        with Session() as session:
            return session.get(Deposito, item_id)

    def update(self, item: Deposito) -> None:
        with Session() as session:
            session.merge(item)
            session.commit()

    def delete(self, item_id) -> None:
        with Session() as session:
            item = session.get(Deposito, item_id)
            if item:
                session.delete(item)
                session.commit()

    def get_all(self) -> List[Deposito]:
        with Session() as session:
            return session.query(Deposito).all()

    def get_by_nombre(self, nombre: str) -> Optional[Deposito]:
        with Session() as session:
            return session.query(Deposito).filter(Deposito.nombre == nombre).first()

    def get_by_ubicacion(self, ubicacion: str) -> List[Deposito]:
        with Session() as session:
            return session.query(Deposito).filter(Deposito.ubicacion == ubicacion).all()
