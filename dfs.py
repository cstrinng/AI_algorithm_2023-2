
def dfs_recursive(graph, node, visited_r):
	visited_r[node] = True   #�ش� ��� �湮 ó��
	print(node, end = ' ') #Ž�� ���� ���
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
			#stack.append(graph[n]) graph[n]�� ����Ʈ�� �߰���
		

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

dfs_recursive(graph, 1, visited_r) # ��� 1���� Ž�� ����
dfs_stack(graph, 1, visited_s)