n = int(input())
a = input()
a = a.lower()
b = 0
for i in range(97,123):
    if chr(i) in a:
        pass
    else:
        b = 1
if b == 1:
    print("NO")
else:
    print("YES")