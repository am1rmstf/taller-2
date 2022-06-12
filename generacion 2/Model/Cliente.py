#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persona import Persona

class Cliente(Persona):
    def __init__(self,cedula, nombre, apellido, domicilio):
       super().__init__(cedula, nombre, apellido)   
       self.domicilio = domicilio

    @property
    def domicilio(self):
        return self.__domicilio
    @domicilio.setter
    def domicilio(self, domicilio):
        self.domicilio = domicilio

    def __str__(self):
        return self.cedula + ' : ' + self.nombre + ' - ' + self.apellido