from app.db.models.movimiento import Movimiento as MovimientoORM
from app.domain.Movimiento import Movimiento as MovimientoDomain

def movimiento_orm_to_domain(movimiento_orm: MovimientoORM) -> MovimientoDomain:
    return MovimientoDomain(
        id=movimiento_orm.id,
        producto_id=movimiento_orm.producto_id,
        deposito_origen_id=movimiento_orm.deposito_origen_id,
        deposito_destino_id=movimiento_orm.deposito_destino_id,
        usuario_id=movimiento_orm.usuario_id,
        cantidad=movimiento_orm.cantidad,
        fecha=movimiento_orm.fecha,
        tipo=movimiento_orm.tipo,
        producto=movimiento_orm.producto,
        deposito_origen=movimiento_orm.deposito_origen,
        deposito_destino=movimiento_orm.deposito_destino,
        usuario=movimiento_orm.usuario
    )

def movimiento_domain_to_orm(movimiento_domain: MovimientoDomain) -> MovimientoORM:
    return MovimientoORM(
        id=movimiento_domain.id,
        producto_id=movimiento_domain.producto_id,
        deposito_origen_id=movimiento_domain.deposito_origen_id,
        deposito_destino_id=movimiento_domain.deposito_destino_id,
        usuario_id=movimiento_domain.usuario_id,
        cantidad=movimiento_domain.cantidad,
        fecha=movimiento_domain.fecha,
        tipo=movimiento_domain.tipo
    )
