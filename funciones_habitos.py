
def esatadistica_actividades_realizadas(actividad):
    """

    Parameters
    ----------
    actividad : str
        La actividad realizada por el participante.

    Returns 
    -------
    frecuencia : dicc
        diccionario cuyos claves son las activcidades y los valores son la frecuencia en la que aparecen.

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

