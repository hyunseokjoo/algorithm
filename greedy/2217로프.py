"""
알고리즘 : 
그리디, 정렬

풀이 : 
정렬을 하여 각 위치 만큼 값 최대로 나올 수 있는 경우 찾아내기

예시 :
ropes = [26, 13, 11, 20]
reverse = [26, 20, 13, 11]
tot_weight = [26*1 = 26, 20*2 = 40, 13*3 = 39, 11*4 = 44 ]
"""


n = int(input()) # 로프 종류 갯수
ropes = []

for i in range(n):
    ropes.append(int(input())) # 로프 종류 받기
    
ropes.sort(reverse=True) # 로프 큰 순으로 역순으로 정렬
result = []

for j in range(n):
    result.append(ropes[j] * (j+1)) # 로프 종류 만큼 최대로 버틸 수 있는 무게
    
print(max(result))
