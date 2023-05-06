n = int(input()) # 토핑 종류 
a,b = map(int, input().split()) # 도우의 가격, 토핑의 가격
c = int(input()) # 도우의 열량
d = [] # 토핑의 열량

for _ in range(n):
    d.append(int(input()))

d.sort(reverse=True)

answer = c / a

for i in range(1, len(d) + 1):
    calorie = c + sum(d[0:i])
    price = a + (b*i)

    if calorie / price > answer:
        answer = calorie /price
    else:
        break

print(int(answer))