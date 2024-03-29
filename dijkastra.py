import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
import heapq

def dijkstra(G, source):
    Q = []
    heapq.heappush(Q, (0, source))
    distances = {vertex: float('infinity') for vertex in G}
    distances[source] = 0
    visited = set()
    path = {}

    while Q:
        (dist, current_vertex) = heapq.heappop(Q)
        visited.add(current_vertex)

        yield current_vertex, visited.copy(), distances.copy()

        for neighbor in G[current_vertex]:
            distance = G[current_vertex][neighbor]['weight']
            if neighbor not in visited:
                old_cost = distances[neighbor]
                new_cost = distances[current_vertex] + distance
                if new_cost < old_cost:
                    heapq.heappush(Q, (new_cost, neighbor))
                    distances[neighbor] = new_cost
                    path[neighbor] = current_vertex

def visualize_dijkstra():
    G = nx.DiGraph()
    G.add_weighted_edges_from([
        ('A', 'B', 1), ('B', 'C', 2), ('A', 'D', 4),
        ('B', 'D', 2), ('D', 'E', 1), ('C', 'E', 5),
        ('E', 'F', 2), ('C', 'F', 3)])

    pos = nx.spring_layout(G)  # positions for all nodes

    fig, ax = plt.subplots()
    ax.set_title("Dijkstra's Algorithm Visualization")

    generator = dijkstra(G, 'A')

    def update(num):
        current_vertex, visited, distances = next(generator)
        ax.clear()
        nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue', ax=ax)
        nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='gray', ax=ax)
        nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif', ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), ax=ax)

        # Highlight the path and nodes
        nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='lightgreen', ax=ax)
        if current_vertex:
            nx.draw_networkx_nodes(G, pos, nodelist=[current_vertex], node_color='red', ax=ax)

    ani = animation.FuncAnimation(fig, update,cache_frame_data=False, frames=range(len(G)), repeat=True)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    visualize_dijkstra()