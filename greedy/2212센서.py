import sys

n = int(input()) # n개의 센서
k = int(input()) # 최대 집중국 갯수
sensor = list(map(int, input().split() )) # 센서 위치

if k >= n:
    print(0)
    sys.exit()

# sensor 내림 차순 정렬
sensor = sorted(sensor, reverse=True)

# sensor들간의 간격 구하기
dist = []
for i in range(len(sensor)-1):
    dist.append(sensor[i] - sensor[i+1])

# sensor들간의 간격 내림 차순 정렬
dist = sorted(dist, reverse=True)
for _ in range(k-1):
    dist.pop(0)
    
print(sum(dist))