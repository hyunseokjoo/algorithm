# 입력값 받기 
x = int(input())

bag = 0
# 5의 배수가 확인 되면 값을 0이기때문에 0이 될때 까지 loop를 돈다 
while x != 0:
	# 5의 배수 인지 확인
	if x % 5 == 0:
		bag += x // 5

	# 5의 배수가 될때까지 -3을 한다 
	x -= 3 
	bag += 1
	
	# 3보다 낮을 경우 
	if x < 0:
		bag = -1 

print(bag)
