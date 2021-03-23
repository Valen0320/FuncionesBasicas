# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 08:44:30 2021

@author: Valen
"""
# Programa que calcula la hipotenusa y el perimetro de un triangulo rectangulo

# Declaracion y llamado a las librerias y paquetes
import math

def f_titulo():
    print("CALCULO DE LA HIPOTENUSA DE UN TRIANGULO RECTANGULO")

def f_calcularHipotenusa(): # Prototipo de la funcion

    # Variables
    ve_catetoUno=0
    ve_catetoDos=0
    
    vp_radicando=0
    
    vps_Hipotenusa=0
    vps_Perimetro=0
    
    # Entradas
    ve_catetoUno=int(input("Digite cateto uno: "))
    ve_catetoDos=int(input("Digite cateto dos: "))
    
    # Procesos
    vp_radicando=math.pow(ve_catetoUno,2)+math.pow(ve_catetoDos,2)
    vps_Hipotenusa= math.sqrt(vp_radicando)
    
    # Salidas
    print("Hipotenusa: ",vps_Hipotenusa)
    
# Fin del desarrollo de la funcion

# Llamado de la funcion
f_titulo()
f_calcularHipotenusa()
