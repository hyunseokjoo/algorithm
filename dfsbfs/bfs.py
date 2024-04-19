from collections import deque

def bfs(start):
    visited = [start]
    que = deque()
    que.append(start)
    while que: 
    	v = que.popleft()
        for w in G[v]:
            if not w in que:
            	visited.append(w)
                que.append(w)
	return visited