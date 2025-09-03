from app.domain.repositories.productoRepository import ProductoRepository
from typing import List, Optional
from app.db.models.Producto import Producto
from app.db.dbConfig import Session

class ProductoRepositoryImpl(ProductoRepository):
    def add(self, item: Producto) -> None:
        with Session() as session:
            session.add(item)
            session.commit()

    def get(self, item_id) -> Optional[Producto]:
        with Session() as session:
            return session.get(Producto, item_id)

    def update(self, item: Producto) -> None:
        with Session() as session:
            session.merge(item)
            session.commit()

    def delete(self, item_id) -> None:
        with Session() as session:
            item = session.get(Producto, item_id) #Primero chequeo si existe
            if item:
                session.delete(item)
                session.commit()

    def get_all(self) -> List[Producto]:
        with Session() as session:
            return session.query(Producto).all()

    def get_by_sku(self, sku: str) -> Optional[Producto]:
        with Session() as session:
            return session.query(Producto).filter(Producto.sku == sku).first()