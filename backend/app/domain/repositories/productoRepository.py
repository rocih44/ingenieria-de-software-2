# En esta clase, implemento los métodos específicos de producto, sumado a los genéricos de Repository

from app.db.models.Producto import Producto as ProductoORM #Lo dejo así para acordarme que es la clase de la BBDD
from .repository import Repository
from typing import List, Optional

class ProductoRepository(Repository[ProductoORM]):
    def add(self, item: ProductoORM) -> None:
        raise NotImplementedError

    def get(self, item_id) -> Optional[ProductoORM]:
        raise NotImplementedError

    def update(self, item: ProductoORM) -> None:
        raise NotImplementedError

    def delete(self, item_id) -> None:
        raise NotImplementedError

    def get_all(self) -> List[ProductoORM]:
        raise NotImplementedError

    def get_by_sku(self, sku: str) -> Optional[ProductoORM]:
        raise NotImplementedError