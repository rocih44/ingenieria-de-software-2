from app.db.models.usuarioRol import UsuarioRol as UsuarioRolORM
from app.domain.UsuarioRol import UsuarioRol as UsuarioRolDomain


def usuariorol_orm_to_domain(ur_orm: UsuarioRolORM) -> UsuarioRolDomain:
    return UsuarioRolDomain(
        usuario_id=ur_orm.usuario_id,
        rol_id=ur_orm.rol_id,
        roles=[],
        usuarios=[]
    )


def usuariorol_domain_to_orm(ur_domain: UsuarioRolDomain) -> UsuarioRolORM:
    return UsuarioRolORM(
        usuario_id=ur_domain.usuario_id,
        rol_id=ur_domain.rol_id
    )
