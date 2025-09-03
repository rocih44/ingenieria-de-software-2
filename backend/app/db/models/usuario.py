from typing import Optional, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.db.models.usuarioRol import UsuarioRol
from app.db.models.movimiento import Movimiento

class Base(DeclarativeBase):
     pass   

class Usuario(Base):
    __tablename__ = "usuario"    

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)

    usuarios_roles: Mapped[List["UsuarioRol"]] = relationship("UsuarioRol", back_populates="usuario")
    movimiento: Mapped[List["Movimiento"]] = relationship(back_populates="usuario")