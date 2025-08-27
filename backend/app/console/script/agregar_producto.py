from db.models.producto import ProductoORM
from db.session import SessionLocal

db = SessionLocal()
nuevo_producto = ProductoORM(nombre="Producto Ejemplo", sku="0001", descripcion="Test", stock=10, stock_minimo=2)
db.add(nuevo_producto)
db.commit()
db.close()
print("Producto insertado correctamente")