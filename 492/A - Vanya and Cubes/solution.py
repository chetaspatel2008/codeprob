n = int(input())
height = 0
level = 1
while n >= level*(level + 1)//2:
    n -= level*(level + 1)//2
    height += 1
    level += 1
print(height)