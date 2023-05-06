# 듣고 싶은 과목 1~36
# n = 과목 수 
# m = 주어진 마일리지 
# li_p = 각 과목에 신청한 사람 수 
# li_l = 각 과목의 수강인원 수

n, m = map(int, input().split())
li = []

for _ in range(n):
    p, l = map(int, input().split())
    mileage = list(map(int, input().split()))
    mileage.sort(reverse=True)
    
    if len(mileage) < l:
        li.append(1)
    else:
        li.append(min(mileage[:l]))

li.sort()

cnt = 0
for i in li:
    if (m - i) >= 0:
        m = m - i
        cnt += 1
    else:
        break
        
print(cnt)

