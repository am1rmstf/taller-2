#!/usr/bin/python
#-*- coding: utf-8 -*-

class Detalle_Factura:
    def __init__(self, producto):
        self.cantidad = 0.0
        self.valor_x_cantidad = 0.0
        self.ref_producto = producto
        self.productos = []
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad
    
    @property
    def valor_x_cantidad(self):
        return self.__valor_x_cantidad
    @valor_x_cantidad.setter
    def valor_x_cantidad(self, valor_x_cantidad):
        self.__valor_x_cantidad = valor_x_cantidad

    def __str__(self):
        return str(self.ref_producto)