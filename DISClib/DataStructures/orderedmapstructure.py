"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config
from DISClib.DataStructures import bst as bst
from DISClib.DataStructures import rbt as rbt

assert config


def newMap(omaptype, comparefunction):
    """
    Crea una tabla de simbolos ordenada.
    Args:
        maptype: El tipo de map ordenado a utilizar
                 'BST' o 'RBT'
    Returns:
       La tabla de símbolos ordenada sin elementos
    Raises:
        Exception
    """
    if (omaptype == 'RBT'):
        return bst.newMap(comparefunction)
    else:
        return rbt.newMap(comparefunction)


def put(map, key, value):
    """
    Ingresa una pareja llave,valor. Si la llave ya existe,
    se reemplaza el valor.
    Args:
        map: La tabla de simbolos ordenada
        key: La llave asociada a la pareja
        value: El valor asociado a la pareja
    Returns:
        La tabla de simbolos
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.put(map, key, value)
    else:
        return rbt.put(map, key, value)


def get(map, key):
    """
    Retorna la pareja lleve-valor con llave igual a key
    Args:
        map: La tabla de simbolos
        key: La llave asociada a la pareja
    Returns:
        La tabla de simbolos con la nueva pareja
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.get(map, key)
    else:
        return rbt.get(map, key)


def remove(map, key):
    """
    Elimina la pareja llave,valor, donde llave == key.
    Args:
        map: La tabla de simbolos
        key: La llave asociada a la pareja
    Returns:
        La tabla de simbolos
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.remove(map, key)
    else:
        return rbt.remove(map, key)


def contains(map, key):
    """
    Informa si la llave key se encuentra en la tabla de hash
    Args:
        map: La tabla de simbolos
        key: La llave a buscar
    Returns:
        True si la llave está presente, False en caso contrario
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.contains(map, key)
    else:
        return rbt.contains(map, key)


def size(map):
    """
    Retorna el número de entradas en la tabla de simbolos
    Args:
        map: La tabla de simbolos
    Returns:
        El número de elementos en la tabla
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.size(map)
    else:
        return rbt.size(map)


def isEmpty(map):
    """
    Informa si la tabla de simbolos se encuentra vacia
    Args:
        map: La tabla de simbolos
    Returns:
        True si la tabla es vacía, False en caso contrario
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.isEmpty(map)
    else:
        return rbt.isEmpty(map)


def keySet(map):
    """
    Retorna una lista con todas las llaves de la tabla
    Args:
        map: La tabla de simbolos
    Returns:
        Una lista con todas las llaves de la tabla
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.keySet(map)
    else:
        return rbt.keySet(map)


def valueSet(map):
    """
    Construye una lista con los valores de la tabla
    Args:
        map: La tabla con los elementos
    Returns:
        Una lista con todos los valores
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.valueSet(map)
    else:
        return rbt.valueSet(map)


def minKey(map):
    """
    Retorna la menor llave de la tabla de simbolos
    Args:
        map: La tabla de simbolos
    Returns:
        La menor llave de la tabla
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.minKey(map)
    else:
        return rbt.minKey(map)


def maxKey(map):
    """
    Retorna la mayor llave de la tabla de simbolos
    Args:
        map: La tabla de simbolos
    Returns:
        La mayor llave de la tabla
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.maxKey(map)
    else:
        return rbt.maxKey(map)


def deleteMin(map):
    """
    Encuentra y remueve la menor llave de la tabla de simbolos
    y su valor asociado
    Args:
        map: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la menor llave
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.deleteMin(map)
    else:
        return rbt.deleteMin(map)


def deleteMax(map):
    """
    Encuentra y remueve la mayor llave de la tabla de simbolos
    y su valor asociado
    Args:
        map: La tabla de simbolos
    Returns:
        La tabla de simbolos sin la mayor llave
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.deleteMax(map)
    else:
        return rbt.deleteMax(map)


def floor(map, key):
    """
    Retorna la llave mas grande en la tabla de simbolos,
    menor o igual a la llave key
    Args:
        map: La tabla de simbolos
        key: La llave de búsqueda
    Returns:
        La llave más grande menor o igual a key
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.floor(map, key)
    else:
        return rbt.floor(map, key)


def ceiling(map, key):
    """
    Retorna la llave mas pequeña en la tabla de simbolos,
    mayor o igual a la llave key
    Args:
        map: La tabla de simbolos
        key: la llave de búsqueda
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.ceiling(map, key)
    else:
        return rbt.ceiling(map, key)


def select(map, k):
    """
    Retorna la siguiente llave a la k-esima llave mas pequeña de la tabla
    Args:
        map: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.select(map, k)
    else:
        return rbt.select(map, k)


def rank(map, key):
    """
    Retorna el número de llaves en la tabla estrictamente menores que key
    Args:
        map: La tabla de simbolos
        pos: la pos-esima llave mas pequeña
    Returns:
        La llave más pequeña mayor o igual a Key
    Raises:
        Exception
    """
    if (map['type'] == 'RBT'):
        return rbt.rank(map, key)
    else:
        return bst.rank(map, key)


def keys(map, keylo, keyhi):
    """
    Retorna todas las llaves del arbol que se encuentren entre
    [keylo, keyhi]

    Args:
        map: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.keys(map, keylo, keyhi)
    else:
        return rbt.keys(map, keylo, keyhi)


def height(map):
    """
    Retorna la altura del arbol de busqueda
    Args:
        map: La tabla de simbolos
    Returns:
        La altura del arbol
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.height(map)
    else:
        return rbt.height(map)


def values(map, keylo, keyhi):
    """
    Retorna todas los valores del arbol que se encuentren entre
    [keylo, keyhi]

    Args:
        map: La tabla de simbolos
        keylo: limite inferior
        keylohi: limite superiorr
    Returns:
        Las llaves en el rago especificado
    Raises:
        Exception
    """
    if (map['type'] == 'BST'):
        return bst.values(map, keylo, keyhi)
    else:
        return rbt.values(map, keylo, keyhi)
