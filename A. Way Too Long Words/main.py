n = int(input())

for i in range(n):
    word = input()
    if len(word) <= 10:
        print(word)
    else:
        print(word[0],len(word)-2,word[len(word)-1],sep="") 
