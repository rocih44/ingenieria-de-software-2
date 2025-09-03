from typing import Optional, List
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.db.models.movimiento import Movimiento

class Base(DeclarativeBase):
     pass

class Producto(Base):
    __tablename__ = "producto"    

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    sku: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    descripcion: Mapped[Optional[str]] = mapped_column(String(200))
    stock: Mapped[int] = mapped_column(Integer, default=0)
    stock_minimo: Mapped[int] = mapped_column(Integer, default=0)
    
    movimiento: Mapped[List["Movimiento"]] = relationship(back_populates="producto") 
    ## Permite establecer la clase más adelante en el codigo, no da error de referencia circular. Relación bidireccional con Movimiento, back_populates indica el atributo en la clase Movimiento que referencia a Producto.
