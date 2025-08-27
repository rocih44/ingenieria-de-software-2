from app.db.base import Base
from app.db.engine import engine

from app.db.models.producto import ProductoORM
from app.db.models.deposito import DepositoORM
from app.db.models.movimiento import MovimientoORM
from app.db.models.rol import RolORM
from app.db.models.usuario import UsuarioORM

def create_db_and_tables():
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    create_db_and_tables()