d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

# 1
dict_ = {k : v for k, v in d.items() if v >= 25}

# 2 : 명시적, for문 인자인 k, v가 tuple형태
dict_ = dict((k, v) for k, v in d.items() if v >= 25)

# >>> {'b': 33, 'd': 26, 'f': 120}


d = {'a': 8, 'b': 33, 'c': 15, 'd': 26, 'e': 12, 'f': 120}

# (k, v) --> idx (0, 1)
dict_ = dict(filter(lambda v : v[1] >= 25, d.items()))

# >>> {'b': 33, 'd': 26, 'f': 120}