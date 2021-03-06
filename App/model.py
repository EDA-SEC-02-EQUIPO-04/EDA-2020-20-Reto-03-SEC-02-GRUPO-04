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
from DISClib.ADT import minpq as mpq
from DISClib.DataStructures import heap as h
from DISClib.DataStructures import listiterator as it
import datetime
from math import radians, cos, sin, asin, sqrt
import collections

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
                'latitude_longitude_index': om.newMap(omaptype='RBT', comparefunction=compare_points),
                "states": lt.newList("SINGLE_LINKED", compare_states),
                "hour_index": om.newMap(omaptype="RBT", comparefunction=compare_hours)
                }
    return analyzer


def new_data_entry(accident):
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


# Funciones para agregar información al catálogo.

def add_accident(analyzer, accident):
    """
    """
    lt.addLast(analyzer['accidents'], accident)
    updateDateIndex(analyzer['date_index'], accident)
    update_lat_lng_index(analyzer['latitude_longitude_index'], accident)
    update_hour_index(analyzer["hour_index"], accident)
    if lt.isPresent(analyzer["states"], accident["State"]) == 0:
        lt.addLast(analyzer["states"], accident["State"])
    return analyzer


def updateDateIndex(map, accident):
    startTime = accident["Start_Time"]
    complete_date = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M:%S")
    date = datetime.datetime(complete_date.year, complete_date.month, complete_date.day)
    key = date
    entry = om.get(map, date)
    if entry:
        dateEntry = me.getValue(entry)
    else:
        dateEntry = new_data_entry(key)
        om.put(map, date, dateEntry)
    add_date_index(dateEntry, accident)
    return map


def update_lat_lng_index(map, accident):
    point = accident["Start_Lat"], accident["Start_Lng"]
    entry = om.get(map, point)
    if entry:
        point_entry = me.getValue(entry)
    else:
        point_entry = new_data_entry(accident)
        om.put(map, point, point_entry)
    add_date_index(point_entry, accident)
    return map


def update_hour_index(map, accident):
    startTime = accident["Start_Time"].split(" ")
    h_m_s = startTime[1].split(":")  # Horas, minutos, segundos
    h = h_m_s[0]  # Horas
    m = h_m_s[1]  # Minutos

    if int(m) < 30:
        hour_index = h + ":00"
    else:
        hour_index = h + ":30"

    entry = om.get(map, hour_index)
    if entry:
        hour_entry = me.getValue(entry)
    else:
        hour_entry = new_hour_entry()
        om.put(map, hour_index, hour_entry)
    add_hour_index(hour_entry, accident)
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

    state_index = datentry["state_index"]
    state_entry = m.get(state_index, accident["State"])
    if state_entry is None:
        entry = new_state_index(accident["State"])
        lt.addLast(entry["lst_accidents_by_state"], accident)
        m.put(state_index, accident["State"], entry)
    else:
        entry = me.getValue(state_entry)
        lt.addLast(entry["lst_accidents_by_state"], accident)


def add_hour_index(hour_entry, accident):
    lst = hour_entry['lst_accidents']
    lt.addLast(lst, accident)
    severity_index = hour_entry['severity_index']
    seventry = m.get(severity_index, accident['Severity'])
    if seventry is None:
        entry = new_severity_index(accident['Severity'])
        lt.addLast(entry['lstseverities'], accident)
        m.put(severity_index, accident['Severity'], entry)
    else:
        entry = me.getValue(seventry)
        lt.addLast(entry['lstseverities'], accident)


def new_data_entry(key):
    """
    Crea una entrada en el indice por fechas, es decir en el árbol
    binario.
    """
    entry = {'severity_index': m.newMap(numelements=3, maptype='PROBING', comparefunction=compare_severities),
             'lstaccidents': lt.newList('SINGLE_LINKED', compare_dates),
             "state_index": m.newMap(maptype="PROBING", comparefunction=compare_states),
             "key": key
             }
    return entry


def new_hour_entry():
    """
    Crea una entrada en el indice por horas, es decir en el árbol
    binario.
    """
    entry = {"severity_index": m.newMap(numelements=4, maptype='PROBING', comparefunction=compare_severities),
             "lst_accidents": lt.newList("SINGLE_LINKED", compare_hours)
             }
    return entry


def new_severity_index(severity_grade):
    """
    Crea una entrada en el indice por tipo de severidad, es decir en
    la tabla de hash, que se encuentra en cada nodo del árbol.
    """
    seventry = {'severity': severity_grade, 'lstseverities': lt.newList('SINGLELINKED', compare_severities)}
    return seventry


def new_state_index(state):
    """
    Crea una entrada en el indice por estado, es decir en
    la tabla de hash, que se encuentra en cada nodo del árbol.
    """
    state_entry = {"state": state, "lst_accidents_by_state": lt.newList("SINGLE_LINKED", compare_states)}
    return state_entry


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
        date = walking_date
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


def getAccidentsByRange(analyzer, initialDate, finalDate):
    """
    Retorna el número de accidentes en un rango de fechas,
    la fecha final el la que da el usuario al programa y la inicizal
    es la menor fecha de la que se tenga registro.
    """

    lst = om.values(analyzer['date_index'], initialDate, finalDate)
    lstiterator = it.newIterator(lst)
    totalaccidents = 0

    while it.hasNext(lstiterator):
        lstdate = it.next(lstiterator)
        totalaccidents += lt.size(lstdate['lstaccidents'])
    mayor = get_greater_accidents_date(analyzer, initialDate, finalDate)
    return (totalaccidents, mayor)


