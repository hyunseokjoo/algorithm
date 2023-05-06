# n명의 원생 키 순서로 줄 세우기
# 총 K개의 조로 나눌려고 함 
# 각조의 티셔츠 맞추는 비용이 가장 키큰 원생과 가장 작은 키 원색의 차 


n, k = map(int, input().split())
students = list(map(int, input().split()))

students.sort(reverse=True)

diff = []
for i in range(n-1):
    diff.append(students[i] - students[i+1])

diff.sort(reverse=True)
print(sum(diff[k-1:]))
