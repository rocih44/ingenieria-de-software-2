from app.db.models.rol import Rol as RolORM
from app.domain.Rol import Rol as RolDomain


def rol_orm_to_domain(rol_orm: RolORM) -> RolDomain:
    return RolDomain(
        id=rol_orm.id,
        nombre=rol_orm.nombre,
        # La relación con usuarios se puede mapear después si necesitás
        usuarios=[]
    )


def rol_domain_to_orm(rol_domain: RolDomain) -> RolORM:
    return RolORM(
        id=rol_domain.id,
        nombre=rol_domain.nombre,
        # La relación con usuarios_roles se maneja aparte
    )
