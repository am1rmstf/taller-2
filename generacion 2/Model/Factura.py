#!/usr/bin/python
#-*- coding: utf-8 -*-
from datetime import datetime
class Factura:
    def __init__(self, codigo, fecha_emision, empleado, cliente, detalle_factura):
        self.codigo = codigo
        self.fecha_emision = fecha_emision
        self.subtotal = 0.0
        self.valor_iva = 0.0
        self.valor_total = 0.0 
        self.ref_cliente = cliente
        self.ref_empleado = empleado
        self.ref_detalle_factura = detalle_factura
        self.clientes = []
        self.empleados = []

    @property
    def codigo(self):
        return self.__codigo
    @subtotal.setter
    def subtotal(self, codigo):
        self.__codigo = codigo

    @property
    def fecha_emision(self):
        return self.__fecha_emision
    @fecha_emision.setter
    def fecha_emision(self, valor):
        self.__fecha_emision = datetime.strptime(valor, '%d-%m-%Y')
    
    @property
    def subtotal(self):
        return self.__subtotal
    @subtotal.setter
    def subtotal(self, subtotal):
        self.__subtotal = subtotal

    @property
    def valor_iva(self):
        return self.__valor_iva
    @valor_iva.setter
    def valor_iva(self, valor_iva ):
        self.__valor_iva = valor_iva
    
    @property
    def valor_total(self):
        return self.__valor_total
    @valor_total.setter
    def valor_total(self, valor_total ):
        self.__valor_total = valor_total

    def __str__(self):
        return str(self.ref_empleado) + ' - ' + str(self.ref_cliente) + ' - ' + str(self.ref_detalle_factura)