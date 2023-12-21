class Node:
    def __init__(self, v: int):
        self.v = v
        self.next = None

class Graph:
    def __init__(self, n: int):
        self.n = n
        self.adjlist = [None for _ in range(n)]

    def addEdge(self, u: int, v: int):
        e = Node(v)
        e.next = self.adjlist[u]
        self.adjlist[u] = e

        e = Node(u)
        e.next = self.adjlist[v]
        self.adjlist[v] = e

    def dfs(self, vertex, visited):
        visited[vertex] = True
        current = self.adjlist[vertex]
        while current:
            if not visited[current.v]:
                self.dfs(current.v, visited)
            current = current.next

    def solve(self) -> int:
        visited = [False] * self.n
        counts = 0

        for vertex in range(self.n):
            if not visited[vertex]:
                self.dfs(vertex, visited)
                counts += 1

        return counts


n, m = map(int, input().split(' '))
graph = Graph(n)
for _ in range(m):
    u, v = map(int, input().split(' '))
    graph.addEdge(u, v)
print(graph.solve())