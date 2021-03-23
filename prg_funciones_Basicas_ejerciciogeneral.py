# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:14:50 2021

@author: Valen
"""
# Programa que calcula la hipotenusa y el perimetro de un triangulo rectangulo

# Declaracion y llamado a las librerias y paquetes
import math

# Variables
ve_catetoUno=0
ve_catetoDos=0

vps_Hipotenusa=0
vps_Perimetro=0

# Entradas
ve_catetoUno=int(input("Digite cateto uno: "))
ve_catetoDos=int(input("Digite cateto dos: "))

# Procesos
vps_Hipotenusa= math.sqrt(math.pow(ve_catetoUno,2)+math.pow(ve_catetoDos,2))

# Salidas
print("Hipotenusa: ",vps_Hipotenusa)