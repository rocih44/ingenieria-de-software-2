from app.domain.producto import Producto as ProductoDomain
from app.db.models.Producto import Producto as ProductoORM

def domain_to_orm(producto_domain: ProductoDomain) -> ProductoORM:
    return ProductoORM(
        id=producto_domain.id,
        nombre=producto_domain.nombre,
        sku= producto_domain.sku,
        descripcion=producto_domain.descripcion,
        stock=producto_domain.stock,
        stock_minimo=producto_domain.stock_minimo
    )

def orm_to_domain(producto_orm: ProductoORM) -> ProductoDomain:
    return ProductoDomain(
        id=producto_orm.id,
        nombre=producto_orm.nombre,
        sku= producto_orm.sku,
        descripcion=producto_orm.descripcion,
        stock=producto_orm.stock,
        stock_minimo=producto_orm.stock_minimo
    )
