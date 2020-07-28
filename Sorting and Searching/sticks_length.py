n = int(input())
p = list(map(int, input().split()))

# * O(n^2) Time Complexty --> Results: TLE
'''
costs = [0]*n
for i in range(n):
    tmp = 0
    for j in range(n):
        if i != j:
            tmp += abs(p[i] - p[j])
    costs[i] = tmp
print(min(costs))
'''
# * O(nlogn) Time Complexity Attempt -->
costs = [0]*n
p.sort()
if p[0] == p[-1]:
    print(0)
else:
    
    pass