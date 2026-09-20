n = int(input())
ori = input()
togo = input()
 
ans = 0
for i in range(n):
    a = int(ori[i])
    b = int(togo[i])
 
    diff = abs(a-b)
    ans += min(diff, 10 - diff)
print(ans)