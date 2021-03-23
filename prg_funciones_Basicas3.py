# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:11:39 2021

@author: Valen
"""

# Programa que calcula la hipotenusa y el perimetro de un triangulo rectangulo

# Declaracion y llamado a las librerias y paquetes
import math

def f_titulo():
    print("CALCULO DE LA HIPOTENUSA DE UN TRIANGULO RECTANGULO")
    
def f_calcularHipotenusa(p_catetoUno,p_catetoDos): # Prototipo de la funcion
    vp_radicando=0
    vps_Hipotenusa=0
    #vps_Perimetro=0
    
    # Procesos
    vp_radicando=math.pow(p_catetoUno,2)+math.pow(p_catetoDos,2)
    vps_Hipotenusa= math.sqrt(vp_radicando)
    
    # Retornar respuesta
    return vps_Hipotenusa
    
# Fin del desarrollo de la funcion

# Control del programa - principal
f_titulo()
ve_catetoUno=int(input("Digite cateto uno: "))
ve_catetoDos=int(input("Digite cateto dos: "))

# Variable de proceso salida - receptora
vps_rf_Hip=f_calcularHipotenusa(ve_catetoUno,ve_catetoDos)
print("La hipotenusa es: ",vps_rf_Hip)