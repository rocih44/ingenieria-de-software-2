from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.db.models.movimiento import Movimiento

class Base(DeclarativeBase):
     pass   

class Deposito(Base):
    __tablename__ = "deposito"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    ubicacion: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relación bidireccional con Movimiento, back_populates indica el atributo en la clase Movimiento que referencia a Deposito.
    movimientos_origen: Mapped[List["Movimiento"]] = relationship(back_populates="deposito_origen", foreign_keys="[Movimiento.deposito_origen_id]")
    movimientos_destino: Mapped[List["Movimiento"]] = relationship(back_populates="deposito_destino", foreign_keys="[Movimiento.deposito_destino_id]")    