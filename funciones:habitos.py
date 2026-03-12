#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 15:19:40 2026

@author: allegra
"""

def esatadistica_actividades_realizadas(actividad):
    """

    Parameters
    ----------
    actividad : str
        La actividad realizada por el .

    Returns
    -------
    frecuencia : TYPE
        DESCRIPTION.

    """
    actividad = input('Ingrese la actividad realizada')
    lista = []
    lista.append(actividad)
    frecuencia = {}
    for act in lista:
        if act in frecuencia:
            frecuencia[act] +=1
        else:
            frecuencia[act] = 1
    return frecuencia
