numP = int(input())
sol = 0
for i in range(numP):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        sol += 1
print(sol)