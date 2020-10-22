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

# accidentsfile = 'us_accidents_small.csv'
# accidentsfile = 'us_accidents_dis_2016.csv'
accidentsfile = 'small.csv'


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


def print_accidents_by_date_range(analyzer, initial_date_, final_date_):
    accidents_in_range = controller.get_accidents_by_date_range(analyzer, initial_date_, final_date_)
    accidents_range_by_severity = controller.get_accidentes_range_by_severity(analyzer, initial_date_, final_date_)
    print('Total de accidentes ocurridos en el rango de la fecha:', accidents_in_range)
    print('\nAccidentes de severidad 1:', accidents_range_by_severity[0])
    print('Accidentes de severidad 2:', accidents_range_by_severity[1])
    print('Accidentes de severidad 3:', accidents_range_by_severity[2])
    if accidents_range_by_severity[0] > accidents_range_by_severity[1] > accidents_range_by_severity[2]:
        print('\nEn este rango de fechas los accidentes más reportados son de tipo 1')
    elif accidents_range_by_severity[1] > accidents_range_by_severity[2]:
        print('\nEn este rango de fechas los accidentes más reportados son de tipo 2')
    else:
        print('\nEn este rango de fechas los accidentes más reportados son de tipo 3')


def print_know_geographical_area(analyzer, latitude_, longitude_, radius_):
    accidents_in_area = controller.get_know_geographical_area(analyzer, latitude_, longitude_, radius_)
    total_accidents_in_area = controller.get_total_geographical_accidents(accidents_in_area)
    print(f'En el punto ({latitude_}, {longitude_}) alrededor de un área de {radius_} millas se han producido:\n')
    for day, accidents in accidents_in_area.items():
        print(f'{day}: {accidents} accidentes')
    print(f'\nPor lo que en total se han generado {total_accidents_in_area} accidentes en el área.')


# ___________________________________________________
#  Menú principal.
# ___________________________________________________


def print_menu():
    print('\n')
    print('*******************************************')
    print('Bienvenido')
    print('1- Inicializar Analizador')
    print('2- Cargar información de accidentes')
    print('3- Conocer los accidentes en una fecha')
    print('4- Conocer los accidentes anteriores a una fecha')
    print('5- Conocer los accidentes en un rango de fechas')
    print('6- Conocer el estado con más accidentes')
    print('7- Conocer los accidentes por rango de horas')
    print('8- Conocer la zona geográfica más accidentada')
    print('9- Usar el conjunto completo de datos')
    print('0- Salir')
    print('*******************************************')


'''
Menu principal.
'''

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
        print('\nConocer los accidentes en una fecha: ')
        date = input('Fecha: ')
        printAccidentsByDateSeverity(cont, date)
    elif int(inputs[0]) == 4:
        print('\nRequerimiento No 2 del reto 3: ')
    elif int(inputs[0]) == 5:
        print('\nConocer los accidentes en un rango de fechas: ')
        initial_date = input('Fecha inicial: ')
        final_date = input('Fecha final: ')
        print_accidents_by_date_range(cont, initial_date, final_date)
    elif int(inputs[0]) == 6:
        print('\nRequerimiento No 4 del reto 3: ')
    elif int(inputs[0]) == 7:
        print('\nRequerimiento No 5 del reto 3: ')
    elif int(inputs[0]) == 8:
        print('Ingrese un punto central para consultar accidentes en esa localización.')
        latitude = input('Latitud: ')
        longitude = input('Longitud: ')
        radius = input('Radio de búsqueda en millas: ')
        print_know_geographical_area(cont, latitude, longitude, radius)
    elif int(inputs[0]) == 9:
        print('\nRequerimiento No 7 del reto 3: ')
    else:
        sys.exit(0)
