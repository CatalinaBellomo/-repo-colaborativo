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
        actividad = input("Ingrese la actividad realizada, escriba SALIR cuando quiera terminar: ")

        if actividad == "SALIR":
            break

        actividades.append(actividad)

    return actividades
        


#Funcion 2 
def analizar_habitos(actividades): 
    '''
    

   Recibe uan lista con todas las actividades realizadas por el usario y cuenta cuanta veces se realiza cada actividad
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





