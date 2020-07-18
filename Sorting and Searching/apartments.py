n,m,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
a.sort()
b.sort()
i = 0
j = 0
while (i < n):
    while j < m and b[j] < a[i]-k:
        j += 1
    if (j < m and b[j] <= a[i]+k):
        res += 1
        j += 1
    i += 1
print(res)