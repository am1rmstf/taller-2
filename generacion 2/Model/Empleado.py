#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persona import Persona

class Empleado(Persona):
    def __init__(self, cedula, nombre, apellido, usuario, clave):
        super().__init__(cedula, nombre, apellido)
        self.usuario = usuario
        self.clave = clave
    
  
    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def clave(self):
        return self.__clave
    @clave.setter
    def clave(self, clave):
        self.__clave = clave
    
    def __str__(self):
        return self.cedula + ' : ' + self.nombre + ' - ' + self.apellido