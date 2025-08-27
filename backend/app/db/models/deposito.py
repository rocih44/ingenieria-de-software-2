# backend/app/db/models/deposito.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.base import Base


class DepositoORM(Base):
    __tablename__ = "DEPOSITO"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    ubicacion = Column(String(300), nullable=True) 

    movimientos = relationship("MovimientoORM", back_populates="deposito")
