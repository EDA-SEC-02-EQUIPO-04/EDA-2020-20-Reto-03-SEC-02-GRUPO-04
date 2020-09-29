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

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
""" Alternativa 3
def loadData(analyzer, accidentsfile):
    """
    #Carga los datos de los archivos CSV en el modelo
    """
    openFile = open(cf.data_dir + accidentsfile, encoding="utf-8")
    input_file = csv.DictReader(openFile, delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________


def accidentsSize(analyzer):
    return model.accidentsSize(analyzer)

def indexHeight(analyzer):
    return model.indexHeight(analyzer)

def indexSize(analyzer):
    return model.indexSize(analyzer)

def minKey(analyzer):
    return model.minKey(analyzer)

def maxKey(analyzer):
    return model.maxKey(analyzer)

def getAccidentsByDate(analyzer, date):
    return model.getAccidentsByDate(analyzer, date)

def getAccidentsBySeverity(analyzer, date):
    return model.getAccidentsBySeverity(analyzer, date)
"""
