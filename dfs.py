
def dfs_recursive(graph, node, visited_r):
	visited_r[node] = True   #해당 노드 방문 처리
	print(node, end = ' ') #탐색 순서 출력
	for i in graph[node]: 
		if not visited_r[i]:
			dfs_recursive(graph, i, visited_r)

def dfs_stack(graph, node, visited_s):
	stack = [node]
		
	while stack:
		n = stack.pop()
		if not visited_s[n]:
			visited_s[n] = True
			print(n, end = ' ')
			stack += graph[n]
			#stack.append(graph[n]) graph[n]이 리스트로 추가됨
		

graph = [
    [],
    [2, 3],
    [1, 8],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7, 8],
    [6, 8],
    [2, 6, 7]
]	

visited_r = [False] * 9
visited_s = [False] * 9

dfs_recursive(graph, 1, visited_r) # 노드 1부터 탐색 시작
dfs_stack(graph, 1, visited_s)