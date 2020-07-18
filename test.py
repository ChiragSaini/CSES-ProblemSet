# a = input()
# b = input()
# n1 = len(a)
# n2 = len(b)

# smaller = min(n1, n2)
# result = []

# for i in range(smaller):
#     result.append(a[i])
#     result.append(b[i])

# if smaller == n1:
#     for i in range(smaller, n2):
#         result.append(b[i])
# else:
#     for i in range(smaller, n1):
#         result.append(a[i])
        
# print("".join(result))
# from collections import defaultdict
# arr = list(map(int , input().split()))
# arr.sort()
# diffs = defaultdict(list)
# n = len(arr)
# for i in range(n-1):
#     diffs[arr[i+1] - arr[i]].append((arr[i+1], arr[i]))
# for pair in diffs[min(diffs)]:
#     print(*sorted(pair))