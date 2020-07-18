def minimum_subset_difference(arr) -> int:
    n = len(arr)
    w = sum(arr)
    t = [[False]*(w+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0] = True
    for i in range(1, n+1):
        for j in range(1, w+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j] = t[i-1][j]
    
    # print("printing dp matrix")
    # print("=="*50)
    # for row in t:
    #     print(row)
    # print("=="*50)
    
    min_diff = float("inf")
    for j in range(1,(w//2)+1):
        if t[n][j] == True:
            min_diff = min(min_diff, (w-2*j))
    return min_diff

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(minimum_subset_difference(arr))