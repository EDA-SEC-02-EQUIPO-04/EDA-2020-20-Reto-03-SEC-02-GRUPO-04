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

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria.
"""


# -----------------------------------------------------
# API del TAD Catálogo de accidentes.
# -----------------------------------------------------

def new_analyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los accidentes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'accidents': lt.newList('SINGLE_LINKED', compare_ids),
                'date_index': om.newMap(omaptype='RBT', comparefunction=compare_dates)}
    return analyzer


# Funciones para agregar información al catálogo.

def add_accident(analyzer, accident):
    """
    """
    lt.addLast(analyzer['accidents'], accident)
    update_date_index(analyzer['date_index'], accident)
    return analyzer


def update_date_index(map_, accident):
    """
    Se toma la fecha del accidente y se busca si ya existe en el árbol
    dicha fecha. Si es asi, se adiciona a su lista de accidentes
    y se actualiza el índice de tipos de accidentes.

    Si no se encuentra creado un nodo para esa fecha en el árbol
    se crea y se actualiza el índice de tipos de accidentes.
    """
    occurreddate = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map_, accidentdate.date())
    if entry is None:
        datentry = new_data_entry()
        om.put(map_, accidentdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    add_date_index(datentry, accident)


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
    entry = {'severity_index': m.newMap(numelements=10, maptype='PROBING', comparefunction=compare_severities),
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


def get_accidents_by_date(analyzer, date):
    """
    Retorna el numero de accidentes en una fecha.
    """
    lst = om.get(analyzer['date_index'], date)
    print('\n------------------------------')
    print(f'Accidentes del {lst["key"]}:')
    totaccidents = lt.size(lst['value']['lstaccidents'])
    lstiterator = it.newIterator(lst['value']['lstaccidents'])
    while it.hasNext(lstiterator):
        element = it.next(lstiterator)
        print(f'- {element["ID"]}')
    return totaccidents


# ==============================
# Funciones de Comparación.
# ==============================

def compare_ids(id1, id2):
    """
    Compara dos accidentes
    """
    if id1 == id2:
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
