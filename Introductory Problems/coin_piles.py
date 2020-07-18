for _ in range(int(input())):
    a, b = map(int, input().split())
    while a > 0 and b > 0:
        if a > b:
            a -= 2
            b -= 1
        else:
            a -= 1
            b -= 2
    if a==0 and b==0:
        print("YES")
    else:
        print("NO")