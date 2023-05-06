"""
알고리즘 : 
그리디 

풀이 :
두 배열의 최대 값과 최솟값을 곱하여 최솟값 뽑기 : min * max
사용한 값제거하기 : pop

예시 : 

배열 안에 변수 총 갯수 : 5
a 배열 : 1 1 1 6 0
b 배열 : 2 7 8 3 1
최소 값 = 18

"""

n = int(input())   # 배열의 길이 
a = list(map(int, input().split())) # a 배열 값 받아오기
b = list(map(int, input().split())) # b 배열 값 받아오기

s = 0 # score 값 
for i in range(n):
    s += min(a) * max(b) # 최소값 되기 위해 (가장 작은 값 * 가장 큰 값)
    a.pop(a.index(min(a))) # a의 가장 작은 값 인덱스 구해서 pop으로 없애기
    b.pop(b.index(max(b))) # b의 가방 큰 값 인덱스 구해서 pop으로 없애기
    
print(s)