#sequence

import itertools
def solution(mylist):
    answer = list(map(''.join, itertools.permutations(mylist)))
    return answer
print(solution([1,2,3]))

from itertools import *

print(accumulate([1,2,3,4,5]))
print(count(10,3))
a = chain('abc','abd')
print(a)
print(permutations('abcd',2))

pool = ['A','B','C']
print(list(map(''.join, permutations(pool))))
print(list(map(''.join, permutations(pool,2))))

def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result
print(permute([1,2,3]))