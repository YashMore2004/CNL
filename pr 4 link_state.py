#practical 4
# link_state.py
# Simple Link-State demonstration using Dijkstra
import heapq

def dijkstra(adj, src):
    # adj: dict[node] = list of (neighbor, cost)
    dist = {n: float('inf') for n in adj}
    prev = {n: None for n in adj}
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, prev

def build_routing_table(prev, dist, src):
    # For each destination, find next hop from src
    routing = {}
    for dest in dist:
        if dest == src:
            continue
        if dist[dest] == float('inf'):
            routing[dest] = ("unreachable", None)
            continue
        # walk back from dest to src to find next hop
        cur = dest
        while prev[cur] is not None and prev[cur] != src:
            cur = prev[cur]
        next_hop = cur if prev[cur] is not None else dest
        routing[dest] = (next_hop, dist[dest])
    return routing

def pretty_print(adj, src):
    print("Graph adjacency list:")
    for k in adj:
        print(f"  {k} -> {adj[k]}")
    print()
    dist, prev = dijkstra(adj, src)
    print(f"Dijkstra from source: {src}")
    for node in sorted(dist):
        print(f"  {node}: cost={dist[node]}, prev={prev[node]}")
    print()
    routing = build_routing_table(prev, dist, src)
    print("Routing table (destination -> next_hop, cost):")
    for dest in sorted(routing):
        print(f"  {dest} -> {routing[dest]}")
    print()

if __name__ == "__main__":
    # Example graph (undirected)
    # Nodes: A,B,C,D,E
    adj = {
        'A': [('B', 2), ('C', 5)],
        'B': [('A', 2), ('C', 6), ('D', 1)],
        'C': [('A', 5), ('B', 6), ('D', 2), ('E', 5)],
        'D': [('B', 1), ('C', 2), ('E', 1)],
        'E': [('C', 5), ('D', 1)]
    }

    src = input("Enter source node (default A): ").strip() or 'A'
    if src not in adj:
        print("Source not in graph. Using A.")
        src = 'A'
    pretty_print(adj, src)

    # Demonstrate path from src to a destination
    dst = input("Enter destination to show path (or press Enter to quit): ").strip()
    if dst:
        # rebuild prev/dist
        dist, prev = dijkstra(adj, src)
        if dist.get(dst, float('inf')) == float('inf'):
            print(f"No path from {src} to {dst}")
        else:
            # reconstruct path
            path = []
            cur = dst
            while cur is not None:
                path.append(cur)
                cur = prev[cur]
            path.reverse()
            print(f"Shortest path {src} -> {dst}: {' -> '.join(path)} (cost {dist[dst]})")
