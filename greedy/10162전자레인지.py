t = int(input()) # t초가 소요
btns = [300, 60, 10] # 5분, 1분, 10초

counts = [] # btn횟수 차례로 입력
for btn in btns:
    counts.append(t // btn)
    t = t % btn

if t != 0: # 나머지가 0이 아닐 때 -3
    print(-1)
else: # 나머지가 0 일 때 count 차례로 출력
    for count in counts:
        print(count)