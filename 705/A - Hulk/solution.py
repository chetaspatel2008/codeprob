n = int(input())
feel = ""
for i in range(1,n+1):
    if i%2 == 1:
        feel += "I hate"
    else:
        feel += "I love"
 
    if i != n:
        feel += " that "
feel += " it"
print(feel)