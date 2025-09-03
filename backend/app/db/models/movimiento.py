from typing import  List
from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Enum as SqlEnum

from app.db.models.Producto import Producto
from app.db.models.deposito import Deposito
from app.db.models.usuario import Usuario


class TipoMovimiento(str,SqlEnum):
    ENTRADA = "entrada"
    SALIDA = "salida"
# clase que define los tipos de movimiento posibles en el sistema.

class Base(DeclarativeBase):
     pass

class Movimiento(Base):
    __tablename__ = "movimiento"    

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    deposito_origen_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"), nullable=False)
    deposito_destino_id: Mapped[int] = mapped_column(ForeignKey("depositos.id"), nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=False)
    cantidad: Mapped[int] = mapped_column(Integer, nullable=False)
    fecha: Mapped[DateTime] = mapped_column(DateTime, default=DateTime.now)
    tipo: Mapped[TipoMovimiento] = mapped_column(SqlEnum(TipoMovimiento), nullable=False) 

    # Relaciones
    producto: Mapped[Producto] = relationship(back_populates="movimientos")
    deposito_origen: Mapped["Deposito"] = relationship(back_populates="movimientos_origen",foreign_keys=[deposito_origen_id])
    deposito_destino: Mapped["Deposito"] = relationship(back_populates="movimientos_destino",foreign_keys=[deposito_destino_id])
    usuario: Mapped["Usuario"] = relationship(back_populates="movimientos")