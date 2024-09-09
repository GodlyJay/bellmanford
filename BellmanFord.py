# Step 1: Create the graph and add edges
V = 10  # Number of vertices in graph
edges = []

def add_edge(edges, u, v, w):
    edges.append((u, v, w))  # Add an edge to the graph

# Input graph

add_edge(edges, 0, 1, 2)
add_edge(edges, 0, 9, 2)
add_edge(edges, 1, 2, 6)
add_edge(edges, 2, 3, 10)
add_edge(edges, 2, 6, 6)
add_edge(edges, 2, 8, -4)
add_edge(edges, 3, 4, -7)
add_edge(edges, 5, 4, -5)
add_edge(edges, 6, 5, 2)
add_edge(edges, 6, 7, -2)
add_edge(edges, 7, 5, 4)
add_edge(edges, 8, 6, 3)
add_edge(edges, 8, 7, 6)
add_edge(edges, 9, 2, 3)
add_edge(edges, 9, 8, 4)

# Step 2: Define the Bellman-Ford algorithm function
def bellman_ford(vertices, edges, src):
    # Step 2.1: Initialize distances from src to all other vertices as INFINITY
    dist = [float("Inf")] * vertices
    dist[src] = 0

    # Step 2.2: Relax all edges |V| - 1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Step 2.3: Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return None

    return dist

# Step 3: Run the Bellman-Ford algorithm
distances = bellman_ford(V, edges, 0)

# Step 4: Print the results
if distances is not None:
    print("Vertex Distance from Source (0)")
    for i in range(len(distances)):
        print(f"{i}\t\t{distances[i]}")