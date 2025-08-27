from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class UsuarioRolORM(Base):
    __tablename__ = "USUARIO_ROL"

    usuario_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    rol_id= Column(Integer, ForeignKey("rol.id"), nullable=False)

    usuarios = relationship("UsuarioORM", back_populates="usuario_rol")
    rol = relationship("RolORM", back_populates="usuario_rol")

