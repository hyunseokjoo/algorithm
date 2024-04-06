# list.sort(key = <funcion>, reverse=True)
# sort 함수는 list만 정렬가능 
# 1 : basic sort, 2 : reverse=True sort 
list = [3,2,1,4]
list.sort()
print(list)

list.sort(reverse=True)
print(list)

list = [[50, 'apple'], [30, 'banana'],  [400, 'melon']]
list.sort(key=lambda x:x[0])
print(list)

# sorted(list, key=<function>, reverse=True)
list = [3,2,1,4]
print(sorted(list))
print(sorted(list, reverse=True))

list = [[50, 'apple'], [30, 'banana'],  [400, 'melon']]
print(sorted(list, key= lambda x: x[0]))
