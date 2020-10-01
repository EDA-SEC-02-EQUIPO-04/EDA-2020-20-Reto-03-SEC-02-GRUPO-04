# -*- coding: utf-8 -*-
"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from App import controller
from time import process_time

assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos.
# ___________________________________________________

accidentsfile = 'us_accidents_small.csv'



# ___________________________________________________
#  Funciones Print
# ___________________________________________________

def printAccidentsByDateSeverity(analyzer, date):
    accidentsInDate = controller.getAccidentsByDate(analyzer, date)
    accidentsBySeverity = controller.getAccidentsBySeverity(analyzer, date)
    print("Total de accidentes ocurridos en la fecha:", accidentsInDate)
    print("\nAccidentes de severidad 1:", accidentsBySeverity[0])
    print("Accidentes de severidad 2:", accidentsBySeverity[1])
    print("Accidentes de severidad 3:", accidentsBySeverity[2])

# ___________________________________________________
#  Menú principal.
# ___________________________________________________


def print_menu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Conocer los accidentes en una fecha")
    print("4- Conocer los accidentes anteriores a una fecha")
    print("5- Conocer los accidentes en un rango de fechas")
    print("6- Conocer el estado con más accidentes")
    print("7- Conocer los accidentes por rango de horas")
    print("8- Conocer la zona geográfica más accidentada")
    print("8- Usar el conjunto completo de datos")
    print("0- Salir")
    print("*******************************************")


"""
Menu principal.
"""


cont = controller.init()
while True:
    print_menu()
    inputs = input('Seleccione una opción para continuar\n> ')
    if int(inputs[0]) == 1:
        t1_start = process_time()
        print('\nInicializando...')
        cont = controller.init()  # cont es el controlador que se usará de acá en adelante.
        print('Tiempo de ejecución ', process_time() - t1_start, ' segundos')
    elif int(inputs[0]) == 2:
""" Aternativa 2
        print("\nCargando información de los accidentes ....")
        controller.loadData(cont, accidentsfile) 
        print('Accidentes cargados: ' + str(controller.accidentsSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))

    elif int(inputs[0]) == 3:
        print("\n Buscar accidentes en un grupo de segveridad en un fecha: ")
        initialDate = input("Fecha (YYYY-MM-DD): ")
        severity = input("Severidad: ")
        numberseverities = controller.getAccidentsByRangeCode(cont, initialDate, severity)
        print("\nTotal de accidentes de severidad: " + severity + " en esa fecha:  " +
              str(numberseverities))
    else:
        sys.exit(0)
sys.exit(0)
"""

        t1_start = process_time()
        print('\nCargando información de accidentes...')
        controller.load_data(cont, accidentsfile)
        print(f'Accidentes cargados: {controller.accidents_size(cont)}')
        print(f'Altura del árbol: {controller.index_height(cont)}')
        print(f'Elementos en el árbol: {controller.index_size(cont)}')
        print(f'Menor Llave: {controller.min_key(cont)}')
        print(f'Mayor Llave: {controller.max_key(cont)}')
        print('Tiempo de ejecución ', process_time() - t1_start, ' segundos')

    elif int(inputs[0]) == 3:
        print("\nConocer los accidentes en una fecha: ")
        date = input("Fecha: ")
        printAccidentsByDateSeverity(cont, date)
        
    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 2 del reto 3: ")
    
    elif int(inputs[0]) == 5:
        print("\nRequerimiento No 3 del reto 3: ")

    elif int(inputs[0]) == 6:
        print("\nRequerimiento No 4 del reto 3: ")

    elif int(inputs[0]) == 7:
        print("\nRequerimiento No 5 del reto 3: ")

    elif int(inputs[0]) == 8:
        print("\nRequerimiento No 6 del reto 3: ")
    
    elif int(inputs[0]) == 8:
        print("\nRequerimiento No 7 del reto 3: ")
    else:
        sys.exit(0)
""" Master    
    elif int(inputs[0]) == 3:
        t1_start = process_time()
        date = input('Fecha a consultar (YYYY-MM-DD): ')
        print(f'\nBuscando accidentes del {date}...')
        total = controller.get_accidents_by_date(cont, date)
        print(f'\nTotal de accidentes en {date}: {total}')
        print('Tiempo de ejecución ', process_time() - t1_start, ' segundos')
     """
