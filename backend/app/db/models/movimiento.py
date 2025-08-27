# backend/app/db/models/movimiento.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.base import Base

import enum

class TipoMovimiento(str,enum.Enum):
    ingreso = "ingreso"
    egreso = "egreso"
    traslado = "traslado"


class MovimientoORM(Base):
    __tablename__ = "MOVIMIENTO"

    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=False)
    deposito_origen_id = Column(Integer, ForeignKey("deposito.id"), nullable=False)
    deposito_destino_id = Column(Integer, ForeignKey("deposito.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=True)
    cantidad = Column(Integer, nullable=False)
    fecha = Column(DateTime, default=datetime, nullable=False)
    tipo = Column(Enum(TipoMovimiento), nullable=False)
    
    producto = relationship("ProductoORM", back_populates="movimiento")
    deposito = relationship("DepositoORM", back_populates="movimiento")
    usuario = relationship("UsuarioORM", back_populates="movimiento")
