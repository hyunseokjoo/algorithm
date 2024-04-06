arr = [2, 4, -10, 4, -9]
arr2 = sorted(list(set(arr)))
dic = {arr2[i] : i for i in range(len(arr2))}
""" 
출력
[-10, -9, 2, 4]
{-10: 0, -9: 1, 2: 2, 4: 3}
"""