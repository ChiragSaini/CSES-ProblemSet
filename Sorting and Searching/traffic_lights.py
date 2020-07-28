x, n = map(int, input().split())
p = list(map(int, input().split()))
added = set()
ans = []
for i in p:
    if any(range(i)) not in added:
        ans.append(n-i)
    else:
