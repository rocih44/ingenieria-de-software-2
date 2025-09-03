from dataclasses import dataclass, field
from typing import List
from domain.Rol import Rol
from domain.Movimiento import Movimiento

@dataclass

class Usuario:

    id: int
    nombre: str
    email: str
    hashed_password: str
    roles: List["Rol"] = field(default_factory=list)
    movimientos: List["Movimiento"] = field(default_factory=list)

    def agregar_rol(self, rol: "Rol"):
        if rol not in self.roles:
            self.roles.append(rol)
            rol.agregar_usuario(self)  # Mantener la relación bidireccional
        else:
            raise ValueError("El rol ya está asignado al usuario")

    def eliminar_rol(self, rol: "Rol"):
        if rol in self.roles:
            self.roles.remove(rol)
            rol.eliminar_usuario(self)  # Mantener la relación bidireccional
        else:
            raise ValueError("El rol no está asignado al usuario")

    def agregar_movimiento(self, movimiento: "Movimiento"): 

        if movimiento not in self.movimientos:
            self.movimientos.append(movimiento)
        else:
            raise ValueError("El movimiento ya está asignado al usuario")

    def eliminar_movimiento(self, movimiento: "Movimiento"):
        if movimiento in self.movimientos:
            self.movimientos.remove(movimiento)
        else:
            raise ValueError("El movimiento no está asignado al usuario")