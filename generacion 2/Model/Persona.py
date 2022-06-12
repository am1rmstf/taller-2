#!/usr/bin/python
#-*- coding: utf-8 -*-

class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def cedula(self):
        return self.__cedula
    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula


     
