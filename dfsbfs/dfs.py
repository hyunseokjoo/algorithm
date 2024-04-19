def dfs(g, start, visited):
    visited[start] = True
    print(v, end=' ')
    for i in g[v]:
        if not visited[i]:
            dfs(g, i, visited)

visited = [False] * 9 
