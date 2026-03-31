
def registrar_habitos(): 
    """ 
    Pide al usuario que ingrese la cantidad de actividades que desee y devuelve
    una lista con todas ellas. 
    
    Returns 
    ------- 
    lista : list -- lista de actividades ingresada por el usuario 
    """ 
    actividades = input('Ingrese actividades: ') 
    lista = actividades.split() 
    return lista 

def analizar_habitos(lista): 
    """ 
    Toma la lista de la funcion anterior (registrar_habitos()) y crea un
    diccionario que indica cuantas veces se repite cada actividad 
    Parameters 
    ---------- 
    lista : list -- lista de actividades (previamente creade por la funcion 
                                          anterior) 
    Returns 
    ------- 
    frecuencia : dict -- diccionario con la frecuencia de cada actividad, 
    cuantas veces se repite cada una en la lista 
    """ 
    frecuencia = {} 
    for act in lista: 
        if act in frecuencia: 
            frecuencia[act] = frecuencia[act] + 1 
        else: frecuencia[act] = 1 
    return frecuencia 

'''
lista = registrar_habitos() 
resultado = analizar_habitos(lista) 
print(resultado)
'''





























