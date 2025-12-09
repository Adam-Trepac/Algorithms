"""
Graph Traversal Algorithms (BFS & DFS)
Author: Adam Trepáč
Description: Implementation of Breadth-First Search (BFS) and Depth-First Search (DFS)
using an Adjacency Matrix representation.
"""

from collections import deque
from typing import List, Optional

class Graph:
    """
    Represents a directed graph using an Adjacency Matrix.
    Also stores state for traversal results (parents, distances, discovery times).
    """
    def __init__(self, size: int) -> None:
        self.size: int = size
        # Adjacency Matrix: matrix[u][v] is True if edge u -> v exists
        self.matrix: List[List[bool]] = [[False] * size for _ in range(size)]

        # Traversal State Storage
        self.parent: List[Optional[int]] = [None] * self.size
        self.distance: List[Optional[int]] = [None] * self.size
        self.visited: List[bool] = [False] * self.size
        
        # DFS specific timing
        self.discovery_time: List[Optional[int]] = [None] * self.size
        self.finishing_time: List[Optional[int]] = [None] * self.size

    def add_edge(self, u: int, v: int) -> None:
        """Adds a directed edge from u to v."""
        if 0 <= u < self.size and 0 <= v < self.size:
            self.matrix[u][v] = True

def get_neighbors(graph: Graph, u: int) -> List[int]:
    """Returns a list of all vertices v such that u -> v."""
    neighbors = []
    for v in range(graph.size):
        if graph.matrix[u][v]:
            neighbors.append(v)
    return neighbors

def bfs(graph: Graph, start_node: int) -> None:
    """
    Breadth-First Search (Iterative using Queue).
    Calculates shortest path distances from start_node in an unweighted graph.
    """
    # Reset state
    graph.visited = [False] * graph.size
    graph.distance = [None] * graph.size
    graph.parent = [None] * graph.size

    # Initialize start node
    graph.visited[start_node] = True
    graph.distance[start_node] = 0
    queue = deque([start_node])

    while queue:
        u = queue.popleft()
        # Process neighbors in sorted order for deterministic results
        for v in sorted(get_neighbors(graph, u)):
            if not graph.visited[v]:
                graph.visited[v] = True
                graph.parent[v] = u
                graph.distance[v] = graph.distance[u] + 1
                queue.append(v)

def dfs(graph: Graph, start_node: int) -> None:
    """
    Depth-First Search (Recursive).
    Calculates discovery and finishing times (useful for topological sort etc).
    """
    # Reset state
    graph.visited = [False] * graph.size
    graph.parent = [None] * graph.size
    graph.discovery_time = [None] * graph.size
    graph.finishing_time = [None] * graph.size
    
    time_counter = [0] # Mutable list to persist count across recursion

    def _dfs_visit(u: int):
        time_counter[0] += 1
        graph.discovery_time[u] = time_counter[0]
        graph.visited[u] = True
        
        for v in sorted(get_neighbors(graph, u)):
            if not graph.visited[v]:
                graph.parent[v] = u
                _dfs_visit(v)
                
        time_counter[0] += 1
        graph.finishing_time[u] = time_counter[0]

    _dfs_visit(start_node)

# --- Main Execution for Demonstration ---
if __name__ == "__main__":
    print("--- Graph Traversal Demo ---")
    
    # Create a simple graph with 5 nodes (0 to 4)
    g = Graph(5)
    edges = [(0, 1), (0, 3), (1, 2), (3, 4), (4, 1)]
    for u, v in edges:
        g.add_edge(u, v)

    print("Running BFS starting from Node 0...")
    bfs(g, 0)
    print(f"Distances from 0: {g.distance}")
    print(f"Parents (BFS tree): {g.parent}")

    print("\nRunning DFS starting from Node 0...")
    dfs(g, 0)
    print(f"Discovery Times: {g.discovery_time}")
    print(f"Finishing Times: {g.finishing_time}")
