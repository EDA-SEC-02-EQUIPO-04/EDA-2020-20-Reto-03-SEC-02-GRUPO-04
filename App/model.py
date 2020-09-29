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

""" Alternativa 3
def newAnalyzer():

    analyzer = {"accidents:": None,
                "dateIndex": None
                }

    analyzer["accidents"] = lt.newList("SINGLE_LINKED", compareIds)
    analyzer["dateIndex"] = om.newMap(omaptype="BST", comparefunction=compareDates)

    return analyzer


# Funciones para agregar informacion al catalogo

def addAccident(analyzer, accident):
    lt.addLast(analyzer["accidents"], accident)
    updateDateIndex(analyzer["dateIndex"], accident)
    return analyzer

def updateDateIndex(map, accident):
    startTime = accident["Start_Time"].split(" ")
    date = startTime[0]
    entry = om.get(map, date)
    if entry:
        dateEntry = me.getValue(entry)
    else:
        dateEntry = newDateEntry(accident)
        om.put(map, date, dateEntry)
    addDateIndex(dateEntry, accident)
    return map

def newDateEntry(accident):
    entry = {"severityIndex": None, "accidentsLst": None}
    entry["severityIndex"] = m.newMap(numelements=30, maptype="PROBING", comparefunction=compareSeveritys)
    entry["accidentsLst"] = lt.newList("SINGLE_LINKED", compareDates)
    return entry

def addDateIndex(dateEntry, accident):
    lt.addLast(dateEntry["accidentsLst"], accident)
    severityIndex = dateEntry["severityIndex"]
    severityEntry = m.get(severityIndex, accident["Severity"])
    if severityEntry:
        entry = me.getValue(severityEntry)
        lt.addLast(entry["severityLst"], accident)
    else:
        entry = newSeverityEntry(accident["Severity"], accident)
        lt.addLast(entry["severityLst"], accident)
        m.put(severityIndex, accident["Severity"], entry)

def newSeverityEntry(severity, accident):
    severityEntry = {"severity": None, "severityLst": None}
    severityEntry["severity"] = severity
    severityEntry["severityLst"] = lt.newList("SINGLE_LINKED", compareSeveritys)
    return severityEntry

# ==============================
# Funciones de consulta
# ==============================

def accidentsSize(analyzer):
    size = lt.size(analyzer["accidents"])
    return size

def indexHeight(analyzer):
    height = om.height(analyzer["dateIndex"])
    return height

def indexSize(analyzer):
    indexSize = om.size(analyzer["dateIndex"])
    return indexSize

def minKey(analyzer):
    minKey = om.minKey(analyzer["dateIndex"])
    return minKey

def maxKey(analyzer):
    maxKey = om.maxKey(analyzer["dateIndex"])
    return maxKey

def getAccidentsByDate(analyzer, date):
    entry = om.get(analyzer["dateIndex"], date)
    dateEntry = me.getValue(entry)
    accidentsByDate = lt.size(dateEntry["accidentsLst"])
    return accidentsByDate

def getAccidentsBySeverity(analyzer, date):
    entry = om.get(analyzer["dateIndex"], date)
    dateEntry = me.getValue(entry)
    try:
        entryAccidentsBySeverity1 = m.get(dateEntry["severityIndex"], "1")
        accidentsBySeverity1 = me.getValue(entryAccidentsBySeverity1)
        severity1Size = lt.size(accidentsBySeverity1["severityLst"])
    except:
        severity1Size = 0

    try:
        entryAccidentsBySeverity2 = m.get(dateEntry["severityIndex"], "2")
        accidentsBySeverity2 = me.getValue(entryAccidentsBySeverity2)
        severity2Size = lt.size(accidentsBySeverity2["severityLst"])
    except:
        severity2Size = 0

    try: 
        entryAccidentsBySeverity3 = m.get(dateEntry["severityIndex"], "3")
        accidentsBySeverity3 = me.getValue(entryAccidentsBySeverity3)
        severity3Size = lt.size(accidentsBySeverity3["severityLst"])
    except:
        severity3Size = 0
    
    return severity1Size, severity2Size, severity3Size

# ==============================
# Funciones de Comparacion
# ==============================

def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareSeveritys(severity1, severity2):
    severity = me.getKey(severity2)
    if severity1 == severity:
        return 0
    elif severity1 > severity:
        return 1
    else:
        return -1
"""
