n = int(input())   # 배열의 길이 
a = list(map(int, input().split())) # a 배열 값 받아오기
b = list(map(int, input().split())) # b 배열 값 받아오기

s = 0 # score 값 
for i in range(n):
    s += min(a) * max(b) # 최소값 되기 위해 (가장 작은 값 * 가장 큰 값)
    a.pop(a.index(min(a))) # a의 가장 작은 값 인덱스 구해서 pop으로 없애기
    b.pop(b.index(max(b))) # b의 가방 큰 값 인덱스 구해서 pop으로 없애기
    
print(s)