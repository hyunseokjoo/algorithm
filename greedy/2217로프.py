n = int(input())
ropes = []

for i in range(n):
    ropes.append(int(input()))
    
ropes.sort(reverse=True)
result = []

for j in range(n):
    result.append(ropes[j] * (j+1))
    
print(max(result))
