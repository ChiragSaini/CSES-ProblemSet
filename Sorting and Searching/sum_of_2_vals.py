n, x = map(int, input().split())
a = list(map(int, input().split()))
nums = {}
ans = False
for i in range(n):
    if x  - a[i] in nums:
        print(nums[x-a[i]]+1, i+1)
        ans = True
        break
    else:
        nums[a[i]] = i
if not ans:
    print("IMPOSSIBLE")