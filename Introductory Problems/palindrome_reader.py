def swap_items(s, i, j):
    print(f"S Before Swapping: {s}")
    first = s.pop(i)
    second  =s.pop(j-1)
    s.insert(i, second)
    s.insert(j, first)
    print(f"S After Swapping: {s}")
    return s

s = input()
s=  list(s)
n = len(s)
i = 0
j = n-1
no_solution = False
while (i <= j):
    print(f"S[i]:{s[i]}, S[j]:{s[j]}")
    if s[i] != s[j]:
        breaked = False
        for k in range(i+1, j):
            if s[k] == s[i]:
                s = swap_items(s, k, i)
                # print(f"S after swapping: {s}")
                breaked = True
                break
            elif s[k] == s[j]:
                s = swap_items(s, k, j)
                # print(f"S after swapping: {s}")
                breaked = True
                break
        if not breaked:
            no_solution = True
            print("NO SOLUTION")
            break
    i += 1
    j -= 1
if not no_solution:
    print("".join(s))