n = int(input())
time = []
for _ in range(n):
    a, b = map(int, input().split())
    time.append((a, b))
max_customers = float("-inf")
for i in range(n-1):
    curr_customer = time[i]
    curr_customers = 1
    for j in range(i+1, n):
        if time[j][0] <= curr_customer[1]:
            curr_customers += 1
        if time[j][0] > curr_customer[1]:
            curr_customers -= 1
    max_customers = max(max_customers, curr_customers)
print(max_customers)