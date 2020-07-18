n, m = map(int, input().split())
h = list(map(int, input().split()))
t = list(map(int, input().split()))
for i in t:
    min_diff = float("inf")
    ans = None
    for j in h:
        if j <= i:
            min_diff = min(min_diff, abs(j-i))
            if min_diff ==  abs(j-i):
                ans = j
    if min_diff == float("inf"):
        print(-1)
    else:
        print(ans)
        h.pop(h.index(j))
        min_diff = float("inf")