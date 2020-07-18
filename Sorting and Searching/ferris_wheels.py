n, x = map(int, input().split())
p  = list(map(int, input().split()))
i = 0
res = 0
p.sort()
while (i < n):
    if i == n-1:
        if p[i] <= x:
            res += 1
            break
    if p[i] + p[i+1] <= x:
        i += 1
    res += 1
    i += 1
print(res)  