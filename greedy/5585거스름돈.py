# 값 입력받기 
n = 1000 - int(input())

# 코인 종류 정의
coins = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coins:
    # 거스름돈보다 코인이 클 때만 진행 
    if n >= coin:
        # coin으로 나눈 몫을 더함
        count += n // coin
        # coin을 나눈 나머지 값을 다시 넣어서 다음 코인 진행
        n %= coin
        
print(count)