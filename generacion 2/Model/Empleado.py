#!/usr/bin/python
#-*- coding: utf-8 -*-

from Persona import Persona

class Empleado(Persona):
    def __init__(self):
        self.usuario = None
        self.clave = None

