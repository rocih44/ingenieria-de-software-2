from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class RolORM(Base):
    __tablename__ = "ROL"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    usuario_rol = relationship("UsuarioRolORM", back_populates="rol")
