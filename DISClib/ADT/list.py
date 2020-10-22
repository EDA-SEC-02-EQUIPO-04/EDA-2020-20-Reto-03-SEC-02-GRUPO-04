"""
 * Copyright 2020, Departamento de sistemas y Computación,
 Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
from DISClib.Utils import error as error
from DISClib.DataStructures import liststructure as lt
assert config


"""
  Este módulo implementa el tipo abstracto de datos (TAD) lista.
  Se puede implementar sobre una estructura de datos encadenada de forma
  sencilla, doble o como un arreglo
"""


def newList(datastructure='SINGLE_LINKED', cmpfunction=None):
    """Crea una lista vacia

    Args:
        cmpfunction: Función de comparación para los elementos de la lista
    Returns:
        Una nueva lista
    Raises:
        Exception
    """
    try:
        lst = lt.newList(datastructure, cmpfunction)
        return lst
    except Exception as exp:
        error.reraise(exp, 'TADList->newList: ')


def addFirst(lst, element):
    """Agrega un elemento a la lista en la primera posicion.

    Agrega un elemento en la primera posición de la lista, se incrementa
    el tamaño de la lista en uno.

    Args:
        lst:  La lista don de inserta el elemento
        element:  El elemento a insertar en la lista

    Returns:
        La lista con el nuevo elemento en la primera posición, si el
        proceso fue exitoso

    Raises:
        Exception
    """
    try:
        lt.addFirst(lst, element)
    except Exception as exp:
        error.reraise(exp, 'TADList->addFirst: ')


def addLast(lst, element):
    """ Agrega un elemento en la última posición de la lista.

    Se adiciona un elemento en la última posición de la lista y se actualiza
    el apuntador a la útima posición. Se incrementa el tamaño de la lista en 1

    Args:
        lst: La lista en la que se inserta el elemento
        element: El elemento a insertar

    Raises:
        Exception
    """
    try:
        lt.addLast(lst, element)
    except Exception as exp:
        error.reraise(exp, 'TADList->addLast: ')


def isEmpty(lst):
    """ Indica si la lista está vacía

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lt.isEmpty(lst)
    except Exception as exp:
        error.reraise(exp, 'TADList->isEmpty: ')


def size(lst):
    """ Informa el número de elementos de la lista.

    Args
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lt.size(lst)
    except Exception as exp:
        error.reraise(exp, 'TADList->size: ')


def firstElement(lst):
    """ Retorna el primer elemento de una lista no vacía.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lt.firstElement(lst)
    except Exception as exp:
        error.reraise(exp, 'TADList->firstElement: ')


def lastElement(lst):
    """ Retorna el último elemento de una  lista no vacia.
        No se elimina el elemento.

    Args:
        lst: La lista a examinar

    Raises:
        Exception
    """
    try:
        return lt.lastElement(lst)
    except Exception as exp:
        error.reraise(exp, 'TADList->LastElement: ')


def getElement(lst, pos):
    """ Retorna el elemento en la posición pos de la lista.

    Se recorre la lista hasta el elemento pos, el cual  debe ser mayor
    que cero y menor o igual al tamaño de la lista.
    Se retorna el elemento en dicha posición sin eleminarlo.
    La lista no puede ser vacia.

    Args:
        lst: La lista a examinar
        pos: Posición del elemento a retornar

    Raises:
        Exception
    """
    try:
        return lt.getElement(lst, pos)
    except Exception as exp:
        error.reraise(exp, 'List->getElement: ')


def deleteElement(lst, pos):
    """ Elimina el elemento en la posición pos de la lista.

    Elimina el elemento que se encuentra en la posición pos de la lista.
    Pos debe ser mayor que cero y menor  o igual al tamaño de la lista.
    Se decrementa en un uno el tamñao de la lista. La lista no puede
    estar vacia.

    Args:
        lst: La lista a retoranr
        pos: Posición del elemento a eliminar.

    Raises:
        Exception
    """
    try:
        lt.deleteElement(lst, pos)
    except Exception as exp:
        error.reraise(exp, 'TADList->deleteElement: ')


def removeFirst(lst):
    """ Remueve el primer elemento de la lista.

    Elimina y retorna el primer elemento de la lista.
    El tamaño de la lista se decrementa en uno.
    Si la lista es vacía se retorna None.

    Args:
        lst: La lista a examinar

    Returns:
        El primer elemento de la lista
    Raises:
        Exception
    """
    try:
        return lt.removeFirst(lst)
    except Exception as exp:
        error.reraise(exp, 'TADList->removeFirst: ')


def removeLast(lst):
    """ Remueve el último elemento de la lista.

    Elimina el último elemento de la lista  y lo retorna en caso de existir.
    El tamaño de la lista se decrementa en 1.
    Si la lista es vacía  retorna None.

    Args:
        lst: La lista a examinar

    Returns:
        El ultimo elemento de la lista
    Raises:
        Exception
    """
    try:
        return lt.removeLast(lst)
    except Exception as exp:
        error.reraise(exp, 'TADList->removeLast: ')


def insertElement(lst, element, pos):
    """ Inserta el elemento element en la posición pos de la lista.

    Inserta el elemento en la posición pos de la lista.
    La lista puede ser vacía.
    Se incrementa en 1 el tamaño de la lista.

    Args:
        lst: La lista en la que se va a insertar el elemento
        element: El elemento a insertar
        pos: posición en la que se va a insertar el elemento,
        0 < pos <= size(lst)

    Raises:
        Exception
    """
    try:
        lt.insertElement(lst, element, pos)
    except Exception as exp:
        error.reraise(exp, 'TADList->insertElement: ')


def isPresent(lst, element):
    """ Informa si el elemento element esta presente en la lista.

    Informa si un elemento está en la lista.
    Si esta presente, retorna la posición en la que se encuentra
    o cero (0) si no esta presente. Se utiliza la función de comparación
    utilizada durante la creación de la lista para comparar los elementos.

    Args:
        lst: La lista a examinar
        element: El elemento a buscar
    Returns:

    Raises:
        Exception
    """
    try:
        return lt.isPresent(lst, element)
    except Exception as exp:
        error.reraise(exp, 'TADList->isPresent: ')


def exchange(lst, pos1, pos2):
    """ Intercambia la informacion en las posiciones pos1 y pos2 de la lista.

    Args:
        lst: La lista a examinar
        pos1: Posición del primer elemento
        pos2: Posiocion del segundo elemento

    Raises:
        Exception
    """
    try:
        lt.exchange(lst, pos1, pos2)
    except Exception as exp:
        error.reraise(exp, 'List->exchange: ')


def changeInfo(lst, pos, element):
    """ Cambia la informacion contenida en el nodo de la lista
        que se encuentra en la posicion pos.

    Args:
        lst: La lista a examinar
        pos: la posición de la lista con la información a cambiar
        newinfo: La nueva información que se debe poner en el nodo de
        la posición pos

    Raises:
        Exception
    """
    try:
        lt.changeInfo(lst, pos, element)
    except Exception as exp:
        error.reraise(exp, 'List->changeInfo: ')


def subList(lst, pos, numelem):
    """ Retorna una sublista de la lista lst.

    Se retorna una lista que contiene los elementos a partir de la
    posicion pos, con una longitud de numelem elementos.
    Se crea una copia de dichos elementos y se retorna una lista nueva.

    Args:
        lst: La lista a examinar
        pos: Posición a partir de la que se desea obtener la sublista
        numelem: Numero de elementos a copiar en la sublista

    Raises:
        Exception
    """
    try:
        return lt.subList(lst, pos, numelem)
    except Exception as exp:
        error.reraise(exp, 'List->subList: ')
