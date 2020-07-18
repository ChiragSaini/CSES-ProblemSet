s = input()
maximum_length = 0
tmp = 1
for i in range(len(s)-1):
    if s[i] ==  s[i+1]:
        tmp += 1
    else:
        maximum_length = max(maximum_length, tmp)
        tmp  = 1
maximum_length = max(maximum_length, tmp)
print(maximum_length)