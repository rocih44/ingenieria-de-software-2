from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class ProductoORM (Base):
    __tablename__= "PRODUCTO"

    id = Column(Integer, primary_key=True) 
    nombre = Column(String (255), nullable=False)
    sku= Column (String (255))
    stock= Column (Integer, default = 0)
    stock_minimo= Column (Integer, default= 5)
    descripcion= Column (String (500))

    movimiento = relationship("MovimientoORM", back_populates="producto")









