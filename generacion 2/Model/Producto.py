#!/usr/bin/python
#-*- coding: utf-8 -*-

class Producto:
    def __init__(self, nombre, idproducto, valor):
        self.nombre = nombre
        self.idproducto = idproducto
        self.valor = valor

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def idproducto(self):
        return self.__idproducto
    @idproducto.setter
    def idproducto(self, idproducto):
        self.__idproducto = idproducto
    
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    
    def __str__(self):
        return self.__nombre + ' - ' + str(self.__valor)