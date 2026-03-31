

# repo-colaborativo

Integrantes del grupo: Allegra Gegeschatz, Ana Piuma, Matilda Ivanchich y Catalina Bellomo.

Este repositorio contiene un programa en Python que permite registrar actividades realizadas durante el día y generar un resumen con la cantidad de veces que aparece cada una.

## Archivos

- `funciones_habitos.py`: contiene las funciones necesarias para registrar y analizar las actividades.
- `programa_principal.py`: importa las funciones del módulo y ejecuta el programa principal.

## Funciones

### `registrar_habitos()`
Esta función solicita al usuario que ingrese actividades una por una.  
El ingreso finaliza cuando el usuario escribe `SALIR`.  
La función devuelve una lista con todas las actividades registradas.

### `analizar_habitos(actividades)`
Esta función recibe una lista de actividades y cuenta cuántas veces aparece cada una.  
El resultado se guarda en un diccionario y luego se devuelve.

## Ejecución

Para usar el programa, se debe ejecutar el archivo `programa_principal.py`.