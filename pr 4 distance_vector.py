# Practical 4
# distance_vector.py
# Program to implement Distance Vector Routing Protocol (Bellman-Ford style)

from copy import deepcopy

def init_vectors(nodes, adj):
    """
    Initialize distance vectors for each node.
    distvec[node][dest] = (cost, next_hop)
    """
    distvec = {}
    for n in nodes:
        dv = {}
        for d in nodes:
            if d == n:
                dv[d] = (0, n)
            else:
                dv[d] = (float('inf'), None)
        # immediate neighbors
        for neigh, cost in adj.get(n, []):
            dv[neigh] = (cost, neigh)
        distvec[n] = dv
    return distvec

def dv_update_once(distvec, nodes, adj):
    """
    Perform one iteration of distance vector updates.
    Each node updates its table based on its neighbors.
    """
    changed = False
    newvec = deepcopy(distvec)
    for u in nodes:
        for v, linkcost in adj.get(u, []):
            # u receives vector from v
            received = distvec[v]
            for dest in nodes:
                via_cost = linkcost + received[dest][0]
                if via_cost < newvec[u][dest][0]:
                    newvec[u][dest] = (via_cost, v)
                    changed = True
    return newvec, changed

def simulate_distance_vector(nodes, adj, max_iters=100):
    """
    Simulate DV routing until convergence or max_iters.
    """
    distvec = init_vectors(nodes, adj)
    print("Initial distance vectors:")
    for n in nodes:
        print(n, distvec[n])
    print()

    for it in range(max_iters):
        distvec, changed = dv_update_once(distvec, nodes, adj)
        print(f"After iteration {it+1}:")
        for n in nodes:
            print(" ", n, distvec[n])
        print()
        if not changed:
            print("✅ Converged after", it+1, "iterations.\n")
            break
    return distvec

def routing_table_from_dv(dv, node):
    """
    Build final routing table for one node.
    """
    rt = {}
    for dest, (cost, next_hop) in dv.items():
        if cost == float('inf'):
            rt[dest] = ("unreachable", None)
        else:
            rt[dest] = (next_hop, cost)
    return rt

if __name__ == "__main__":
    # Example network topology
    adj = {
        'A': [('B', 2), ('C', 5)],
        'B': [('A', 2), ('C', 6), ('D', 1)],
        'C': [('A', 5), ('B', 6), ('D', 2), ('E', 5)],
        'D': [('B', 1), ('C', 2), ('E', 1)],
        'E': [('C', 5), ('D', 1)]
    }

    nodes = sorted(adj.keys())
    final = simulate_distance_vector(nodes, adj)

    # Print final routing tables
    for n in nodes:
        print(f"Routing table for {n}:")
        rt = routing_table_from_dv(final[n], n)
        for dest in sorted(rt):
            print(" ", dest, "->", rt[dest])
        print()
