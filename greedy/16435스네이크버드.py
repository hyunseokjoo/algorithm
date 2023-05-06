"""
알고리즘 : 정렬

풀이 :
먹이(heights)의 수를 오름차순 정렬 후에
먹이가 l 값 아래의 값이면 l의 키를 키운다.
"""

n, l = map(int, input().split()) # 먹이 갯수, 처음 스네이크 길이 
heights = list(map(int, input().split())) # 먹이 위치

heights = sorted(heights) # 오른 차순 정렬
for height in heights:
    if l >= height:
        l += 1
        
print(l)