N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = [False] * (N + 1)  # bfs의 방문기록

for lst in graph:
    print(lst)

# 입력
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 출력
# 0와 연결된 노드 [False, False, False, False, False]
# 1와 연결된 노드 [False, False, True, True, True]
# 2와 연결된 노드 [False, True, False, False, True]
# 3와 연결된 노드 [False, True, False, False, True]
# 4와 연결된 노드 [False, True, True, True, False]