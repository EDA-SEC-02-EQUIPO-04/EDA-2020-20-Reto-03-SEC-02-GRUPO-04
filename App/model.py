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
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

Se define la estructura de un catálogo de libros.
El catálogo tendrá  una lista para los libros.

Los autores, los tags y los años se guardaran en
tablas de simbolos.
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'crimes': None,
                'dates': None
                }

    analyzer['crimes'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['dates'] = om.newMap(omaptype='BST', comparefunction=compareDates)
    return analyzer


# Funciones para agregar informacion al catalogo


def addCrime(analyzer, crime):
    """
    """
    lt.addLast(analyzer['crimes'], crime)
    addCrimeIndex(analyzer['dates'], crime)
    return analyzer


def addCrimeIndex(map, crime):
    occurreddate = crime['OCCURRED_ON_DATE']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    crimentry = om.get(map, crimedate.date())
    if crimentry is not None:
        lst = me.getValue(crimentry)
        lt.addLast(lst, crime)
    else:
        lst = lt.newList('SINGLE_LINKED', compareDates)
        lt.addLast(lst, crime)
        om.put(map, crimedate.date(), lst)


# ==============================
# Funciones de consulta
# ==============================


def crimesSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer['crimes'])


def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['dates'])


def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['dates'])


def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['dates'])


def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['dates'])


def getCrimesByRange(analyzer, initialDate, finalDate):
    lst = om.values(analyzer['dates'], initialDate, finalDate)
    return lst

# ==============================
# Funciones de Comparacion
# ==============================


def compareIds(id1, id2):
    """
    Compara dos ids de libros
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
