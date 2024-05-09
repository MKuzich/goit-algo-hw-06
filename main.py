import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph()
G.graph['name'] = '11 Biggest Cities of Netherlands'

G.add_edge('Amsterdam', 'Utrecht', weight=45)
G.add_edge('Amsterdam', 'The Hague', weight=65)
G.add_edge('Rotterdam', 'Utrecht', weight=62)
G.add_edge('Rotterdam', 'The Hague', weight=24)
G.add_edge('Amsterdam', 'Zwolle', weight=103)
G.add_edge('Utrecht', 'Zwolle', weight=90)
G.add_edge('Utrecht', 'Arnhem', weight=65)
G.add_edge('Nijmegen', 'Arnhem', weight=19)
G.add_edge('Arnhem', 'Zwolle', weight=67)
G.add_edge('Nijmegen', 'Eindhoven', weight=73)
G.add_edge('Maastricht', 'Eindhoven', weight=88)
G.add_edge('Maastricht', 'Nijmegen', weight=140)
G.add_edge('Eindhoven', 'Rotterdam', weight=111)
G.add_edge('Amsterdam', 'Leeuwarden', weight=140)
G.add_edge('Leeuwarden', 'Groningen', weight=60)
G.add_edge('Groningen', 'Zwolle', weight=106)

options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 1,
    "with_labels": True
}
pos = nx.spring_layout(G)
nx.draw(G, pos, **options)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

print('Number of nodes: ', G.number_of_nodes())
print('Number of edges: ', G.number_of_edges())
print('Degree centrality: ', nx.degree_centrality(G))
print('Closeness centrality: ', nx.closeness_centrality(G))
print('Betweenness centrality: ', nx.betweenness_centrality(G))

def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

print('DFS recursive:')
dfs_recursive(G, 'Maastricht')

def bfs_recursive(graph, queue, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return
    vertex = queue.popleft()
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)
    bfs_recursive(graph, queue, visited)

print('\nBFS recursive:')
bfs_recursive(G, deque(['Maastricht']))

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        print(current_vertex, end=' ')
        for neighbor in list(graph.neighbors(current_vertex)):
            weight = graph[current_vertex][neighbor]['weight']
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

print('\nDijkstra:')
print(dijkstra(G, 'Maastricht'))