# 1시간에 A 만큼 피로도 쓰고 B만큼 업무 처리 
# 1시간에 C 만큼 피로도 줄고 없무는 없음 피로도 0 이하는 0으로 치환 됨
# 피로도 최대 M 

a,b,c,m = map(int, input().split())

stress = 0 
hour = 0 
job = 0

while hour != 24:
    if (stress + a) <= m:
        stress += a
        job += b
    else:
        if stress - c >= 0:
            stress -= c
        else:
            stress = 0
    hour += 1 


print(job)