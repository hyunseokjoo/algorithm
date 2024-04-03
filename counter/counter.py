def hash_counter(t, array):
    counter = {}
    for target in array:
        if target in counter:
            counter[target] += 1
        else:
            counter[target] = 1

    return counter[t]

def list_counter(t, array):
    return array.count(t)

def for_counter(t, array):
    count = 0
    for target in array:
        if target == t:
            count += 1

    return count