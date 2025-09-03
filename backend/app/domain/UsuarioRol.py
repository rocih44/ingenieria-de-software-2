from dataclasses import dataclass, field
from typing import List
from domain.Rol import Rol
from domain.Usuario import Usuario

@dataclass
class UsuarioRol:
    usuario_id: int
    rol_id: int
    roles: List["Rol"] = field(default_factory=list)
    usuarios: List["Usuario"] = field(default_factory=list)

def __ingreso_de_datos__(self):
        if not isinstance(self.usuario_id, int) or not isinstance(self.rol_id, int):
            raise ValueError("usuario_id y rol_id deben ser enteros")