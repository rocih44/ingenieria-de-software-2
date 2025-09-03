from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column, relationship
from app.db.models.usuario import Usuario
from app.db.models.rol import Rol

class Base(DeclarativeBase):
     pass   

class UsuarioRol(Base):
    __tablename__ = "usuario_roles"

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)
    rol_id: Mapped[int] = mapped_column(ForeignKey("rol.id"), nullable=False)

    usuario: Mapped["Usuario"] = relationship(back_populates="usuarios_roles")
    rol: Mapped["Rol"] = relationship(back_populates="usuarios_roles")