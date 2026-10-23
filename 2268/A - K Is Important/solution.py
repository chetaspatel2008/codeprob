n = int(input())
 
for i in range(n):
    n , k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = len(arr)
    score = 0
    while (len(arr))> ( k - 1):
        m = len(arr)
        if arr[k - 1] > arr[m - k]:
            score += arr[k - 1]
            arr.pop(k - 1)
            
        else:
            score += arr[m - k]
            arr.pop(m - k)
    print(score)