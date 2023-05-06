# 딸기우유 1 -> 초코우유 1 -> 바나나우유 1 -> 딸기우유 1
# 길을 걸으면서 우유 먹기 
# 우유가계에는 [딸기 = 0, 초코 = 1, 바나나 = 2] 중 하나만 판매 

n = int(input()) # 가게 갯수
stores = list(map(int, input().split()))

cnt = 0
status = 0
for store in stores:
    if store == status:
        cnt += 1
        status += 1
        if status > 2:
            status = 0

print(cnt)