from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")  # Tipo genérico (Producto, Cliente, etc.)

class Repository(ABC, Generic[T]):

    @abstractmethod
    def add(self, item: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, item_id) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: T) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, item_id) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[T]:
        raise NotImplementedError
