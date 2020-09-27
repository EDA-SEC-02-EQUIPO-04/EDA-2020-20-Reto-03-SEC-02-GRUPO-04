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
import datetime

assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de accidentes
# -----------------------------------------------------

def newAnalyser():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los accidentes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyser = {'severity':lt.newList('SINGLE_LINKED', compareids),
                'date': om.newMap(omaptype ='BST', comparefunction = compareDates)}
    return analyser

# Funciones para agregar informacion al catalogo

def addAccident(analyzer, accident):
    """
    """
    lt.addLast(analyzer['severity'], accident)
    updateDateIndex(analyzer['date'], accident)
    return analyzer

def updateDateIndex(map, accident):
    """
    Se toma la fecha del accidente y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de accidentes
    y se actualiza el indice de la severidad de los accidentes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de la severidad de los accidentes
    """
    
    ocurreddate = accident['Start_Time']
    accidentDate = datetime.datetime.strptime(ocurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, accidentDate.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, accidentDate.date(), datentry)
    else: 
        datentry = me.getValue(entry)
    addDateIndex(datentry, accident)
    
    return map

def addDateIndex(datentry, accident):
    """
    Actualiza un indice de la severidad del accidente. Este indice tiene una lista
    de las severidades y una tabla de hash cuya llave a severidad del accidente y
    el valor es una lista con los accidentes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """

    lst = datentry['lstaccidents']
    lt.addLast(lst, accident)
    severityIndex = datentry['severityIndex']
    offentry = m.get(severityIndex, accident['Severity'])
    if offentry is None:
        entry = newoffenseEntry(accident['Severity'], accident)
        lt.addLast(entry['lstseverity'], accident)
        m.put(severityIndex, accident['Severity'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstseverity'], accident)
    return datentry

def newDataEntry(accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario
    """
    entry = {'severityIndex': None, 'lstaccidents': None}
    entry['severityIndex'] = m.newMap(numelements=30,
                                     maptype='PROBING',
                                     comparefunction=compareseverities)
    entry['lstaccidents'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

def newoffenseEntry(severitygrp, accident):
    """
    Crea una entrada en el indice por la severidad del accidente, es decir, en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """

    seventry = {'severity': None, 'lstseverity': None}
    seventry['severity'] = severitygrp
    seventry['lstseverity'] = lt.newList('SINGLE_LINKED', compareseverities)
    return seventry

# ==============================
# Funciones de consulta
# ==============================


def accidentsSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer['severity'])


def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['date'])


def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['date'])


def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['date'])


def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['date'])

def getAccidentsByRangeCode(analyzer, initialDate, severityCode):
    """
    Para una fecha determinada, retorna el numero de accidentes
    según una severidad
    """
    accidentDate = om.get(analyzer['date'], initialDate)
    if accidentDate['key'] is not None:
        severitymap = me.getValue(accidentDate)['severityIndex']
        numseverities = m.get(severitymap, severityCode)
        if numseverities is not None:
            return m.size(me.getValue(numseverities)['lstseverity'])
    return 0

# ==============================
# Funciones de Comparacion
# ==============================

def compareids(id1, id2):
    """
    Compara dos accidentes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def  compareseverities(severity1, severity2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    severity = me.getKey(severity2)
    if severity1 == severity:
        return 0
    elif severity1 > severity:
        return 1
    else:
        -1
