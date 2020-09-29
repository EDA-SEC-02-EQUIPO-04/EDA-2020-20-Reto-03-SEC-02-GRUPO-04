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
#  Inicializacion del catálogo.
# ___________________________________________________


def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.new_analyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos.
# ___________________________________________________

def load_data(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo.
    """
    accidentsfile = cf.data_dir + accidentsfile
    with open(accidentsfile, encoding="utf-8") as input_file:
        reader = csv.DictReader(input_file, delimiter=",")
        for accident in reader:
            model.add_accident(analyzer, accident)
    return analyzer


# ___________________________________________________
#  Funciones para consultas.
# ___________________________________________________

def accidents_size(analyzer):
    """
    Número de crímenes leídos.
    """
    return model.crime_size(analyzer)


def inde_height(analyzer):
    """
    Altura del indice (árbol).
    """
    return model.index_height(analyzer)


def index_size(analyzer):
    """
    Numero de nodos en el árbol.
    """
    return model.index_size(analyzer)


def min_key(analyzer):
    """
    La menor llave del árbol.
    """
    return model.min_key(analyzer)


def max_key(analyzer):
    """
    La mayor llave del árbol.
    """
    return model.max_key(analyzer)


def get_accidents_by_date(analyzer, date):
    """
    Retorna el total de crimenes en una fecha específica, ordenados por severidad.
    """
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return model.get_accidents_by_date(analyzer, date.date())
