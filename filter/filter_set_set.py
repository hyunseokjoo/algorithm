# 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
# {1, 2, 3, 4, 5, 6}
set.union(a, b)
# {1, 2, 3, 4, 5, 6}

# 교집합
a & b
# {3, 4}
set.intersection(a, b)
# {3, 4}

# 차집합
a - b
# {1, 2}
set.difference(a, b)
# {1, 2}

# 대칭차집합
a ^ b
# {1, 2, 5, 6}
set.symmetric_difference(a, b)
# {1, 2, 5, 6}