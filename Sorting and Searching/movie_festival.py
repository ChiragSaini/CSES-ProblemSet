n = int(input())
movies = []
for _ in range(n):
    a, b = map(int, input().split())
    movies.append((a, b))
movies.sort()
# * [(3,5), (4,9), (5, 8)]
print(movies)
print("="*50)
ans = 1
curr = movies[0]
i = 1
while (i < n):
    print(f"Current:{curr}")
    print(f"Comapring: {movies[i]}")
    if movies[i][0] >= curr[1]:
        ans += 1
        curr = movies[i]
    i += 1
    print(f"Ans: {ans}")
    print("="*50)
print(ans)