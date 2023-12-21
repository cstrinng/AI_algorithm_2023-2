def find_min_weight_edge(adj_nodes, S, V_S):
    min_weight = float('inf')
    min_edge = None
    
    for u in S:
        for neighbor, weight in adj_nodes[u]:
            if neighbor in V_S and weight < min_weight:
                min_weight = weight
                min_edge = (u, neighbor)
    
    return min_edge


n, m, l = map(int, input().split())
adj_nodes = [[] for i in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj_nodes[u].append((v, w))
    adj_nodes[v].append((u, w))
    
S = set(int(input()) for _ in range(l))
V_S = set(range(n)) - S
    
min_edge = find_min_weight_edge(adj_nodes, S, V_S)
    
if min_edge:
    print(min_edge[0])
    print(min_edge[1])
else:
    print(-1)
    print(-1)

