from dataclasses import dataclass, field
from datetime import datetime
from typing import List
from domain.Usuario import Usuario

@dataclass

class Rol:
    id:int
    nombre:str
    usuarios: List["Usuario"] =  field(default_factory=list)


    def agregar_usuario(self, usuario: "Usuario"):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            usuario.agregar_rol(self)  # Mantener la relación bidireccional
        else:
            raise ValueError("El usuario ya está asignado al rol")


    def eliminar_usuario(self, usuario: "Usuario"):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            usuario.eliminar_rol(self)  # Mantener la relación bidireccional
        else:
            raise ValueError("El usuario no está asignado al rol")