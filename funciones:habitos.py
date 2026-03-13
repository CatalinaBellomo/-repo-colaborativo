#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:19:40 2026

@author: allegra
"""


#Funcion 1 
def registrar_habitos():
    '''
    Permite al usuario ingresar actividades realizadas hasta escribir 'salir' para terminar el programa
    
   
    Returns
    -------
    actividades : list
        Una lista con las actividades ingresadas por el usuario.

    '''
    
    
    actividades = []

    while True:
        actividad = input("Ingrese la actividad realizada, escriba salir cuando quiera terminar: ")

        if actividad == "salir":
            break

        actividades.append(actividad)

    return actividades
        
# probar la funcion 

print(registrar_habitos())

#Funcion 2 
def analizar_habitos(actividades): 
    '''
    

   Recibe uan lista con todas las actividades realziadas por el usario y cuenta cuanta veces se realiza cada actividad
    ----------
    actividades : list
        lista con todas las actividades realizadas 

    Returns
    -------
    diccionario : dict
        diccionario donde la clave es cada actividad realizada y el valor es la canitdad de veces que realizo el usuario

    '''
    diccionario={}
    for actividad in actividades:
        if actividad in diccionario:
            diccionario[actividad] += 1
        else:
            diccionario[actividad] = 1

    return diccionario

#probar la funcion
acciones=['comer','comer','saltar','cantar','correr','dormir','correr']
print(analizar_habitos(acciones))



