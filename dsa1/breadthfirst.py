import matplotlib.pyplot as plt
import networkx as nx
from utils import runtime
from collections import deque

@runtime
def bfs(graph, start):
    visited = set()
    queue  = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')


def draw_graph(graph):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue',
            font_size=15, font_weight='bold', edge_color='gray')
    plt.show()




# draw_graph(graph)
