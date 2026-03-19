#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:19:40 2026

@author: allegra
"""


#Funcion 1 
def registrar_habitos():
    '''
    Permite al usuario ingresar actividades realizadas hasta escribir 'SALIR' para terminar el programa
    
   
    Returns
    -------
    actividades : list
        Una lista con las actividades ingresadas por el usuario.

    '''
    
    
    actividades = []

    while True:
        actividad = input("Ingrese la actividad realizada, escriba SALIR cuando quiera terminar: ").strip()

        if actividad.upper() == "SALIR":
            break

        actividades.append(actividad)

    return actividades
        


#Funcion 2 
def analizar_habitos(actividades): 
    '''
    

   Recibe una lista con todas las actividades realizadas por el usuario y cuenta cuántas veces aparece cada actividad.
    ----------
    actividades : list
        Lista con todas las actividades realizadas 

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





