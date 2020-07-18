for _ in range(int(input())):
    y, x = map(int, input().split()) # *  4, 2
    z = max(x, y)
    # * z = 4
    z2 = (z-1)**2
    # * z2 = 9
    ans = 0
    if z%2 == 1:
        if y == z:
            ans = z2+x
        else:
            ans = z2+2*z-y
    else:
        if x==z:
            ans = z2+y
        else:
            ans = z2+2*z-x
            
    print(ans)