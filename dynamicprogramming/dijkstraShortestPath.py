"""
Python Program to solve Dijkstra shortest path problem.

Algorithm
1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree,
    i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty.
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE.
    Assign distance value as 0 for the source vertex so that it is picked first.
3) While sptSet doesn’t include all vertices:
    Pick a vertex u which is not there in sptSet and has minimum distance value.
    Include u to sptSet.
    Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices.
    For every adjacent vertex v, if the sum of a distance value of u (from source) and weight of edge u-v,
    is less than the distance value of v, then update the distance value of v.
"""

import sys


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.vertices):
            print(f"Node: {node}, to {dist[node]}")

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.vertices):
            if dist[v] < min and sptSet[v] is False:
                min = dist[v]
                min_index = v

        return min_index

    # Funtion that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        sptSet = [False] * self.vertices

        for cout in range(self.vertices):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.vertices):
                if (
                    self.graph[u][v] > 0
                    and sptSet[v] is False
                    and dist[v] > dist[u] + self.graph[u][v]
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


def printGraph(graph):
    for row in graph:
        print(row)


graph = Graph(9)
graph.graph = [
    [0, 5, 0, 0, 0, 0, 0, 13, 0],
    [4, 0, 9, 0, 0, 0, 0, 21, 0],
    [0, 8, 0, 7, 0, 2, 0, 0, 4],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0],
]

printGraph(graph.graph)
graph.dijkstra(0)
