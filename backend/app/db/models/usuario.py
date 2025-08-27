from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class UsuarioORM(Base):
    __tablename__ = "USUARIO"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255), unique=True, nullable=True)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)

    usuario_rol= relationship("UsuarioRolORM", back_populates="usuario")
    movimiento = relationship("MovimientoORM", back_populates="usuario")