def get_accidentes_range_by_severity(analyzer, initial_date, final_date):
    walking_date = initial_date
    severities_on_range = [0, 0, 0]
    while walking_date <= final_date:
        date = walking_date
        actual_severities = getAccidentsBySeverity(analyzer, date)
        severities_on_range[0] += actual_severities[0]
        severities_on_range[1] += actual_severities[1]
        severities_on_range[2] += actual_severities[2]
        walking_date += datetime.timedelta(days=1)
    return severities_on_range


def get_greater_accidents_date(analyzer, initial_date, final_date):
    key_lst = om.values(analyzer["date_index"], initial_date, final_date)
    iterator = it.newIterator(key_lst)
    accidents_size = 0
    greater = None
    while it.hasNext(iterator):
        date_entry = it.next(iterator)
        if accidents_size < lt.size(date_entry["lstaccidents"]):
            greater = date_entry["key"].strftime("%Y-%m-%d")
            accidents_size = lt.size(date_entry["lstaccidents"])
    return greater


def get_state_by_accidents_size_in_range(analyzer, initial_date, final_date):
    key_lst = om.values(analyzer["date_index"], initial_date, final_date)
    state_lst = analyzer["states"]
    state_iterator = it.newIterator(state_lst)
    greater = None
    greater_size = 0
    size = 0
    while it.hasNext(state_iterator):
        state = it.next(state_iterator)
        key_iterator = it.newIterator(key_lst)
        while it.hasNext(key_iterator):
            date = it.next(key_iterator)
            if m.contains(date["state_index"], state):
                entry = m.get(date["state_index"], state)
                lst_accidents_by_state = me.getValue(entry)["lst_accidents_by_state"]
                size = size + lt.size(lst_accidents_by_state)
        if size > greater_size:
            greater = state
            greater_size = size
    return greater


def get_accidents_severity_by_hour_range(analyzer, keylo, keyhi):
    entry = om.get(analyzer["hour_index"], "05:30")
    hour_range = om.values(analyzer["hour_index"], keylo, keyhi)
    iterator = it.newIterator(hour_range)
    severity_1 = 0
    severity_2 = 0
    severity_3 = 0
    severity_4 = 0
    total = 0
    while it.hasNext(iterator):
        hour = it.next(iterator)
        for severity_number in range(1, 5):
            severity_entry = m.get(hour["severity_index"], str(severity_number))
            if severity_entry is not None:
                severity = me.getValue(severity_entry)
                size = lt.size(severity["lstseverities"])
                if severity_number == 1:
                    severity_1 = severity_1 + size
                elif severity_number == 2:
                    severity_2 = severity_2 + size
                elif severity_number == 3:
                    severity_3 = severity_3 + size
                else:
                    severity_4 = severity_4 + size
                total = severity_1 + severity_2 + severity_3 + severity_4
            else:
                pass
    return total, severity_1, severity_2, severity_3, severity_4


def get_accidentes_range_by_severity(analyzer, initial_date, final_date):
    walking_date = initial_date
    severities_on_range = [0, 0, 0]
    while walking_date <= final_date:
        date = walking_date
        actual_severities = getAccidentsBySeverity(analyzer, date)
        severities_on_range[0] += actual_severities[0]
        severities_on_range[1] += actual_severities[1]
        severities_on_range[2] += actual_severities[2]
        walking_date += datetime.timedelta(days=1)
    return severities_on_range


def get_know_geographical_area(analyzer, latitude_, longitude_, radius):
    points = om.values(analyzer["date_index"], datetime.datetime.strptime("2015-01-01", '%Y-%m-%d'),
                       datetime.datetime.strptime("2021-01-01", '%Y-%m-%d'))
    iterator = it.newIterator(points)
    actual_area = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    while it.hasNext(iterator):
        entry = it.next(iterator)
        lat_point, lon_point = (entry['lstaccidents']['first']['info']['Start_Lat'],
                                entry['lstaccidents']['first']['info']['Start_Lng'])
        distance_between_points = distance(latitude_, float(lat_point), longitude_, float(lon_point))
        if distance_between_points <= radius:
            week_day = datetime.datetime.strptime(entry['lstaccidents']['first']['info']['Start_Time'],
                                                  '%Y-%m-%d %H:%M:%S').strftime('%A')
            actual_area[week_day] += entry['lstaccidents']['size']
    return actual_area


def get_total_geographical_accidents(accidents_in_area):
    total = 0
    for accidents in accidents_in_area.values():
        total += accidents
    return total


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
    Compara dos puntos
    """
    if type(point1) != tuple:
        print('True')
    if type(point2) != tuple:
        print('True')
    if point1 == point2:
        return 0
    elif point1 > point2:
        return 1
    else:
        return -1


def compare_hours(hour1, hour2):
    """
    Compara dos horas
    """
    if hour1 == hour2:
        return 0
    elif hour1 > hour2:
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


def compare_states(state1, state2):
    """
    Compara dos estados en los que ocurrieron accidentes.

    """
    try:
        state = me.getKey(state2)
        if state1 == state:
            return 0
        elif state1 > state:
            return 1
        else:
            return -1
    except:
        if state1 == state2:
            return 0
        elif state1 > state2:
            return 1
        else:
            return -1
