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
from DISClib.ADT import stack
from DISClib.Algorithms.Graphs import dfo
from DISClib.Utils import error as error
from DISClib.ADT import map
assert config


def KosarajuSCC(graph):
    """
    Implementa el algoritmo de Kosaraju
    para encontrar los componentes conectados
    de un grafo dirigido
    Args:
        graph: El grafo a examinar
    Returns:
        Una estructura con los componentes
        conectados
    Raises:
        Exception
    """
    try:
        scc = {
                'idscc': None,
                'marked': None,
                'grmarked': None,
                'components': 0
            }

        scc['idscc'] = map.newMap(g.numVertex(graph),
                                  maptype='PROBING',
                                  comparefunction=graph['comparefunction']
                                  )

        scc['marked'] = map.newMap(g.numVertex(graph), maptype='PROBING',
                                   comparefunction=graph['comparefunction']
                                   )
        scc['grmarked'] = map.newMap(g.numVertex(graph), maptype='PROBING',
                                     comparefunction=graph['comparefunction']
                                     )

        # Se calcula el grafo reverso de graph
        greverse = reverseGraph(graph)

        # Se calcula el DFO del reverso de graph
        dforeverse = dfo.DepthFirstOrder(greverse)
        grevrevpost = dforeverse['reversepost']

        # Se recorre el grafo en el orden dado por reversepost (G-reverso)
        scc['components'] = 1
        while (not stack.isEmpty(grevrevpost)):
            vert = stack.pop(grevrevpost)
            if not map.contains(scc['marked'], vert):
                sccCount(graph, scc, vert)
                scc['components'] += 1
        return scc
    except Exception as exp:
        error.reraise(exp, 'scc:Kosaraju')


def sccCount(graph, scc, vert):
    """
    Este algoritmo cuenta el número de componentes conectados.
    Deja en idscc, el número del componente al que pertenece cada vértice
    """
    try:
        map.put(scc['marked'], vert, True)
        map.put(scc['idscc'], vert, scc['components'])
        lstadjacents = g.adjacents(graph, vert)
        adjiterator = it.newIterator(lstadjacents)
        while it.hasNext(adjiterator):
            adjvert = it.next(adjiterator)
            if not map.contains(scc['marked'], adjvert):
                sccCount(graph, scc, adjvert)
        return scc
    except Exception as exp:
        error.reraise(exp, 'dfo:sccCount')


def stronglyConnected(scc, verta, vertb):
    """
    Dados dos vértices, informa si están fuertemente conectados o no.
    """
    try:
        scca = map.get(scc['idscc'], verta)['value']
        sccb = map.get(scc['idscc'], vertb)['value']
        if scca == sccb:
            return True
        return False
    except Exception as exp:
        error.reraise(exp, 'dfo:Sconnected')


def connectedComponents(scc):
    """
    Retorna el numero de componentes conectados
    """
    try:
        return scc['components']
    except Exception as exp:
        error.reraise(exp, 'scc:components')

# --------------------------------------------------
#              Funciones Auxiliares
# --------------------------------------------------


def reverseGraph(graph):
    """
        Retornar el reverso del grafo graph
    """
    try:
        greverse = g.newGraph(size=g.numVertex(graph),
                              directed=True,
                              comparefunction=graph['comparefunction']
                              )

        lstvert = g.vertices(graph)
        itervert = it.newIterator(lstvert)
        while it.hasNext(itervert):
            vert = it.next(itervert)
            g.insertVertex(greverse, vert)

        itervert = it.newIterator(lstvert)
        while it.hasNext(itervert):
            vert = it.next(itervert)
            lstadj = g.adjacents(graph, vert)
            iteradj = it.newIterator(lstadj)
            while it.hasNext(iteradj):
                adj = it.next(iteradj)
                g.addEdge(greverse, adj, vert)
        return greverse
    except Exception as exp:
        error.reraise(exp, 'scc:reverse')


def comparenames(searchname, element):
    return (searchname == element['key'])
