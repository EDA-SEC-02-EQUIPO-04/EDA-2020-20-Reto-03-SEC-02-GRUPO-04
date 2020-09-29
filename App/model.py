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

    Crea una lista vacia para guardar todos los accidentnes
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
    update_date_index(analyzer['dateIndex'], accident)
    return analyzer


def update_date_index(map_, accident):
    """
    Se toma la fecha del accidente y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de accidentnes
    y se actualiza el indice de tipos de accidentnes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de accidentnes
    """
    occurreddate = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map_, accidentdate.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map_, accidentdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, accident)
    return map_


def add_date_index(datentry, accident):
    """
    Actualiza un indice de tipo de accidentnes.  Este indice tiene una lista
    de accidentnes y una tabla de hash cuya llave es el tipo de accidentn y
    el valor es una lista con los accidentnes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstaccidents']
    lt.addLast(lst, accident)
    offenseIndex = datentry['offenseIndex']
    offentry = m.get(offenseIndex, accident['OFFENSE_CODE_GROUP'])
    if (offentry is None):
        entry = newOffenseEntry(accident['OFFENSE_CODE_GROUP'], accident)
        lt.addLast(entry['lstoffenses'], accident)
        m.put(offenseIndex, accident['OFFENSE_CODE_GROUP'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], accident)
    return datentry


def new_data_entry(accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': m.newMap(numelements=30,
                                      maptype='PROBING',
                                      comparefunction=compare_offenses),
             'lstaccidents': lt.newList('SINGLE_LINKED', compare_dates)}
    return entry


def new_offense_entry(offensegrp, accident):
    """
    Crea una entrada en el indice por tipo de accidentn, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': offensegrp, 'lstoffenses': lt.newList('SINGLELINKED', compare_offenses)}
    return ofentry


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


def get_accidents_by_date(analyzer, initialDate, finalDate):
    """
    Retorna el numero de accidentnes en un rago de fechas.
    """
    lst = om.values(analyzer['date_index'], initialDate, finalDate)
    lstiterator = it.newIterator(lst)
    totaccidents = 0
    while it.hasNext(lstiterator):
        lstdate = it.next(lstiterator)
        totaccidents += lt.size(lstdate['lstaccidents'])
    return totaccidents


# ==============================
# Funciones de Comparación.
# ==============================

def compareIds(id1, id2):
    """
    Compara dos accidentnes
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
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compare_offenses(offense1, offense2):
    """
    Compara dos tipos de accidentnes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1
