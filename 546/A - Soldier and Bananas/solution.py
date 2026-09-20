k, n , w = map(int, input().split())
 
w = w*(w + 1)/2
x = n - w*k 
if x >= 0:
    print(0)
else:
    print(int(-x))