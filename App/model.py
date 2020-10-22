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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
from DISClib.DataStructures import listiterator as it
import datetime
from math import radians, cos, sin, asin, sqrt

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria.
"""


# -----------------------------------------------------
# API del TAD Catálogo de accidentes.
# -----------------------------------------------------

def new_Analyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los accidentes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'accidents': lt.newList('SINGLE_LINKED', compare_ids),
                'date_index': om.newMap(omaptype='RBT', comparefunction=compare_dates),
                'latitude_longitude_index': om.newMap(omaptype='RBT', comparefunction=compare_points)}
    return analyzer


# Funciones para agregar información al catálogo.

def add_accident(analyzer, accident):
    """
    """
    lt.addLast(analyzer['accidents'], accident)
    updateDateIndex(analyzer['date_index'], accident)
    update_lat_lng_index(analyzer['latitude_longitude_index'], accident)
    return analyzer


def updateDateIndex(map, accident):
    startTime = accident["Start_Time"].split(" ")
    date = startTime[0]
    entry = om.get(map, date)
    if entry:
        dateEntry = me.getValue(entry)
    else:
        dateEntry = new_data_entry()
        om.put(map, date, dateEntry)
    add_date_index(dateEntry, accident)
    return map


def update_lat_lng_index(map, accident):
    point = accident["Start_Lat"], accident["Start_Lng"]
    entry = om.get(map, point)
    if entry:
        point_entry = me.getValue(entry)
    else:
        point_entry = new_data_entry()
        om.put(map, point, point_entry)
    add_date_index(point_entry, accident)
    return map


def add_date_index(datentry, accident):
    """
    Actualiza un indice de tipo de accidentes. Este índice tiene una lista
    de accidentes y una tabla de hash cuya llave es el tipo de accidentn y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstaccidents']
    lt.addLast(lst, accident)
    severity_index = datentry['severity_index']
    seventry = m.get(severity_index, accident['Severity'])
    if seventry is None:
        entry = new_severity_index(accident['Severity'])
        lt.addLast(entry['lstseverities'], accident)
        m.put(severity_index, accident['Severity'], entry)
    else:
        entry = me.getValue(seventry)
        lt.addLast(entry['lstseverities'], accident)


def new_data_entry():
    """
    Crea una entrada en el indice por fechas, es decir en el árbol
    binario.
    """
    entry = {'severity_index': m.newMap(numelements=3, maptype='PROBING', comparefunction=compare_severities),
             'lstaccidents': lt.newList('SINGLE_LINKED', compare_dates)}
    return entry


def new_severity_index(severity_grade):
    """
    Crea una entrada en el indice por tipo de severidad, es decir en
    la tabla de hash, que se encuentra en cada nodo del árbol.
    """
    seventry = {'severity': severity_grade, 'lstseverities': lt.newList('SINGLELINKED', compare_severities)}
    return seventry


# ==============================
# Funciones de consulta.
# ==============================


def accidents_size(analyzer):
    """
    Número de accidentes.
    """
    return lt.size(analyzer['accidents'])


def index_height(analyzer):
    """
    Altura del árbol.
    """
    return om.height(analyzer['date_index'])


def index_size(analyzer):
    """
    Número de elementos en el índice.
    """
    return om.size(analyzer['date_index'])


def min_key(analyzer):
    """
    Llave más pequeña.
    """
    return om.minKey(analyzer['date_index'])


def max_key(analyzer):
    """
    Llave más grande.
    """
    return om.maxKey(analyzer['date_index'])


def getAccidentsByDate(analyzer, date):
    entry = om.get(analyzer["date_index"], date)
    if entry is None:
        return 0
    dateEntry = me.getValue(entry)
    accidentsByDate = lt.size(dateEntry["lstaccidents"])
    return accidentsByDate


def get_accidents_by_date_range(analyzer, initial_date, final_date):
    walking_date = initial_date
    accidents_on_range = 0
    while walking_date <= final_date:
        date = walking_date.strftime('%Y-%m-%d')
        accidents_on_range += getAccidentsByDate(analyzer, date)
        walking_date += datetime.timedelta(days=1)
    return accidents_on_range


def getAccidentsBySeverity(analyzer, date):
    entry = om.get(analyzer["date_index"], date)
    if entry is None:
        return 0, 0, 0
    dateEntry = me.getValue(entry)
    try:
        entryAccidentsBySeverity1 = m.get(dateEntry["severity_index"], "1")
        accidentsBySeverity1 = me.getValue(entryAccidentsBySeverity1)
        severity1Size = lt.size(accidentsBySeverity1["lstseverities"])
    except:
        severity1Size = 0

    try:
        entryAccidentsBySeverity2 = m.get(dateEntry["severity_index"], "2")
        accidentsBySeverity2 = me.getValue(entryAccidentsBySeverity2)
        severity2Size = lt.size(accidentsBySeverity2["lstseverities"])
    except:
        severity2Size = 0

    try:
        entryAccidentsBySeverity3 = m.get(dateEntry["severity_index"], "3")
        accidentsBySeverity3 = me.getValue(entryAccidentsBySeverity3)
        severity3Size = lt.size(accidentsBySeverity3["lstseverities"])
    except:
        severity3Size = 0

    return severity1Size, severity2Size, severity3Size


def get_accidentes_range_by_severity(analyzer, initial_date, final_date):
    walking_date = initial_date
    severities_on_range = [0, 0, 0]
    while walking_date <= final_date:
        date = walking_date.strftime('%Y-%m-%d')
        actual_severities = getAccidentsBySeverity(analyzer, date)
        severities_on_range[0] += actual_severities[0]
        severities_on_range[1] += actual_severities[1]
        severities_on_range[2] += actual_severities[2]
        walking_date += datetime.timedelta(days=1)
    return severities_on_range


def get_know_geographical_area(analyzer, latitude_, longitude_, radius):
    points = om.values(analyzer["latitude_longitude_index"], 1, -1)
    iterator = it.newIterator(points['first']['info']['lstaccidents'])
    print(points['first']['info']['lstaccidents'])
    # while it.hasNext(iterator):
    #     print(iterator)
    #     print(i)
    #     lat_point, lon_point = 0, 0
    #     distance_between_points = distance(latitude_, lat_point, longitude_, lon_point)


def distance(lat1, lat2, lon1, lon2):
    lon1, lon2 = radians(lon1), radians(lon2)
    lat1, lat2 = radians(lat1), radians(lat2)
    # Haversine formula
    dlon, dlat = lon2 - lon1, lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in miles.
    r = 3956
    return c * r

    # ==============================
# Funciones de Comparación.
# ==============================

def compare_ids(id1, id2):
    """
    Compara dos accidentes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compare_dates(date1, date2):
    """
    Compara dos fechas
    """
    if date1 == date2:
        return 0
    elif date1 > date2:

        return 1
    else:
        return -1


def compare_points(point1, point2):
    """
    Compara dos fechas
    """
    if point1 == point2:
        return 0
    elif point1 == -1:
        return 1
    else:
        return -1


def compare_severities(severity1, severity2):
    """
    Compara dos severidades de accidentes.

    """
    severity = me.getKey(severity2)
    if severity1 == severity:
        return 0
    elif severity1 > severity:
        return 1
    else:
        return -1
