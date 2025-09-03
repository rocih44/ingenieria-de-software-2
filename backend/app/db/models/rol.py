from typing import List
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.db.models.usuarioRol import UsuarioRol

class Base(DeclarativeBase):
     pass   

class Rol(Base):
    __tablename__ = "rol"    

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    
    usuarios_roles: Mapped[List["UsuarioRol"]] = relationship("UsuarioRol", back_populates="rol")