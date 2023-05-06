# 과일우유. 드링킹요구르트  2+1 행사 중 
# 3개중 가장 싼 것은 무료 
# 3개를 사지 않는다면 정가로 구매 
# 가장 큰 값을 가진 순서대로 3개씩 묵으면 가장 최솟값이 됨

n = int(input()) # 유제품의 수

milk = []
for _ in range(n): # 유제품의 가격 
    milk.append(int(input()))


milk.sort(reverse=True) # 내림 차순으로 정렬

# 
batch = []
for i in range(n):
    if (i+1) % 3 != 0:
        batch.append(milk[i]) # 3번째 값 마다 없애기

print(sum(batch))


