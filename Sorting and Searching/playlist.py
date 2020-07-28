n = int(input())
k = list(map(int, input().split()))
# * GIVES TLE IN 4 CASES
# i = 0
# j = 1
# seen = set()
# seen.add(k[i])
# max_ans = 1
# curr_ans = 1
# while j < n:
#     if k[j] not in seen:
#         seen.add(k[j])
#         curr_ans += 1
#         j += 1
#     else:
#         curr_ans = 1
#         i += 1
#         seen = set()
#         seen.add(k[i])
#         j = i+1
#     max_ans = max(max_ans, curr_ans)
# print(max_ans)

# * 13 / 17 Test Cases Passed , 4 gives TLE

# * this ones gived wrong answer
lastIdx = {}
i = 0
ans = 1
for j in range(1, n):
    i = max(i, lastIdx.get(k[j])+1 if lastIdx.get(k[j]) is not None else 1)
    ans = max(ans, j-i+1)
    lastIdx[k[j]] = j
print(ans)
