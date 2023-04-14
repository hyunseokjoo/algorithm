# 문자열 중복제거
# set함수를 이용하는 방법 (순서 보장 X)


from collections import OrderedDict
data = '111222333444'
print(''.join(set(data)))

# dict을 이용하는 방법
print(''.join(dict.fromkeys(data)))

# orderedDict로 변환 후 join 함수 사용
print(''.join(OrderedDict.fromkeys(data)))
