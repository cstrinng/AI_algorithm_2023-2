def dijikstra_algorithm(start, end, adj_node):
    if neighbor in adj_node[start]





n, m = map(int, input().split())
adj_node = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    adj_node[u].append((v, w))
    adj_node[v].append((u, w))
    
S = set(i for i in range(n))