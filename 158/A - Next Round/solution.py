n , k = map(int, input().split())
scores= list(map(int, input().split()))
finscore = scores[k - 1]
count = 0
for score in scores:
    if score >= finscore and score > 0:
        count += 1
 
print(count)