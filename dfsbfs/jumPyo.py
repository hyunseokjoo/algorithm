
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()


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
# 1와 연결된 노드 [2, 3, 4]
# 2와 연결된 노드 [1, 4]
# 3와 연결된 노드 [1, 4]
# 4와 연결된 노드 [1, 2, 3]