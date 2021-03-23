# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:33:52 2021

@author: Valen
"""

# Leer dos numeros y calcular la combinatria de esos dos numeros

# Declaracion variables
fact_M=1
fact_N=1
fact_MN=1
# Entradas
ve_M=int(input("Digite M: "))
ve_N=int(input("Digite N: "))

# Calcular el factorial de M
for i in range(1,ve_M+1,1):
    fact_M=fact_M*i

# Calcular el factorial de N
vp_contReWhile=1
while(vp_contReWhile<=ve_N):
    fact_N=fact_N*vp_contReWhile
    vp_contReWhile=vp_contReWhile+1

# Calcular el factorial de M-N
vp_difMN=ve_M-ve_N
for i in range(1,vp_difMN+1,1):
    fact_MN=fact_MN*i
    
# Calcular la combinatoria
vps_comb_MN=fact_M/(fact_N*fact_MN)

# Salidas
print("Factorial M: ",fact_M)
print("Factorial N: ",fact_N)
print("Factorial M-N: ",fact_MN)
print("La combinatoria de M,N: ",vps_comb_MN)