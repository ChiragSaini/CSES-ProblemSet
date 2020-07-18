n = int(input())
for i in range(1, n+1):
    total_positions = i*i
    a = total_positions*(total_positions-1) // 2
    if i > 2:
        a -= 4 * (i-1) * (i-2)    
    print(a)