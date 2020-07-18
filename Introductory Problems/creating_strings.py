from collections import Counter
from itertools import permutations, combinations 
def fact(i):
    res = 1
    for j in range(2, i+1):
        res *= j
    return res

s = input()
s = list(s)
n = len(s)
c = Counter(s)
print(c)
divisor = 0
for i in c:
    if c[i] > 1:
        divisor += c[i]

total_combinations = fact(n) // fact(divisor)
perm = combinations(s, n)
print(total_combinations)
for p in perm:
    print("".join(p))