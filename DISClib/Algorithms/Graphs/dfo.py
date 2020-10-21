"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import graph as g
from DISClib.ADT import queue
from DISClib.ADT import stack
from DISClib.ADT import map
from DISClib.Utils import error as error
assert config


def DepthFirstOrder(graph):
    try:
        search = {
                  'marked': None,
                  'pre': None,
                  'post': None,
                  'reversepost': None
                  }
        search['pre'] = queue.newQueue()
        search['post'] = queue.newQueue()
        search['reversepost'] = stack.newStack()
        search['marked'] = map.newMap(numelements=g.numVertex(graph),
                                      maptype='PROBING',
                                      comparefunction=graph['comparefunction']
                                      )
        lstvert = g.vertices(graph)
        vertiterator = it.newIterator(lstvert)
        while it.hasNext(vertiterator):
            vertex = it.next(vertiterator)
            if not (map.contains(search['marked'], vertex)):
                dfsVertex(graph, search, vertex)
        return search
    except Exception as exp:
        error.reraise(exp, 'dfo:DFO')


def dfsVertex(graph, search, vertex):
    """
    Genera un recorrido DFS sobre el grafo graph
    Args:
        graph:  El grafo a recorrer
        source: Vertice de inicio del recorrido.
    Returns:
        Una estructura para determinar los vertices
        conectados a source
    Raises:
        Exception
    """
    try:
        queue.enqueue(search['pre'], vertex)
        map.put(search['marked'], vertex, True)
        lstadjacents = g.adjacents(graph, vertex)
        adjiterator = it.newIterator(lstadjacents)
        while it.hasNext(adjiterator):
            adjvert = it.next(adjiterator)
            if not map.contains(search['marked'], adjvert):
                dfsVertex(graph,
                          search,
                          adjvert,
                          )
        queue.enqueue(search['post'], vertex)
        stack.push(search['reversepost'], vertex)
        return search

    except Exception as exp:
        error.reraise(exp, 'dfo:dfsVertex')


def comparenames(self, searchname, element):
    return (searchname == element['key'])
