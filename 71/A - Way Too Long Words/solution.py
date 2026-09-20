n = int(input())
 
for i in range (n):
    word = input()
    l = len(word)
    if l > 10:
        print(word[0],(l-2),word[l-1], sep="")
    else:
        print(word)