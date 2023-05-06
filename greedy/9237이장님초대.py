# n개의 묘목을 심는다 
# 묘목은 1개를 심는데 1일이 걸린다. 
# 묘목이 걸리는 시간은 배열로 입력해준다

n = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)

invite = []
p_day = 0
while len(times) > 0:
    invite.append(times.pop(0) + p_day)
    # 묘목을 심는날 하루가 추가 되었기 때문에 최대로 걸리는 날인 하루를 추가하여 더해준다.
    p_day += 1

print(max(invite)+2) # 묘목을 구입한 날 1일 이장님을 부를날 1일 총 2일 추가로 더하기