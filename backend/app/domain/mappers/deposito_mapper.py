from app.db.models.deposito import Deposito as DepositoORM
from app.domain.Deposito import Deposito as DepositoDomain


def deposito_orm_to_domain(deposito_orm: DepositoORM) -> DepositoDomain:
    return DepositoDomain(
        id=deposito_orm.id,
        nombre=deposito_orm.nombre,
        ubicacion=deposito_orm.ubicacion,
        # Movimientos solo referenciados, no se cargan en cascada acá
        movimientos_origen=list(deposito_orm.movimientos_origen),
        movimientos_destino=list(deposito_orm.movimientos_destino),
    )


def deposito_domain_to_orm(deposito_domain: DepositoDomain) -> DepositoORM:
    return DepositoORM(
        id=deposito_domain.id,
        nombre=deposito_domain.nombre,
        ubicacion=deposito_domain.ubicacion,
        # Movimientos solo referenciados, no se crean en cascada acá
        movimientos_origen=list(deposito_domain.movimientos_origen),
        movimientos_destino=list(deposito_domain.movimientos_destino),
    )
