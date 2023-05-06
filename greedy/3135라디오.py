# 1번 버튼 주파수 1 증가 
# 2번 버튼 주파수 2 감소 
# 나머지 N개의 버튼은 즐겨찾기용 

# 현재 주파수 A 듣고 싶은 주파수 B로 가는 최소 버튼 수 

a, b = map(int, input().split())
n = int(input())
htzs = []

for _ in range(n):
    htzs.append(int(input()))

# 제일 가까운 곳 찾기
diff = []
diff.append(abs(a - b))
for htz in htzs:
    diff.append(abs(htz - b))


if diff.index(min(diff)) >= 1:
    print(min(diff)+ 1)
else:
    print(min(diff))


