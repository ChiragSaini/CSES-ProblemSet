n = int(input())
arr = list(map(int, input().split()))
turns = 0
for i in range(n-1):
    if arr[i+1] < arr[i]:
        turns += arr[i] - arr[i+1]
        arr[i+1]  = arr[i]
print(turns)